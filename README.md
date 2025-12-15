# Ask-the-Web AI Agent

A production-ready, modular AI agent that searches the web and provides informed answers using LangChain, Ollama, and DuckDuckGo Search.

## 🎯 Overview

Build an intelligent AI agent that can:
- 🔍 Search the web in real-time using DuckDuckGo
- 🤖 Reason over search results using local LLMs (no API keys!)
- 💬 Provide synthesized, informed answers
- 🎓 Learn AI agent development through 5 progressive modules
- 🚀 Deploy with modern web stack

**Perfect for:**
- Learning AI agent development from basics to advanced
- Building production-ready search agents
- Understanding LangChain and tool calling patterns
- Running LLMs locally without cloud dependencies

## ✨ Key Features

- 🐍 **Modular Python Architecture** - Clean, maintainable code structure
- 🎓 **Progressive Learning** - 5 step-by-step modules teaching agent concepts
- 🎨 **Modern Web UI** - React + Vite + Tailwind CSS interface
- 🔧 **FastAPI Backend** - Production-ready REST API
- 🚀 **One-Command Setup** - Automated installation scripts
- 🔍 **Real-time Search** - Live DuckDuckGo integration
- 📚 **Comprehensive Docs** - Setup, API, development, and troubleshooting guides
- 🧪 **Test Suite** - Automated testing infrastructure
- 🔓 **No API Keys** - Run completely locally with Ollama

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | FastAPI + LangChain + Ollama |
| **Frontend** | React 18 + Vite + Tailwind CSS |
| **LLM** | Mistral (via Ollama) |
| **Search** | DuckDuckGo Search API |
| **Language** | Python 3.8+ |

## 📋 Prerequisites

- **Python 3.8+** with pip
- **Node.js 18+** and npm (for web UI)
- **Ollama** ([download here](https://ollama.com))
- **Git** (optional)

## 🚀 Quick Start

### 1. Install Ollama & Model

```bash
# Download Ollama from https://ollama.com
# Then pull the Mistral model
ollama pull mistral

# Verify it's running
ollama list
```

### 2. Set Up the Project

**One-Command Setup (Recommended):**
```bash
cd Ask-the-web-agent
bash scripts/setup_all.sh
```

This automatically:
- Creates Python virtual environment
- Installs all Python dependencies
- Installs frontend dependencies
- Verifies Ollama installation

**Manual Setup:**
```bash
cd Ask-the-web-agent

# Python setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd frontend
npm install
cd ..
```

### 3. Start the Application

**Option A: Start Everything (Recommended)**
```bash
bash scripts/run_ui.sh
```

Then open **http://localhost:5173** in your browser! 🎉

**Option B: Manual Start (3 terminals)**

Terminal 1 - Ollama:
```bash
ollama serve
```

Terminal 2 - Backend:
```bash
cd Ask-the-web-agent
source .venv/bin/activate
uvicorn backend.app:app --reload
```

Terminal 3 - Frontend:
```bash
cd Ask-the-web-agent/frontend
npm run dev
```

### 4. Access the Application

- **Web UI**: http://localhost:5173
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 💡 Usage

### Web Interface

1. Open http://localhost:5173
2. Type your question (e.g., "What are the latest AI developments?")
3. Watch the agent search and reason in real-time
4. Get synthesized answers with sources

### CLI (Learning Mode)

Learn agent development step-by-step:

```bash
python main.py          # Interactive menu

# Or run specific steps
python main.py 1        # Step 1: Basic tools
python main.py 2        # Step 2: Manual tool calling
python main.py 3        # Step 3: Schema generation
python main.py 4        # Step 4: LangChain agent
python main.py 5        # Step 5: Web search agent
python main.py all      # Run all steps
```

### API Usage

```bash
# Using curl
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Python?"}'

# Using Python
import requests

response = requests.post('http://localhost:8000/ask', 
    json={'question': 'What is Python?'})
print(response.json()['answer'])
```

## 📁 Project Structure

```
Ask-the-web-agent/
├── 📂 src/                       # Core learning modules
│   ├── step1_basic_tool.py       # Basic tool implementation
│   ├── step2_manual_tool_calling.py  # Manual LLM tool calling
│   ├── step3_schema_generation.py    # Schema auto-generation
│   ├── step4_langchain_agent.py      # LangChain ReAct agent
│   └── step5_web_search_agent.py     # Web search agent ⭐
│
├── 📂 utils/                     # Shared utilities
│   ├── tools.py                  # Reusable tool functions
│   └── schemas.py                # Schema generation
│
├── 📂 backend/                   # FastAPI server
│   └── app.py                    # REST API
│
├── 📂 frontend/                  # React UI
│   ├── src/
│   │   ├── AskTheWeb.jsx        # Main component
│   │   └── App.jsx
│   └── package.json
│
├── 📂 tests/                     # Test suite
│   └── test_backend.py
│
├── 📂 scripts/                   # Setup & run scripts
│   ├── setup_all.sh             # Complete setup
│   └── run_ui.sh                # Start all servers
│
├── 📂 docs/                      # Documentation
│   ├── SETUP.md                 # Installation guide
│   ├── USER_GUIDE.md            # User documentation
│   ├── API.md                   # API reference
│   ├── DEVELOPER_GUIDE.md       # Development guide
│   ├── CONTRIBUTING.md          # Contribution guidelines
│   ├── TROUBLESHOOTING.md       # Common issues
│   └── PROJECT_STRUCTURE.md     # Architecture details
│
├── main.py                       # CLI entry point
├── requirements.txt              # Python dependencies
├── environment.yml               # Conda environment
└── README.md                     # This file
```

**Key Files:**
- `src/step5_web_search_agent.py` - Production web search agent (used by backend)
- `backend/app.py` - FastAPI server importing from src/
- `main.py` - Interactive CLI for learning modules

## 🎓 Learning Path

### The 5 Progressive Steps

Each module in `src/` teaches a specific concept:

| Step | Module | What You Learn | Key Concepts |
|------|--------|----------------|--------------|
| **1** | `step1_basic_tool.py` | Basic tool implementation | Function structure, docstrings, type hints |
| **2** | `step2_manual_tool_calling.py` | Manual LLM tool calling | Parsing LLM output, tool execution, JSON handling |
| **3** | `step3_schema_generation.py` | Auto schema generation | Function introspection, dynamic schemas |
| **4** | `step4_langchain_agent.py` | LangChain ReAct agent | LangChain framework, agent patterns, reasoning |
| **5** | `step5_web_search_agent.py` | Production web search | Real search integration, production patterns |

### Running the Learning Modules

```bash
# Interactive menu - recommended for beginners
python main.py

# Run specific step
python main.py 3

# Run all steps sequentially
python main.py all

# Run module directly
python -m src.step1_basic_tool
```

Each step includes:
- ✅ Working, runnable code
- ✅ Detailed comments and explanations
- ✅ Example outputs
- ✅ Progressive complexity

## 🧪 Testing

### Quick Test

```bash
# Test backend integration
python tests/test_backend.py
```

### API Testing

```bash
# Start backend first
uvicorn backend.app:app --reload

# Test endpoint
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is 2+2?"}'
```

### Run All Tests

```bash
# Using pytest
pytest tests/

# With coverage
pytest --cov=src --cov=utils --cov=backend tests/
```

## 🐛 Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**2. Ollama Connection Error**
```bash
# Check Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama
ollama serve

# Verify model exists
ollama list
ollama pull mistral  # if not installed
```

**3. Port Already in Use**
```bash
# macOS/Linux - kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**4. Frontend Won't Start**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

**5. Import Errors in Backend**
```bash
# Verify you're in the correct directory
cd Ask-the-web-agent

# Check Python path
python -c "import sys; print(sys.path)"

# Test imports
python -c "from src.step5_web_search_agent import create_web_search_agent"
```

For more solutions, see [docs/TROUBLESHOOTING.md](Ask-the-web-agent/docs/TROUBLESHOOTING.md)

## 📚 Documentation

Comprehensive guides available in `docs/`:

- **[SETUP.md](Ask-the-web-agent/docs/SETUP.md)** - Detailed installation guide
- **[USER_GUIDE.md](Ask-the-web-agent/docs/USER_GUIDE.md)** - Complete usage documentation
- **[API.md](Ask-the-web-agent/docs/API.md)** - REST API reference with examples
- **[DEVELOPER_GUIDE.md](Ask-the-web-agent/docs/DEVELOPER_GUIDE.md)** - How to extend and develop
- **[CONTRIBUTING.md](Ask-the-web-agent/docs/CONTRIBUTING.md)** - Contribution guidelines
- **[TROUBLESHOOTING.md](Ask-the-web-agent/docs/TROUBLESHOOTING.md)** - Common issues & solutions
- **[PROJECT_STRUCTURE.md](Ask-the-web-agent/docs/PROJECT_STRUCTURE.md)** - Architecture overview

## 🔧 Customization

### Add New Tools

1. **Define the tool** in `utils/tools.py`:
```python
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
```

2. **Add to agent** in `src/step5_web_search_agent.py`:
```python
from langchain.tools import tool
from utils.tools import calculate

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions"""
    return calculate(expression)

# Add to tools list
tools = [web_search, calculator]
```

3. **Test it**:
```bash
python -m src.step5_web_search_agent
# Try: "What is 25 * 47?"
```

### Switch LLM Models

Edit any step file or `backend/app.py`:

```python
# Faster, smaller model
agent = create_web_search_agent(model="gemma:2b")

# Better quality
agent = create_web_search_agent(model="llama3")

# Adjust temperature
llm = ChatOllama(model="mistral", temperature=0.7)
```

### Customize Agent Behavior

In `src/step5_web_search_agent.py`:

```python
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=5,        # Limit reasoning steps
    handle_parsing_errors=True,  # Graceful error handling
    early_stopping_method="generate"  # Stop when answer found
)
```

## 🚀 Deployment

### Backend (Railway, Render, Fly.io)

1. **Set environment variables:**
```bash
OLLAMA_BASE_URL=http://your-ollama-server:11434
```

2. **Dockerfile** (create if needed):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

3. **Deploy:**
```bash
# Railway
railway up

# Render - connect your repo
# Fly.io
fly deploy
```

### Frontend (Vercel, Netlify)

1. **Build:**
```bash
cd frontend
npm run build
```

2. **Deploy:**
```bash
# Vercel
vercel --prod

# Netlify
netlify deploy --prod --dir=dist
```

3. **Set environment variable:**
```bash
VITE_API_URL=https://your-backend-url.com
```

## ⚙️ Advanced Usage

### API Integration

**Python Client:**
```python
import requests

def ask_agent(question: str) -> dict:
    response = requests.post(
        'http://localhost:8000/ask',
        json={'question': question},
        timeout=60
    )
    return response.json()

result = ask_agent("Latest AI news?")
print(result['answer'])
```

**JavaScript/Node.js:**
```javascript
async function askAgent(question) {
    const response = await fetch('http://localhost:8000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    });
    return await response.json();
}

const result = await askAgent("Latest AI news?");
console.log(result.answer);
```

### Batch Processing

```python
questions = [
    "What is machine learning?",
    "Latest Python updates?",
    "Best practices for APIs?"
]

for q in questions:
    result = ask_agent(q)
    print(f"Q: {q}")
    print(f"A: {result['answer']}\n")
```

## 🎯 Architecture Highlights

### Why This Design?

1. **Modularity** - Each component is independently testable and maintainable
2. **Educational** - Progressive learning from basics to production patterns
3. **Scalability** - Easy to add tools, models, and features
4. **Production-Ready** - Follows best practices for Python projects
5. **Type Safety** - Full type hints for better IDE support and fewer bugs
6. **Documentation** - Comprehensive docs for all skill levels

### Key Design Patterns

- **ReAct Pattern** - Reasoning + Acting in LangChain agents
- **Tool Abstraction** - Reusable tool functions in `utils/`
- **Schema Generation** - Dynamic tool schemas from function signatures
- **API Gateway** - FastAPI as clean interface to agent backend
- **Component Separation** - Frontend, backend, and logic fully decoupled

## 📊 Performance Tips

1. **Use smaller models for development:**
   ```python
   llm = ChatOllama(model="gemma:2b")  # Fast, good for testing
   ```

2. **Implement caching:**
   ```python
   from functools import lru_cache
   
   @lru_cache(maxsize=100)
   def cached_search(query: str):
       return web_search(query)
   ```

3. **Limit agent iterations:**
   ```python
   agent = initialize_agent(..., max_iterations=3)
   ```

4. **Use async endpoints:**
   ```python
   @app.post("/ask")
   async def ask(req: AskRequest):
       # Your code
   ```

## 🤝 Contributing

We welcome contributions! Please see [docs/CONTRIBUTING.md](Ask-the-web-agent/docs/CONTRIBUTING.md) for:

- Code of conduct
- Development workflow
- Coding standards
- Pull request process
- Issue reporting guidelines

**Quick contribution steps:**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Format code: `black .` and `isort .`
6. Submit a pull request

## 📝 License

MIT License - Free for educational and commercial use!

See [LICENSE](Ask-the-web-agent/LICENSE) for details.

## 🙏 Acknowledgments

- **[LangChain](https://python.langchain.com/)** - Agent framework and tools
- **[Ollama](https://ollama.com/)** - Local LLM inference
- **[DuckDuckGo](https://duckduckgo.com/)** - Privacy-focused search API
- **[Mistral AI](https://mistral.ai/)** - Open-source language model
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework
- **[React](https://react.dev/)** - UI library
- **[Vite](https://vitejs.dev/)** - Frontend build tool

## 🎯 What's Next?

### Future Enhancements

- [ ] Streaming responses for real-time output
- [ ] Conversation history and memory
- [ ] More tools (calculator, weather, news APIs)
- [ ] Authentication and rate limiting
- [ ] Docker containerization
- [ ] Migration to LangGraph for complex workflows
- [ ] Multi-model support
- [ ] Advanced prompt engineering

### Learn More

- Read the [Developer Guide](Ask-the-web-agent/docs/DEVELOPER_GUIDE.md) to extend the agent
- Check [User Guide](Ask-the-web-agent/docs/USER_GUIDE.md) for advanced features
- Browse [API docs](Ask-the-web-agent/docs/API.md) for integration patterns

## 📞 Support

- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)
- **Documentation**: See `docs/` directory

## ⭐ Star Us!

If you find this project helpful, please consider giving it a star on GitHub!

---

**Built with ❤️ using LangChain, Ollama, FastAPI, and React**

*A modular, educational, production-ready AI agent implementation* 🚀
