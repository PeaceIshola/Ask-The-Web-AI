"""
Ask-the-Web Agent - Main Entry Point
Run all steps sequentially or individually
"""
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from src.step1_basic_tool import run_step1
from src.step2_manual_tool_calling import run_step2
from src.step3_schema_generation import run_step3
from src.step4_langchain_agent import run_step4
from src.step5_web_search_agent import run_step5


def print_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("Ask-the-Web Agent - Step-by-Step Demo")
    print("=" * 60)
    print("\nAvailable steps:")
    print("  1. Basic Tool Implementation")
    print("  2. Manual Tool Calling with LLM")
    print("  3. Standardized Schema Generation")
    print("  4. LangChain Agent with Tools")
    print("  5. Web Search Agent")
    print("  all. Run all steps")
    print("  q. Quit")
    print("=" * 60)


def run_all_steps():
    """Run all steps sequentially"""
    steps = [
        ("Step 1: Basic Tool Implementation", run_step1),
        ("Step 2: Manual Tool Calling", run_step2),
        ("Step 3: Schema Generation", run_step3),
        ("Step 4: LangChain Agent", run_step4),
        ("Step 5: Web Search Agent", run_step5),
    ]
    
    for step_name, step_func in steps:
        print(f"\n\n{'=' * 60}")
        print(f"Running {step_name}")
        print('=' * 60)
        try:
            step_func()
            print(f"\n✓ {step_name} completed successfully")
        except Exception as e:
            print(f"\n✗ {step_name} failed: {str(e)}")
        
        input("\nPress Enter to continue to next step...")


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Command line argument provided
        step = sys.argv[1]
        if step == "1":
            run_step1()
        elif step == "2":
            run_step2()
        elif step == "3":
            run_step3()
        elif step == "4":
            run_step4()
        elif step == "5":
            run_step5()
        elif step == "all":
            run_all_steps()
        else:
            print(f"Unknown step: {step}")
            print("Usage: python main.py [1|2|3|4|5|all]")
    else:
        # Interactive menu
        while True:
            print_menu()
            choice = input("\nEnter your choice: ").strip().lower()
            
            if choice == "q":
                print("\nGoodbye!")
                break
            elif choice == "1":
                run_step1()
            elif choice == "2":
                run_step2()
            elif choice == "3":
                run_step3()
            elif choice == "4":
                run_step4()
            elif choice == "5":
                run_step5()
            elif choice == "all":
                run_all_steps()
            else:
                print("\nInvalid choice. Please try again.")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
