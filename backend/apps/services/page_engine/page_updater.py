import os
import json
import re
import uuid

from apps.services.parser.parser import parse_document
from apps.services.ai.gemini_agent import detect_changes_with_ai
from apps.services.merge.merge_engine import apply_changes


def update_single_page(page, source_text, output_dir):
    """
    Update a single page using AI
    """

    page_path = page["path"]
    page_number = page["page_number"]

    print(f"🧠 Updating Page {page_number}")

    # Parse page text
    page_text = parse_document(page_path)

    # Detect changes for this page
    ai_result = detect_changes_with_ai(page_text, source_text)

    try:
        json_match = re.search(r'\[.*\]', ai_result, re.DOTALL)

        if json_match:
            json_text = json_match.group()
            changes = json.loads(json_text)

            print(f"✅ Page {page_number} - {len(changes)} changes")

        else:
            changes = []

    except Exception as e:
        print(f"❌ Page {page_number} AI error: {e}")
        changes = []

    # Output file
    filename = f"updated_page_{page_number}_{uuid.uuid4().hex}.docx"
    output_path = os.path.join(output_dir, filename)

    # Apply changes
    apply_changes(page_path, changes, output_path)

    return {
        "page_number": page_number,
        "path": output_path
    }


def update_pages(pages, source_text, output_dir):
    """
    Update multiple pages
    """

    updated_pages = []

    for page in pages:
        updated_page = update_single_page(page, source_text, output_dir)
        updated_pages.append(updated_page)

    return updated_pages