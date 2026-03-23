import json
import re
import os
from django.conf import settings
from apps.services.parser.parser import parse_document
from apps.services.ai.gemini_agent import detect_changes_with_ai
from apps.services.merge.merge_engine import apply_changes
from apps.services.merge.file_writer import save_to_docx


def update_document(main_doc, source_docs):
    main_text = parse_document(main_doc.file.path)
    
    all_changes = []
    for source_doc in source_docs:
        print(f"Processing source: {source_doc.file.path}")
        source_text = parse_document(source_doc.file.path)
        ai_result = detect_changes_with_ai(main_text, source_text)
        
        try:
            json_match = re.search(r'\[.*\]', ai_result, re.DOTALL)
            if json_match:
                json_text = json_match.group()
                changes = json.loads(json_text)
                all_changes.extend(changes)
        except Exception as e:
            print(f"Error parsing AI result for {source_doc.file.name}: {e}")

    updated_text = apply_changes(main_text, all_changes)

    # Ensure output directory exists
    output_dir = os.path.join(settings.MEDIA_ROOT, 'outputs')
    os.makedirs(output_dir, exist_ok=True)
    
    output_filename = f"updated_{main_doc.id}.docx"
    output_path = os.path.join(output_dir, output_filename)
    
    save_to_docx(updated_text, output_path)

    # Return the relative path for URL generation
    return os.path.join('outputs', output_filename)