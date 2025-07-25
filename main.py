import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")
    
    # Check if prompt is provided as command line argument
    if len(sys.argv) < 2:
        print("Error: Please provide a prompt as a command line argument.")
        print("Usage: uv run main.py \"Your prompt here\" [--verbose]")
        sys.exit(1)
    
    # Get the prompt from command line argument
    user_prompt = sys.argv[1]
    
    # Check if verbose flag is provided
    verbose = len(sys.argv) >= 3 and sys.argv[2] == "--verbose"
    
    # Print user prompt if verbose mode is enabled
    if verbose:
        print(f"User prompt: {user_prompt}")
    
    # Create a list of types.Content with the user's prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    # Generate content using Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages
    )
    
    # Print the response text
    print(response.text)
    
    # Print token usage information only if verbose mode is enabled
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

