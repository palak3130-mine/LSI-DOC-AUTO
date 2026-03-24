import os
from docx import Document


def stitch_documents(updated_pages, output_path):
    """
    Stitch multiple DOCX pages into one final document
    """

    print("📚 Stitching Updated Pages")

    final_doc = Document()

    # Sort pages by page number
    sorted_pages = sorted(updated_pages, key=lambda x: x["page_number"])

    for page in sorted_pages:
        page_path = page["path"]

        print(f"📄 Adding Page {page['page_number']}")

        sub_doc = Document(page_path)

        for element in sub_doc.element.body:
            final_doc.element.body.append(element)

    final_doc.save(output_path)

    print("✅ Stitching Complete")

    return output_path