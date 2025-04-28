import os
from dotenv import load_dotenv

load_dotenv()

def get_mistral_api_key():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable is not set in .env file")
    return api_key

def get_groq_api_key():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set in .env file")
    return api_key