# Add this line to /home/rootrecord/.ollama/skills/.gitignore

github-skill/scripts/poll-and-push.log

This keeps the poller's own log file from ever being staged/committed by
itself (it would otherwise show up as a "changed file" every single
minute forever).
