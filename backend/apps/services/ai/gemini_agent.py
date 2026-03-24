from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def detect_changes_with_ai(main_text, source_text):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or "your_gemini_api_key" in api_key:
        print("⚠️ GEMINI_API_KEY is missing or invalid. Returning empty changes.")
        return "[]"

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a precise document editor. Your task is to update the MAIN DOCUMENT based on information found in the SOURCE DOCUMENT.

Follow these strict rules:
1. Identify specific data points (dates, names, values, statuses, figures) in the SOURCE DOCUMENT that update or correct information in the MAIN DOCUMENT.
2. For each update, find the EXACT string in the MAIN DOCUMENT that needs to be replaced. Copy it VERBATIM, including all spaces and punctuation.
3. Keep all other text, formatting, and structure of the MAIN DOCUMENT identical.
4. If a piece of information from the SOURCE DOCUMENT should be added to the MAIN DOCUMENT, find the text it should follow and use that as the "find" string. Then, in "replace", include the original text PLUS the new information.
5. Return ONLY a JSON array of change objects.

Return ONLY JSON:
[
  {{
    "find": "the exact string from the main document",
    "replace": "the updated string containing the new information"
  }}
]

If no updates are needed, return [].

MAIN DOCUMENT:
{main_text}

SOURCE DOCUMENT:
{source_text}
"""

    try:
        # Try latest Gemini model first
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if not response or not response.text:
            return "[]"

        return response.text

    except Exception as e:
        try:
            print("⚠️ gemini-2.5-flash failed, trying gemini-2.5-flash...")

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e2:
            print(f"❌ Gemini API Error: {e2}")
            return "[]"