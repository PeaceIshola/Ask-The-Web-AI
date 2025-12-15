#!/bin/bash
# Complete setup for the Ask-the-Web Agent project

echo "=========================================="
echo "Ask-the-Web Agent - Complete Setup"
echo "=========================================="

echo "\n📦 Step 1: Installing Python dependencies..."
pip install -q -r requirements.txt

echo "\n📦 Step 2: Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "\n🤖 Step 3: Checking Ollama..."
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama not found. Please install from: https://ollama.com"
else
    echo "✓ Ollama is installed"
    echo "Pulling mistral model..."
    ollama pull mistral
fi

echo "\n=========================================="
echo "✓ Setup Complete!"
echo "=========================================="
echo "\nTo run Python steps:"
echo "  python main.py"
echo "\nTo run the full UI:"
echo "  ./run_ui.sh"
echo "  (or see UI_GUIDE.md for manual steps)"
echo "=========================================="
