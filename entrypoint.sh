#!/bin/bash

# FastAPI 애플리케이션 실행
uvicorn main:app --host 0.0.0.0 --port 8000 &

# /ai/main.py 실행
python /app/cse/main.py &
python /app/AIE/main.py &
python /app/AI/main.py &
python /app/CBE/main.py &
python /app/EE/main.py &
python /app/kor/main.py &
python /app/mec/main.py &
python /app/SSE/main.py &

# register_user.py 실행
python /app/register_user.py &

# wait for all background processes
wait
