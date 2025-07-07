import os
from dotenv import load_dotenv
import pathlib

# Print current working directory
print("Current working directory:", os.getcwd())
print("Looking for .env file...")

# Get absolute path to the project root directory (where main.py is)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(project_root, '.env')
print("Looking for .env at:", env_path)
print(".env file exists:", os.path.exists(env_path))

# Try to load .env with explicit path
load_dotenv(env_path)

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

print("Debug - COHERE_API_KEY present:", "Yes" if COHERE_API_KEY else "No")
print("Debug - YOUTUBE_API_KEY present:", "Yes" if YOUTUBE_API_KEY else "No")
