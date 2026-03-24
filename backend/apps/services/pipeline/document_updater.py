import json
import re
import os
import uuid
from django.conf import settings

from apps.services.parser.parser import parse_document
from apps.services.ai.gemini_agent import detect_changes_with_ai
from apps.services.merge.merge_engine import apply_changes

# Source Intelligence
from apps.services.source_intelligence.source_analyzer import (
    analyze_source_documents,
    consolidate_sources
)

# Page Engine
from apps.services.page_engine.page_splitter import split_document_by_page
from apps.services.page_engine.page_updater import update_pages

# Validation
from apps.services.validation.validator import (
    validate_pages,
    validate_final_document
)

# Stitch Engine
from apps.services.stitch.document_stitcher import stitch_documents


def update_document(main_doc, source_docs):

    print("🚀 Starting Enterprise Document Update Pipeline")

    # Create temp directory
    temp_dir = os.path.join(settings.MEDIA_ROOT, "temp")

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir, exist_ok=True)

    # Step 1 — Source Intelligence
    print("🧠 Step 1 — Source Intelligence")

    analyzed_sources = analyze_source_documents(source_docs)
    consolidated_source_text = consolidate_sources(analyzed_sources)

    # Step 2 — Page Split
    print("📄 Step 2 — Splitting Main Document")

    pages = split_document_by_page(
        main_doc.file.path,
        temp_dir
    )

    print(f"📄 Total Pages: {len(pages)}")

    # Step 3 — Page Update
    print("🤖 Step 3 — Updating Pages")

    updated_pages = update_pages(
        pages,
        consolidated_source_text,
        temp_dir
    )

    # Step 4 — Validation
    print("🔍 Step 4 — Validating Pages")

    valid_pages = validate_pages(updated_pages)

    # Step 5 — Stitch Documents
    print("📚 Step 5 — Stitching Final Document")

    output_dir = os.path.join(settings.MEDIA_ROOT, 'outputs')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    output_filename = f"updated_{main_doc.id}_{uuid.uuid4().hex}.docx"
    output_path = os.path.join(output_dir, output_filename)

    stitch_documents(valid_pages, output_path)

    # Step 6 — Final Validation
    print("🔍 Step 6 — Final Validation")

    validate_final_document(output_path)

    print("✅ Enterprise Document Update Complete")

    return os.path.join('outputs', output_filename)