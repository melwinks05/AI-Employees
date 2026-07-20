import os
from google import genai
from decouple import config

# 1. Inject API key into system environment safely
os.environ["GEMINI_API_KEY"] = config('GEMINI_API_KEY').strip()

def ask_gemini_agent(prompt_text):
    client = genai.Client() 
    response = client.models.generate_content(
        model=config('GEMINI_MODEL'), 
        contents=prompt_text,
    )
    return response.text

if __name__ == "__main__":
    print("Sending request to Gemini...")
    try:
        # Changed the prompt text to ask for 5 animal names
        output = ask_gemini_agent("who is indias PM")
        print("\nOutput:\n", output)
    except Exception as e:
        print("\nRequest failed. Error details:", e)

for model in client.models.list():
    print(model.name)