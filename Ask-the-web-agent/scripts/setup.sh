#!/bin/bash
# Quick setup script for Ask-the-Web Agent

echo "=========================================="
echo "Ask-the-Web Agent Setup"
echo "=========================================="

# Install Python dependencies
echo "\n📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "\n✓ Setup complete!"
echo "\nTo run the project:"
echo "  python main.py         # Interactive menu"
echo "  python main.py 1       # Run step 1"
echo "  python main.py all     # Run all steps"
echo "\nMake sure Ollama is running: ollama serve"
