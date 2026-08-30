import os
from dotenv import load_dotenv



def main():
    print("Hello from ai-agent!")
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not found in environment variables.")

if __name__ == "__main__":
    main()
