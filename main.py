import argparse
import sys
import traceback

from agent.config import settings
from agent.graph import agent


def main():
    parser = argparse.ArgumentParser(description="Run engineering project planner")
    parser.add_argument("--recursion-limit", "-r", type=int, default=settings.recursion_limit,
                        help=f"Recursion limit (default: {settings.recursion_limit})")
    parser.add_argument("--prompt", "-p", help="Project prompt; otherwise read it interactively")

    args = parser.parse_args()

    try:
        user_prompt = args.prompt or input("Enter your project prompt: ").strip()
        if not user_prompt:
            parser.error("a non-empty project prompt is required")
        result = agent.invoke(
            {"user_prompt": user_prompt},
            {"recursion_limit": args.recursion_limit}
        )
        print("Final State:", result)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
