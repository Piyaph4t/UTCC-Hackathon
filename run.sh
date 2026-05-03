#!/bin/bash 

HOST=0.0.0.0
PORT=8000
uv run --env-file=.env fastapi dev "$(pwd)/app/main.py" --host $HOST --port $PORT
