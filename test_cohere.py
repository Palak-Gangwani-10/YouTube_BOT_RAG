import os
from dotenv import load_dotenv
import cohere

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("COHERE_API_KEY")
print("API key being used:", api_key[:5] + "..." if api_key else "No API key found")
print("Testing Cohere API key...")

try:
    # Initialize Cohere client
    co = cohere.Client(api_key)
    
    # Try a simple generate call
    response = co.generate(prompt='Say "hello"', max_tokens=5)
    print("Success! Your API key is valid.")
    print("Response:", response.generations[0].text)
    
except Exception as e:
    print("Error testing API key:", str(e)) 