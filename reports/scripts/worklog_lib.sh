#!/usr/bin/env bash
# Offline work auto-doc: file/folder create+modify (+delete of known paths).
# Path / size / mtime only. NO keystrokes, mouse, clipboard, or file contents.
set -euo pipefail

WORKLOG_DIR="${WORKLOG_DIR:-/home/rootrecord/Database/WORKLOG}"
CURRENT="${WORKLOG_DIR}/worklog_current.md"
STATE="${WORKLOG_DIR}/.last_scan"
HOUR_MARK="${WORKLOG_DIR}/.hour_start"
ENV_FILE="${ENV_FILE:-/home/rootrecord/master/master-key.env}"
PID_FILE="${WORKLOG_DIR}/.poller.pid"
SEEN_FILE="${WORKLOG_DIR}/.seen_index"
SEEN_DIRS="${WORKLOG_DIR}/.seen_dirs"

WATCH_ROOTS=(
  "/home/rootrecord/Database/DAILY AI DEV HANDOFF"
  "/home/rootrecord/Database/NETWORK"
  "/home/rootrecord/Documents"
  "/home/rootrecord/Desktop"
  "/home/rootrecord/Downloads"
  "/home/rootrecord/.ollama/skills"
)

ensure_dirs() {
  mkdir -p "$WORKLOG_DIR"
  chmod 700 "$WORKLOG_DIR" 2>/dev/null || true
  if [[ ! -f "$CURRENT" ]]; then
    printf '# Worklog current\n\nStarted: %s\n\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" > "$CURRENT"
    chmod 600 "$CURRENT" 2>/dev/null || true
  fi
  [[ -f "$HOUR_MARK" ]] || date '+%Y%m%d%H' > "$HOUR_MARK"
  [[ -f "${WORKLOG_DIR}/.segment_start" ]] || date '+%Y%m%d-%H%M%S' > "${WORKLOG_DIR}/.segment_start"
  [[ -f "$STATE" ]] || date '+%s' > "$STATE"
  [[ -f "$SEEN_FILE" ]] || : > "$SEEN_FILE"
  [[ -f "$SEEN_DIRS" ]] || : > "$SEEN_DIRS"
}

should_skip() {
  local p="$1"
  case "$p" in
    */Database/WORKLOG/*|*/Database/WORKLOG) return 0 ;;
    */Database/KEYLOGGER/*|*/Database/KEYLOGGER) return 0 ;;
    */Database/GITHUB/*|*/Database/GITHUB) return 0 ;;
    */.git/*|*/.git) return 0 ;;
    */node_modules/*|*/__pycache__/*|*/.cache/*) return 0 ;;
    *.log|*/logs/store/*|*/logs/*) return 0 ;;
    */.poller.pid|*/.last_scan|*/.hour_start|*/.segment_start|*/.seen_index|*/.seen_dirs|*/poller.out) return 0 ;;
    */.worklog-smoke*) return 0 ;;
  esac
  return 1
}

rotate_if_hour() {
  local now_h old_h seg_start end name
  now_h=$(date '+%Y%m%d%H')
  old_h=$(cat "$HOUR_MARK" 2>/dev/null || echo "$now_h")
  if [[ "$now_h" != "$old_h" ]]; then
    seg_start=$(cat "${WORKLOG_DIR}/.segment_start" 2>/dev/null || echo "$old_h")
    end=$(date '+%Y%m%d-%H%M%S')
    name="${seg_start}-${end}.md"
    [[ -f "$CURRENT" ]] && mv "$CURRENT" "${WORKLOG_DIR}/${name}" && chmod 600 "${WORKLOG_DIR}/${name}" 2>/dev/null || true
    printf '# Worklog current\n\nStarted: %s\n\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" > "$CURRENT"
    chmod 600 "$CURRENT" 2>/dev/null || true
    echo "$now_h" > "$HOUR_MARK"
    date '+%Y%m%d-%H%M%S' > "${WORKLOG_DIR}/.segment_start"
  fi
}

scrub_log() {
  [[ -f "$CURRENT" && -f "$ENV_FILE" ]] || return 0
  local tmp patterns=0 key val esc
  tmp=$(mktemp)
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ "$line" =~ ^[[:space:]]*# ]] && continue
    [[ "$line" =~ ^[[:space:]]*$ ]] && continue
    [[ "$line" != *=* ]] && continue
    key="${line%%=*}"; val="${line#*=}"; val="${val%$'\r'}"
    [[ "$val" =~ ^\".*\"$ ]] && val="${val:1:-1}"
    [[ "$val" =~ ^\'.*\'$ ]] && val="${val:1:-1}"
    [[ ${#val} -lt 8 ]] && continue
    if [[ "$key" == *_KEYLOG_DELETE || "$key" == *_WORKLOG_DELETE ]] || \
       { [[ "$key" =~ (KEY|TOKEN|SECRET|PASS|PASSWORD|CRED) ]] && [[ ${#val} -ge 12 ]]; }; then
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

# Returns: NEW_FILE | MOD_FILE via stdout side channel using globals is messy; print event lines.
scan_once() {
  ensure_dirs
  rotate_if_hour
  local now since tmp_list f sz mt key mt_h path_only prev events=0
  now=$(date '+%Y-%m-%d %H:%M:%S %Z')
  since=$(cat "$STATE" 2>/dev/null || date '+%s')
  since=$((since - 90))
  tmp_list=$(mktemp)

  # --- files ---
  for root in "${WATCH_ROOTS[@]}"; do
    [[ -d "$root" ]] || continue
    while IFS= read -r f; do
      should_skip "$f" && continue
      [[ -e "$f" ]] || continue
      sz=$(stat -c '%s' "$f" 2>/dev/null || echo 0)
      mt=$(stat -c '%Y' "$f" 2>/dev/null || echo 0)
      key="${f}|${sz}|${mt}"
      grep -Fxq "$key" "$SEEN_FILE" 2>/dev/null && continue
      path_only="$f"
      if grep -E "^${path_only//\//\\/}\\|" "$SEEN_FILE" >/dev/null 2>&1 || grep -F "|${path_only}|" <(echo) >/dev/null 2>&1; then
        :
      fi
      # NEW if path never seen; MOD if path seen with different sz|mt
      if grep -F "${f}|" "$SEEN_FILE" >/dev/null 2>&1; then
        printf 'MOD_FILE\t%s\t%s\t%s\n' "$key" "$f" "$sz"
      else
        printf 'NEW_FILE\t%s\t%s\t%s\n' "$key" "$f" "$sz"
      fi
    done < <(find "$root" -type f -newermt "@${since}" 2>/dev/null) >> "$tmp_list" || true
  done

  # --- directories (new folders) ---
  for root in "${WATCH_ROOTS[@]}"; do
    [[ -d "$root" ]] || continue
    while IFS= read -r f; do
      should_skip "$f" && continue
      [[ -d "$f" ]] || continue
      [[ "$f" == "$root" ]] && continue
      mt=$(stat -c '%Y' "$f" 2>/dev/null || echo 0)
      key="${f}|dir|${mt}"
      grep -Fxq "$f" "$SEEN_DIRS" 2>/dev/null && continue
      printf 'NEW_DIR\t%s\t%s\t0\n' "$key" "$f"
    done < <(find "$root" -mindepth 1 -type d -newermt "@${since}" 2>/dev/null) >> "$tmp_list" || true
  done

  # --- deletions: known paths missing (sample last 400 seen paths only — keep light) ---
  local check_tmp
  check_tmp=$(mktemp)
  tail -n 400 "$SEEN_FILE" 2>/dev/null | cut -d'|' -f1 | sort -u > "$check_tmp" || true
  tail -n 200 "$SEEN_DIRS" 2>/dev/null | sort -u >> "$check_tmp" || true
  sort -u "$check_tmp" -o "$check_tmp"
  while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    should_skip "$f" && continue
    if [[ ! -e "$f" ]]; then
      printf 'DELETED\t%s|gone\t%s\t0\n' "$f" "$f"
    fi
  done < "$check_tmp" >> "$tmp_list" || true
  rm -f "$check_tmp"

  if [[ -s "$tmp_list" ]]; then
    {
      echo "### $now"
      while IFS=$'\t' read -r kind key f sz; do
        [[ -z "${f:-}" ]] && continue
        case "$kind" in
          NEW_FILE|MOD_FILE)
            should_skip "$f" && continue
            mt_h=$(stat -c '%y' "$f" 2>/dev/null | cut -d. -f1 || echo '?')
            sz=$(stat -c '%s' "$f" 2>/dev/null || echo "${sz:-?}")
            printf -- '- %s %s | size=%s | mtime=%s\n' "$kind" "$f" "$sz" "$mt_h"
            # drop older keys for same path, append new
            if [[ -f "$SEEN_FILE" ]]; then
              grep -vF "${f}|" "$SEEN_FILE" > "${SEEN_FILE}.tmp" 2>/dev/null || true
              mv "${SEEN_FILE}.tmp" "$SEEN_FILE"
            fi
            printf '%s\n' "$key" >> "$SEEN_FILE"
            ;;
          NEW_DIR)
            should_skip "$f" && continue
            mt_h=$(stat -c '%y' "$f" 2>/dev/null | cut -d. -f1 || echo '?')
            printf -- '- NEW_DIR %s | mtime=%s\n' "$f" "$mt_h"
            printf '%s\n' "$f" >> "$SEEN_DIRS"
            ;;
          DELETED)
            printf -- '- DELETED %s\n' "$f"
            grep -vF "${f}|" "$SEEN_FILE" > "${SEEN_FILE}.tmp" 2>/dev/null || true
            mv "${SEEN_FILE}.tmp" "$SEEN_FILE" 2>/dev/null || true
            grep -vxF "$f" "$SEEN_DIRS" > "${SEEN_DIRS}.tmp" 2>/dev/null || true
            mv "${SEEN_DIRS}.tmp" "$SEEN_DIRS" 2>/dev/null || true
            ;;
        esac
      done < "$tmp_list"
      echo
    } >> "$CURRENT"
  fi
  rm -f "$tmp_list"
  date '+%s' > "$STATE"
  scrub_log
}
