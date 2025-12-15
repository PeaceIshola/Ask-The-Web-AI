# backend/app.py
"""
FastAPI backend for Ask-the-Web Agent
Uses modular Python files from src/ directory
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import the web search agent from our modular structure
from src.step5_web_search_agent import create_web_search_agent

# ----------------------------AGENT------------------------------------

# Create the web search agent using our modular code
agent = create_web_search_agent(model="mistral", verbose=True)
# ----------------------------------FASTAPI------------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(req: AskRequest):
    """Proxy the question to the LangChain agent and return its answer."""
    result = agent.invoke({"input": req.question})
    return {"answer": result["output"]}
