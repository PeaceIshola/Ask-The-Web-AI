"""
Step 1: Basic Tool Implementation
Demonstrates creating a simple weather tool function
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.tools import get_current_weather


def run_step1():
    """Run Step 1: Test basic weather tool"""
    print("=" * 60)
    print("STEP 1: Basic Tool Implementation")
    print("=" * 60)
    
    # Test the function
    print("\nTesting get_current_weather function:")
    print(get_current_weather("San Francisco"))
    print(get_current_weather("San Diego"))
    print(get_current_weather("Seattle", "fahrenheit"))
    
    print("\n✓ Step 1 complete: Basic tool implementation working")
    print("=" * 60)


if __name__ == "__main__":
    run_step1()
