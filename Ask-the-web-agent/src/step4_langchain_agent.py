"""
Step 4: LangChain Agent with Tools
Demonstrates using LangChain's ReAct agent for tool calling
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from langchain.tools import tool
from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType
from utils.tools import get_current_weather


@tool
def weather_check(city: str) -> str:
    """Get the current weather for a given city. Use this to check weather conditions.
    
    Args:
        city: The name of the city to check weather for
    
    Returns:
        A string describing the current weather conditions
    """
    return get_current_weather(city)


def create_langchain_agent(model="mistral", verbose=True):
    """Create a LangChain ReAct agent with weather tool"""
    llm = ChatOllama(model=model, temperature=0)
    tools = [weather_check]
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=verbose,
        handle_parsing_errors=True
    )
    
    return agent


def run_step4():
    """Run Step 4: LangChain agent with tools"""
    print("=" * 60)
    print("STEP 4: LangChain Agent with Tools")
    print("=" * 60)
    
    # Create the agent
    print("\nInitializing LangChain agent...")
    agent = create_langchain_agent()
    
    # Test the agent
    question = "Do I need an umbrella in Seattle today?"
    print(f"\nQuestion: {question}")
    print("\nAgent reasoning:")
    print("-" * 60)
    
    response = agent.invoke({"input": question})
    
    print("-" * 60)
    print("\nFinal Answer:")
    print(response['output'])
    
    print("\n✓ Step 4 complete: LangChain agent working")
    print("=" * 60)


if __name__ == "__main__":
    run_step4()
