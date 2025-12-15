#!/usr/bin/env python3
"""
Test the backend API without starting the full server
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 60)
print("Testing Backend Integration")
print("=" * 60)

print("\n1. Importing modules...")
try:
    from src.step5_web_search_agent import create_web_search_agent
    print("✓ Successfully imported web search agent")
except Exception as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

print("\n2. Creating agent...")
try:
    agent = create_web_search_agent(model="mistral", verbose=False)
    print("✓ Agent created successfully")
except Exception as e:
    print(f"✗ Agent creation failed: {e}")
    print("Note: Make sure Ollama is running (ollama serve)")
    sys.exit(1)

print("\n3. Testing simple question...")
try:
    result = agent.invoke({"input": "What is 2+2?"})
    print(f"✓ Agent responded: {result['output'][:100]}...")
except Exception as e:
    print(f"✗ Test failed: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ Backend integration test passed!")
print("=" * 60)
print("\nYou can now run the full UI:")
print("  Terminal 1: ollama serve")
print("  Terminal 2: cd backend && uvicorn app:app --reload")
print("  Terminal 3: cd frontend && npm run dev")
print("=" * 60)
