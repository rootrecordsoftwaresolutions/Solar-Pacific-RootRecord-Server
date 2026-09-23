#!/usr/bin/env bash
# Shared helpers for offline work auto-doc. No secrets printed.
set -euo pipefail

WORKLOG_DIR="${WORKLOG_DIR:-/home/rootrecord/Database/WORKLOG}"
CURRENT="${WORKLOG_DIR}/worklog_current.md"
STATE="${WORKLOG_DIR}/.last_scan"
HOUR_MARK="${WORKLOG_DIR}/.hour_start"
ENV_FILE="${ENV_FILE:-/home/rootrecord/master/master-key.env}"
PID_FILE="${WORKLOG_DIR}/.poller.pid"

WATCH_ROOTS=(
  "/home/rootrecord/Database"
  "/home/rootrecord/Documents"
  "/home/rootrecord/.ollama/skills"
)

ensure_dirs() {
  mkdir -p "$WORKLOG_DIR"
  chmod 700 "$WORKLOG_DIR" 2>/dev/null || true
  if [[ ! -f "$CURRENT" ]]; then
    printf '# Worklog current\n\nStarted: %s\n\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" > "$CURRENT"
    chmod 600 "$CURRENT" 2>/dev/null || true
  fi
  if [[ ! -f "$HOUR_MARK" ]]; then
    date '+%Y%m%d%H' > "$HOUR_MARK"
    date '+%Y%m%d-%H%M%S' > "${WORKLOG_DIR}/.segment_start"
  fi
  if [[ ! -f "$STATE" ]]; then
    # epoch seconds — only activity after this moment
    date '+%s' > "$STATE"
  fi
}

should_skip() {
  local p="$1"
  case "$p" in
    */Database/WORKLOG/*|*/Database/WORKLOG) return 0 ;;
    */Database/KEYLOGGER/*|*/Database/KEYLOGGER) return 0 ;;
    */Database/GITHUB/*|*/Database/GITHUB) return 0 ;;
    */.git/*|*/.git) return 0 ;;
    */node_modules/*|*/__pycache__/*) return 0 ;;
    */.poller.pid|*/.last_scan|*/.hour_start|*/.segment_start) return 0 ;;
  esac
  return 1
}

rotate_if_hour() {
  local now_h
  now_h=$(date '+%Y%m%d%H')
  local old_h
  old_h=$(cat "$HOUR_MARK" 2>/dev/null || echo "$now_h")
  if [[ "$now_h" != "$old_h" ]]; then
    local seg_start end name
    seg_start=$(cat "${WORKLOG_DIR}/.segment_start" 2>/dev/null || echo "$old_h")
    end=$(date '+%Y%m%d-%H%M%S')
    name="${seg_start}-${end}.md"
    if [[ -f "$CURRENT" ]]; then
      mv "$CURRENT" "${WORKLOG_DIR}/${name}"
      chmod 600 "${WORKLOG_DIR}/${name}" 2>/dev/null || true
    fi
    printf '# Worklog current\n\nStarted: %s\n\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" > "$CURRENT"
    chmod 600 "$CURRENT" 2>/dev/null || true
    echo "$now_h" > "$HOUR_MARK"
    date '+%Y%m%d-%H%M%S' > "${WORKLOG_DIR}/.segment_start"
  fi
}

# Build sed script from env values; never echo values.
scrub_log() {
  [[ -f "$CURRENT" ]] || return 0
  [[ -f "$ENV_FILE" ]] || return 0
  local tmp patterns=0
  tmp=$(mktemp)
  # Explicit delete keys + any KEY/TOKEN/SECRET/PASS values len>=12
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ "$line" =~ ^[[:space:]]*# ]] && continue
    [[ "$line" =~ ^[[:space:]]*$ ]] && continue
    [[ "$line" != *=* ]] && continue
    local key="${line%%=*}"
    local val="${line#*=}"
    val="${val%$'\r'}"
    # strip optional quotes
    if [[ "$val" =~ ^\".*\"$ ]]; then val="${val:1:-1}"; fi
    if [[ "$val" =~ ^\'.*\'$ ]]; then val="${val:1:-1}"; fi
    [[ ${#val} -lt 8 ]] && continue
    if [[ "$key" == *_KEYLOG_DELETE || "$key" == *_WORKLOG_DELETE ]] || \
       { [[ "$key" =~ (KEY|TOKEN|SECRET|PASS|PASSWORD|CRED) ]] && [[ ${#val} -ge 12 ]]; }; then
      # escape for sed
      local esc
      esc=$(printf '%s' "$val" | sed -e 's/[\\/&.^$*[\]]/\\&/g')
      printf 's/%s/[REDACTED]/g\n' "$esc" >> "$tmp"
      patterns=$((patterns+1))
    fi
  done < "$ENV_FILE"
  if [[ "$patterns" -gt 0 ]]; then
    sed -f "$tmp" "$CURRENT" > "${CURRENT}.scrub" && mv "${CURRENT}.scrub" "$CURRENT"
    chmod 600 "$CURRENT" 2>/dev/null || true
  fi
  rm -f "$tmp"
}

scan_once() {
  ensure_dirs
  rotate_if_hour
  local now seen_file tmp_list
  now=$(date '+%Y-%m-%d %H:%M:%S %Z')
  seen_file="${WORKLOG_DIR}/.seen_index"
  touch "$seen_file"
  tmp_list=$(mktemp)
  for root in "${WATCH_ROOTS[@]}"; do
    [[ -d "$root" ]] || continue
    find "$root" -type f 2>/dev/null | while IFS= read -r f; do
      should_skip "$f" && continue
      [[ -e "$f" ]] || continue
      local sz mt key
      sz=$(stat -c '%s' "$f" 2>/dev/null || echo 0)
      mt=$(stat -c '%Y' "$f" 2>/dev/null || echo 0)
      key="${f}|${sz}|${mt}"
      if grep -Fxq "$key" "$seen_file" 2>/dev/null; then
        continue
      fi
      printf '%s	%s
' "$key" "$f"
    done >> "$tmp_list" || true
  done
  if [[ -s "$tmp_list" ]]; then
    {
      echo "### $now"
      while IFS=$'	' read -r key f; do
        [[ -z "${f:-}" ]] && continue
        should_skip "$f" && continue
        local sz mt_h
        sz=$(stat -c '%s' "$f" 2>/dev/null || echo '?')
        mt_h=$(stat -c '%y' "$f" 2>/dev/null | cut -d. -f1 || echo '?')
        printf -- '- FILE %s | size=%s | mtime=%s
' "$f" "$sz" "$mt_h"
        printf '%s
' "$key" >> "$seen_file"
      done < "$tmp_list"
      echo
    } >> "$CURRENT"
  fi
  rm -f "$tmp_list"
  date '+%s' > "$STATE"
  scrub_log
  return 0
}

