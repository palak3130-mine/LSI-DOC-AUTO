from docx import Document


def save_to_docx(text, output_path):
    doc = Document()

    for line in text.split("\n"):
        doc.add_paragraph(line)

    doc.save(output_path)