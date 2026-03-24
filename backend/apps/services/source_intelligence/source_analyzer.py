import re
from apps.services.parser.parser import parse_document


def clean_text(text):
    """
    Clean extracted text for better AI processing
    """
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)

    # Remove multiple spaces
    text = re.sub(r'[ ]{2,}', ' ', text)

    return text.strip()


def extract_sections(text):
    """
    Attempt to split text into logical sections
    """
    sections = []

    # Split by headings (simple heuristic)
    pattern = r'\n([A-Z][A-Z\s]{3,})\n'

    splits = re.split(pattern, text)

    if len(splits) > 1:
        for i in range(1, len(splits), 2):
            heading = splits[i]
            content = splits[i + 1] if i + 1 < len(splits) else ""
            sections.append({
                "heading": heading.strip(),
                "content": content.strip()
            })
    else:
        sections.append({
            "heading": "FULL_DOCUMENT",
            "content": text
        })

    return sections


def analyze_source_documents(source_docs):
    """
    Analyze multiple source documents
    """
    analyzed_sources = []

    for source_doc in source_docs:
        file_path = source_doc.file.path

        print(f"Analyzing source: {file_path}")

        raw_text = parse_document(file_path)

        cleaned_text = clean_text(raw_text)

        sections = extract_sections(cleaned_text)

        analyzed_sources.append({
            "file": file_path,
            "sections": sections
        })

    return analyzed_sources


def consolidate_sources(analyzed_sources):
    """
    Convert structured sources into AI-ready context
    """
    consolidated_text = ""

    for source in analyzed_sources:
        consolidated_text += f"\n\n===== SOURCE FILE =====\n"
        consolidated_text += f"FILE: {source['file']}\n"

        for section in source["sections"]:
            consolidated_text += f"\nSECTION: {section['heading']}\n"
            consolidated_text += section["content"]
            consolidated_text += "\n"

    return consolidated_text