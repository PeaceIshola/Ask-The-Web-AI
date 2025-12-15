"""
Step 2: Manual Tool Calling with LLM
Demonstrates manual parsing of LLM output to call tools
"""
import sys
from pathlib import Path
import re
import json

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from openai import OpenAI
from utils.tools import get_current_weather


SYSTEM_PROMPT = """You are a helpful assistant with access to tools. When you need information that requires a tool, respond with:
TOOL_CALL: {"name": "tool_name", "args": {"arg1": "value1", "arg2": "value2"}}

Available tools:
- get_current_weather: Get the current weather for a city
  Arguments:
    - city (str): The name of the city
    - unit (str, optional): Temperature unit, either "celsius" or "fahrenheit". Defaults to "celsius"
  
Example:
User: "What's the weather in Tokyo?"
Assistant: TOOL_CALL: {"name": "get_current_weather", "args": {"city": "Tokyo"}}

Only use TOOL_CALL when you need to retrieve information. Otherwise, respond naturally."""


def create_llm_client():
    """Create OpenAI client for Ollama"""
    return OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")


def call_llm(client, user_question, model="mistral"):
    """Call the LLM with system prompt and user question"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_question}
        ],
        temperature=0
    )
    return response.choices[0].message.content


def parse_and_execute_tool(llm_output):
    """Parse LLM output and execute the tool if requested"""
    if "TOOL_CALL:" not in llm_output:
        print("No tool call detected in the LLM output.")
        return None
    
    # Extract everything after "TOOL_CALL:"
    tool_call_start = llm_output.find("TOOL_CALL:") + len("TOOL_CALL:")
    tool_call_text = llm_output[tool_call_start:].strip()
    
    # Find the JSON object (between first { and matching })
    brace_count = 0
    json_end = 0
    for i, char in enumerate(tool_call_text):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                json_end = i + 1
                break
    
    tool_call_json = tool_call_text[:json_end]
    tool_call_data = json.loads(tool_call_json)
    
    tool_name = tool_call_data["name"]
    tool_args = tool_call_data["args"]
    
    print(f"Calling tool `{tool_name}` with args {tool_args}")
    
    # Execute the tool
    if tool_name == "get_current_weather":
        result = get_current_weather(**tool_args)
        print(f"Result: {result}")
        return result
    else:
        print(f"Unknown tool: {tool_name}")
        return None


def run_step2():
    """Run Step 2: Manual tool calling with LLM"""
    print("=" * 60)
    print("STEP 2: Manual Tool Calling with LLM")
    print("=" * 60)
    
    client = create_llm_client()
    user_question = "What is the weather in San Diego today?"
    
    print(f"\nUser Question: {user_question}")
    print("\nCalling LLM...")
    
    llm_output = call_llm(client, user_question)
    
    print("\nLLM Response:")
    print(llm_output)
    
    print("\nParsing and executing tool...")
    parse_and_execute_tool(llm_output)
    
    print("\n✓ Step 2 complete: Manual tool calling working")
    print("=" * 60)


if __name__ == "__main__":
    run_step2()
