# Ask-the-Web Agent

A reproducible implementation of an AI agent that searches the web and provides informed answers using LangChain, Ollama, and DuckDuckGo Search.

## 🎯 Overview

This implementation demonstrates how to build an AI agent that can:
- Accept natural language questions
- Search the web for current information
- Reason over search results using a local LLM
- Provide synthesized, informed answers

**Tech Stack:**
- **Backend**: FastAPI + LangChain + Ollama (Mistral 7B)
- **Frontend**: React + Vite + TailwindCSS
- **Search**: DuckDuckGo Search API
- **LLM**: Local inference via Ollama

## 📋 Prerequisites

Before starting, ensure you have:

- **Python 3.11+** (via Conda/Miniconda)
- **Node.js 18+** and npm
- **Ollama** installed and running
- **Git** (optional, for cloning)

## 🚀 Setup Instructions

### Step 1: Install Ollama

Download and install Ollama from [https://ollama.com](https://ollama.com)

Pull the Mistral model:
```bash
ollama pull mistral:7b
```

Start the Ollama server (keep this running):
```bash
ollama serve
```

### Step 2: Create Conda Environment

Navigate to the work directory:
```bash
cd Ask-the-web-agent
```

Create and activate the environment:
```bash
conda env create -f environment.yml
conda activate web_agent
```

Register as Jupyter kernel (optional, for notebook):
```bash
python -m ipykernel install --user --name=web_agent --display-name "web_agent"
```

### Step 3: Install Frontend Dependencies

Navigate to the frontend folder:
```bash
cd frontend
npm install
cd ..
```

## 🎮 Running the Application

### Option 1: Using the Start Script (Recommended)

Run both servers with one command:
```bash
./start_servers.sh
```

This will start:
- Backend API on `http://localhost:8000`
- Frontend UI on `http://localhost:5173`

### Option 2: Manual Setup (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
conda activate web_agent
python -m uvicorn app:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Accessing the Application

Open your browser and navigate to:
```
http://localhost:5173
```

## 💡 How to Use

1. Type your question in the input field
2. Click "Ask" or press Enter
3. Watch the agent:
   - Search the web using DuckDuckGo
   - Reason over the results
   - Provide a synthesized answer

**Example Questions:**
- "What are the latest developments in AI in December 2025?"
- "What's happening in San Francisco this week?"
- "Explain quantum computing breakthroughs in 2025"

## 📁 Implementation Structure

```
Ask-the-web-agent/
├── ask_the_web_agent.ipynb    # Step-by-step tutorial notebook
├── environment.yml             # Reproducible environment specification
├── start_servers.sh            # Server startup script
├── README.md                   # This file
├── backend/
│   └── app.py                  # FastAPI backend with LangChain agent
└── frontend/
    ├── package.json            # Node dependencies
    ├── vite.config.js          # Vite configuration
    ├── src/
    │   ├── App.jsx            # Main React component
    │   ├── AskTheWeb.jsx      # UI component
    │   └── main.jsx           # React entry point
    └── index.html             # HTML template
```

## 🔧 Key Components

### Backend (`backend/app.py`)
- FastAPI server with CORS enabled
- LangChain ReAct agent with web search tool
- Integrates Mistral model via Ollama
- Exposes `/ask` endpoint for queries

### Frontend (`frontend/src/`)
- React UI with TailwindCSS styling
- Real-time question-answer interface
- Proxies requests to backend via Vite

### Agent Tools
- **web_search**: DuckDuckGo search integration
- Returns top 5 results with titles, URLs, and snippets
- Extensible - add more tools as needed

## 🐛 Troubleshooting

### Ollama Connection Error
**Problem**: Backend can't connect to Ollama  
**Solution**: 
```bash
ollama serve  # Start Ollama server
ollama list   # Verify mistral is installed
```

### Port Already in Use
**Problem**: Port 8000 or 5173 is busy  
**Solution**:
```bash
# Kill processes on ports
lsof -ti:8000 | xargs kill -9
lsof -ti:5173 | xargs kill -9
```

### Frontend Shows Blank Page
**Problem**: Frontend not loading  
**Solution**:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Backend Import Errors
**Problem**: Missing Python packages  
**Solution**:
```bash
conda activate web_agent
pip install fastapi uvicorn langchain langchain-community ddgs
```

## 📚 Reproducibility Guide

This implementation follows a structured tutorial approach in `ask_the_web_agent.ipynb`, allowing you to reproduce each component step-by-step:

1. **Section 1**: Environment setup and dependencies
2. **Section 2**: Manual tool calling implementation
3. **Section 3**: Tool schema standardization
4. **Section 4**: LangChain integration
5. **Section 5**: Web search agent implementation
6. **Section 6**: Minimal UI deployment

Each section includes working code, explanations, and validation steps to ensure reproducibility.

## 🎯 Extensions and Future Work

To extend this implementation:

- **Add more tools**: Weather API, news feeds, calculator
- **Improve prompts**: Better reasoning and answer formatting
- **Add streaming**: Real-time token streaming to frontend
- **Deploy**: Containerize with Docker for reproducible deployment
- **Switch models**: Experiment with llama3, phi3, or other models
- **Migrate to LangGraph**: For more advanced agent workflows

## 📄 API Documentation

Once the backend is running, interactive API documentation is available at:
```
http://localhost:8000/docs
```

This provides complete endpoint specifications for reproducing API calls.

## 🙏 Acknowledgments

- **LangChain**: Agent framework
- **Ollama**: Local LLM inference
- **DuckDuckGo**: Free search API
- **Mistral AI**: Open-source LLM

## 📝 License

This implementation is for educational and research purposes. Refer to individual package licenses for dependencies.

---

**Reproducible AI Research 🚀**

For questions about reproducing this work, refer to the step-by-step notebook or the troubleshooting section above.
