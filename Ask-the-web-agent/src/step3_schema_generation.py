"""
Step 3: Standardized Schema Generation
Demonstrates automatic tool schema generation and usage with LLM
"""
import sys
from pathlib import Path
import json
from pprint import pprint

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from openai import OpenAI
from utils.tools import get_current_weather
from utils.schemas import to_schema


SYSTEM_PROMPT = """You are a helpful assistant with access to tools. When you need information that requires a tool, respond with:
TOOL_CALL: {"name": "tool_name", "args": {"arg1": "value1", "arg2": "value2"}}

Only use TOOL_CALL when you need to retrieve information. Otherwise, respond naturally."""


def generate_tool_schemas(tools):
    """Generate schemas for a list of tool functions"""
    return [to_schema(tool) for tool in tools]


def create_tool_spec_message(tool_schemas):
    """Create a formatted tool specification message"""
    return "Available tools:\n" + json.dumps(tool_schemas, indent=2)


def call_llm_with_schema(user_question, model="mistral"):
    """Call LLM with tool schemas included"""
    client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
    
    tools = [get_current_weather]
    tool_schemas = generate_tool_schemas(tools)
    tool_spec_message = create_tool_spec_message(tool_schemas)
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"Tool specifications:\n{tool_spec_message}"},
            {"role": "user", "content": user_question}
        ],
        temperature=0
    )
    
    return response.choices[0].message.content


def run_step3():
    """Run Step 3: Standardized schema generation"""
    print("=" * 60)
    print("STEP 3: Standardized Schema Generation")
    print("=" * 60)
    
    # Generate and display schema
    print("\nGenerating schema for get_current_weather:")
    tool_schema = to_schema(get_current_weather)
    pprint(tool_schema)
    
    # Test with LLM
    user_question = "What is the weather in San Diego today?"
    print(f"\n\nUser Question: {user_question}")
    print("\nCalling LLM with schema...")
    
    llm_output = call_llm_with_schema(user_question)
    
    print("\nLLM Response with Schema:")
    print(llm_output)
    
    print("\n✓ Step 3 complete: Schema generation working")
    print("=" * 60)


if __name__ == "__main__":
    run_step3()
