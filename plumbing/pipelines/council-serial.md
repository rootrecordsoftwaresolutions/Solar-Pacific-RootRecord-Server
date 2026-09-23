# Pipeline: council serial (staged)

AVA → Bruce → Carly → AVA

Each hop:
1. `single-flight.sh run council:<voice>:<ts> -- run-ollama.sh <voice-telegram|core> "…"`
2. Append to council scratch under `Database/intake/council/` (not skills/)
3. Next voice only after prior hop exits 0

Never parallelize the three voices.
