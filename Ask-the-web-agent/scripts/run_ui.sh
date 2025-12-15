#!/bin/bash
# Start all servers for the Ask-the-Web Agent UI

echo "=========================================="
echo "Starting Ask-the-Web Agent Full Stack"
echo "=========================================="

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "\n⚠️  Ollama is not running!"
    echo "Please start Ollama in another terminal:"
    echo "  ollama serve"
    exit 1
fi

echo "\n✓ Ollama is running"

# Start backend in background
echo "\n🚀 Starting FastAPI backend on http://localhost:8000..."
cd backend && uvicorn app:app --reload --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Start frontend
echo "\n🎨 Starting React frontend on http://localhost:5173..."
cd ../frontend && npm run dev &
FRONTEND_PID=$!

echo "\n=========================================="
echo "✓ All servers running!"
echo "=========================================="
echo "\n📍 Open http://localhost:5173 in your browser"
echo "\n💡 To stop servers: Ctrl+C then run:"
echo "   kill $BACKEND_PID $FRONTEND_PID"
echo "=========================================="

# Wait for user to stop
wait
