import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    
    # using the variabl verbose let the user place --verbose anywhere in the
    # arguments and it will still work
    verbose = "--verbose" in sys.argv
    args = []
    # starts iterating of sys.argv after the program name (sys.argv[0])
    for arg in sys.argv[1:]:
        # makes sure not to append options to the args list to not pass them as
        # being part of the prompt.
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print(f'Usage: python3 {sys.argv[0]} "Prompt for the AI" [--verbose]')
        print("Exiting...")
        sys.exit(1)
    
    # Prepare a client with an API key to be able to prompt the LLM
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # Prompt the gemini model
    prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    # Get answer back and print the tokens used
    if verbose:
        print(f"User prompt: {messages[0]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

if __name__ == "__main__":
    main()
