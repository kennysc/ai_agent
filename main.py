import os
from dotenv import load_dotenv
from google import genai
import sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} ["Prompt for the AI"]')
    print("Exiting...")
    sys.exit(1)

# Prepare a client with an API key to be able to prompt the LLM
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Prompt the gemini model
prompt = sys.argv[1]
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

# Get answer back and print the tokens used
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
