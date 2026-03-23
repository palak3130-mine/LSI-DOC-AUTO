from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def detect_changes_with_ai(main_text, source_text):
    prompt = f"""
You are an AI document update engine.

Compare SOURCE document with MAIN document.

Extract only meaningful changes.

MAIN DOCUMENT:
{main_text[:4000]}

SOURCE DOCUMENT:
{source_text[:4000]}

Return ONLY JSON:
[
  {{
    "section": "...",
    "change": "..."
  }}
]
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text