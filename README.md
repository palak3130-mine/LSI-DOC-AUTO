# LSI Document Automation System

An enterprise-grade, AI-powered document workflow system designed to synchronize and update large-scale reports (200+ pages) using multiple source data points.

## 🚀 Key Features
- **Intelligent Data Sync**: Automatically identifies and updates specific data points (dates, names, values, figures) from source files into a main report.
- **Large Document Support**: Optimized for 350+ combined pages using a specialized "Page Engine" that splits, updates, and restitches documents to maintain performance and formatting.
- **AI-Powered Precision**: Leverages Google Gemini 1.5/2.0 Flash for verbatim text extraction and accurate find-and-replace instructions.
- **Enterprise Validation**: Multi-step validation pipeline ensuring document integrity, structural consistency, and data accuracy after updates.
- **Format Agnostic**: Seamlessly handles and converts between PDF and DOCX formats.

## 📂 Project Documentation
For detailed information, please refer to the following documents:
- [**Quick Start Guide**](QUICK_START.md): Step-by-step setup and execution instructions.
- [**System Architecture**](system_architecture.md): Detailed breakdown of folders, files, and component responsibilities.
- [**Mental Model**](MENTAL_MODEL.md): Conceptual overview of the data flow and processing strategy.

## 🛠 Technology Stack
- **Backend**: Python 3.x, Django 6.0, Django REST Framework.
- **Frontend**: Next.js 14, React 18, Tailwind CSS.
- **AI**: Google Gemini Flash (via `google-genai`).
- **Document Processing**: `python-docx` (DOCX manipulation), `PyMuPDF` (PDF parsing).

## 📁 Repository Structure
```text
.
├── backend/                  # Django API and Processing Engine
│   ├── apps/                 # Application logic (Documents, Services)
│   ├── core/                 # Project configuration
│   └── media/                # File storage (Uploads & Outputs)
├── frontend/                 # Next.js Web Dashboard
│   ├── app/                  # UI Routes and Components
│   └── public/               # Static assets
├── QUICK_START.md            # Getting started guide
├── SYSTEM_ARCHITECTURE.md    # Codebase structure
└── MENTAL_MODEL.md           # Logical data flow
```

## 📝 License
Proprietary / LSI Internal.
