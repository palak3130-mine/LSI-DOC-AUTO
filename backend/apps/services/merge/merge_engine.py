from docx import Document


def replace_text_in_paragraph(paragraph, find_text, replace_text):
    """
    Replace text in paragraph while preserving formatting
    """
    if find_text in paragraph.text:
        inline = paragraph.runs
        for i in range(len(inline)):
            if find_text in inline[i].text:
                inline[i].text = inline[i].text.replace(find_text, replace_text)
                return True
    return False


def replace_text_in_table(table, find_text, replace_text):
    """
    Replace text inside tables
    """
    replaced = False

    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                if replace_text_in_paragraph(paragraph, find_text, replace_text):
                    replaced = True

    return replaced


def apply_changes(doc_path, changes, output_path):
    doc = Document(doc_path)

    for change in changes:
        find_text = change.get("find")
        replace_text = change.get("replace")

        if not find_text or not replace_text:
            continue

        replaced = False

        # Update paragraphs
        for paragraph in doc.paragraphs:
            if replace_text_in_paragraph(paragraph, find_text, replace_text):
                replaced = True

        # Update tables
        for table in doc.tables:
            if replace_text_in_table(table, find_text, replace_text):
                replaced = True

        if replaced:
            print(f"✅ Updated: {find_text[:50]}...")
        else:
            print(f"❌ Not found: {find_text[:50]}...")

    doc.save(output_path)
    return output_path