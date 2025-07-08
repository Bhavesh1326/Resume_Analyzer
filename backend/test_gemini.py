# test_gemini.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def test_gemini():
    try:
        print("Testing Gemini API...")
        genai.configure(api_key=GEMINI_API_KEY)
        
        # List available models
        print("\nAvailable models:")
        models = genai.list_models()
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
        
        # Test a simple prompt
        print("\nTesting with a simple prompt...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, Gemini! Can you tell me a short joke?")
        print("\nResponse:", response.text)
        
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    test_gemini()