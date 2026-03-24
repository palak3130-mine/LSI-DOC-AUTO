# Quick Start Guide: LSI Document Automation

Follow these steps to get the project running on your local machine.

## Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **Google Gemini API Key** (Gemini 1.5 or 2.0 Flash)

---

## 1. Backend Setup (Django)

1. **Navigate to the backend folder**:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the `backend/` directory:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```

5. **Run Migrations & Start Server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   The backend will be available at `http://127.0.0.1:8000/`.

---

## 2. Frontend Setup (Next.js)

1. **Navigate to the frontend folder**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start Development Server**:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000/`.

---

## 3. Usage Instructions

1. Open `http://localhost:3000/upload` in your browser.
2. **Main Document**: Upload your large `.docx` template (supports 200+ pages).
3. **Source Documents**: Upload multiple `.pdf` or `.docx` files containing updated data.
4. Click **Process Documents**.
5. **Monitor the Terminal**: You will see real-time logs as the system splits the document, calls the AI, and validates the output.
6. Once complete, click the download link to retrieve your updated report.
