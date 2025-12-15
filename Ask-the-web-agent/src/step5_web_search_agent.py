"""
Step 5: Web Search Agent
Demonstrates a Perplexity-style agent that searches the web
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from duckduckgo_search import DDGS
from langchain.tools import tool
from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType


@tool
def web_search(query: str) -> str:
    """Search the web for current information using DuckDuckGo.
    
    Args:
        query: The search query string
    
    Returns:
        A formatted string with search results including titles and URLs
    """
    ddgs = DDGS()
    results = ddgs.text(query, max_results=5)
    
    if not results:
        return "No results found."
    
    formatted_results = []
    for i, result in enumerate(results, 1):
        title = result.get('title', 'No title')
        url = result.get('href', 'No URL')
        snippet = result.get('body', 'No description')
        formatted_results.append(f"{i}. {title}\n   URL: {url}\n   {snippet}")
    
    return "\n\n".join(formatted_results)


def create_web_search_agent(model="mistral", verbose=True):
    """Create a LangChain agent with web search capability"""
    llm = ChatOllama(model=model, temperature=0)
    tools = [web_search]
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=verbose,
        handle_parsing_errors=True
    )
    
    return agent


def run_step5():
    """Run Step 5: Web search agent"""
    print("=" * 60)
    print("STEP 5: Web Search Agent (Perplexity-Style)")
    print("=" * 60)
    
    # Create the web search agent
    print("\nInitializing web search agent...")
    agent = create_web_search_agent()
    
    # Test with a question requiring current information
    question = "What are the latest developments in artificial intelligence in December 2024?"
    print(f"\nQuestion: {question}")
    print("\nAgent reasoning:")
    print("-" * 60)
    
    response = agent.invoke({"input": question})
    
    print("-" * 60)
    print("\nFinal Answer:")
    print(response['output'])
    
    print("\n✓ Step 5 complete: Web search agent working")
    print("=" * 60)


if __name__ == "__main__":
    run_step5()
