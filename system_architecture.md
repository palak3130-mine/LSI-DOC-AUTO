# System Architecture: LSI Document Automation

This document provides a high-level overview of the project's folder structure and the purpose of each component in the AI-powered document workflow system.

## Project Structure Overview

```text
lsi-document-automation/
├── backend/                  # Django (Python) Backend
│   ├── apps/                 # Core application logic
│   │   ├── documents/        # Document management (Upload/Models/Views)
│   │   ├── processing/       # Processing state & status tracking
│   │   ├── services/         # Enterprise-grade processing modules
│   │   │   ├── ai/           # Gemini AI Integration (Prompting & Intelligence)
│   │   │   ├── merge/        # Merge Engine (Precise text replacement)
│   │   │   ├── page_engine/  # Document splitting & page-by-page updating
│   │   │   ├── parser/       # Multi-format parsing (PDF & DOCX)
│   │   │   ├── pipeline/     # Main enterprise workflow orchestrator
│   │   │   ├── source_intelligence/ # Cross-document analysis & consolidation
│   │   │   ├── stitch/       # Document reconstruction (XML stitching)
│   │   │   └── validation/   # Post-process integrity & accuracy checks
│   ├── core/                 # Django project settings & URL config
│   ├── media/                # User-uploaded files and processed outputs
│   │   ├── documents/        # Original uploaded files
│   │   └── outputs/          # AI-generated updated documents
│   ├── manage.py             # Django CLI entry point
│   ├── requirements.txt      # Backend Python dependencies
│   └── .env                  # Environment variables (API Keys, DEBUG, etc.)
└── frontend/                 # Next.js (React) Frontend
    ├── app/                  # Next.js App Router (Pages & Layouts)
    │   ├── upload/           # Document Upload & Processing page
    │   ├── workflow/         # Processing history & Status page
    │   ├── globals.css       # Tailwind CSS & Global styles
    │   ├── layout.tsx        # Main UI shell (Sidebar/Navbar)
    │   └── page.js           # Dashboard / Landing page
    ├── public/               # Static assets (Images/Icons)
    ├── next.config.mjs       # Next.js configuration
    └── package.json          # Frontend Node.js dependencies
```

## Component Details

### **Backend Service Modules (`apps/services/`)**
- **`ai/`**: Manages communication with Google Gemini. Handles prompt engineering for verbatim extraction and fallback model logic.
- **`merge/`**: The precision tool for modifying `.docx` files. It preserves formatting while replacing text in paragraphs and tables.
- **`page_engine/`**: Handles scalability by splitting massive documents into manageable chunks (pages) for processing.
- **`parser/`**: Extracting clean text from diverse sources (PDF/DOCX) to provide context for the AI.
- **`pipeline/`**: Orchestrates the 6-step enterprise workflow: Parse -> Analyze -> Split -> Update -> Stitch -> Validate.
- **`source_intelligence/`**: Consolidates multiple source documents into a single "Source of Truth" to reduce AI costs and increase data consistency.
- **`stitch/`**: Reconstructs the final document from processed pages using low-level XML manipulation to ensure no loss of formatting.
- **`validation/`**: Automatically checks the final output for common errors, structural issues, and ensures the update instructions were followed correctly.

### **Frontend (Next.js)**
- **`app/upload/`**: Trigger point for the ID-based processing pipeline.
- **`app/workflow/`**: Real-time view of processed documents and download links.
- **`app/layout.tsx`**: Enterprise dark-themed UI wrapper.

## Enterprise Workflow
1. **Consolidation**: All source files are analyzed and combined.
2. **Page Splitting**: The 200+ page main document is split into individual chunks.
3. **Targeted Updating**: Only relevant pages are sent to the AI for updating.
4. **Formatting Reconstruction**: Pages are stitched back into a single document.
5. **Final Validation**: The output is validated before being released for download.
