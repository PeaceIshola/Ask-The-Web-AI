#!/bin/bash

# Start backend
echo "Starting backend server..."
cd "$HOME/Documents/Ask-The-Web-AI/Ask-the-web-agent/backend"
source /opt/miniconda3/etc/profile.d/conda.sh
conda activate web_agent
python -m uvicorn app:app --reload --port 8000 &
BACKEND_PID=$!

# Wait a bit for backend to start
sleep 3

# Start frontend
echo "Starting frontend server..."
cd "$HOME/Documents/Ask-The-Web-AI/Ask-the-web-agent/frontend"
npm run dev &
FRONTEND_PID=$!

echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "Servers are running!"
echo "Frontend: http://localhost:5173"
echo "Backend: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for user interrupt
wait
