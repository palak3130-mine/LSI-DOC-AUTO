"use client";

import { useState } from "react";
import axios from "axios";

export default function UploadPage() {
  const [mainFile, setMainFile] = useState(null);
  const [sourceFiles, setSourceFiles] = useState([]);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  // Upload function
  const uploadFile = async (file, type) => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("doc_type", type);

    return await axios.post(
      "http://127.0.0.1:8000/api/documents/upload/",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
  };

  const handleProcess = async () => {
    if (!mainFile || sourceFiles.length === 0) {
      setMessage("⚠️ Upload main + at least one source file");
      return;
    }

    try {
      setLoading(true);
      setMessage("");

      // Upload MAIN
      const mainRes = await uploadFile(mainFile, "MAIN");
      const mainId = mainRes.data.id;

      // Upload MULTIPLE SOURCE FILES
      const sourceIds = [];
      for (let i = 0; i < sourceFiles.length; i++) {
        const res = await uploadFile(sourceFiles[i], "SOURCE");
        sourceIds.push(res.data.id);
      }

      // Process with IDs
      const res = await axios.post(
        "http://127.0.0.1:8000/api/documents/process/",
        { main_id: mainId, source_ids: sourceIds }
      );

      setMessage(res.data.file);
    } catch (error) {
      console.error(error);
      setMessage("❌ Error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">📄 Upload Documents</h1>

      <div className="grid grid-cols-2 gap-6">
        
        {/* MAIN */}
        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="mb-3 font-semibold">Main Document</h2>
          <input
            type="file"
            onChange={(e) => setMainFile(e.target.files[0])}
          />
          {mainFile && <p className="mt-2">📄 {mainFile.name}</p>}
        </div>

        {/* MULTI SOURCE */}
        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="mb-3 font-semibold">Source Documents</h2>
          <input
            type="file"
            multiple
            onChange={(e) => setSourceFiles(e.target.files)}
          />

          <div className="mt-2 text-sm">
            {Array.from(sourceFiles).map((file, i) => (
              <p key={i}>📄 {file.name}</p>
            ))}
          </div>
        </div>

      </div>

      {/* BUTTON */}
      <button
        onClick={handleProcess}
        disabled={loading}
        className="mt-6 bg-blue-600 px-6 py-3 rounded-lg"
      >
        {loading ? "Processing..." : "🚀 Process Documents"}
      </button>

      {/* RESULT */}
      {message && message.startsWith('http') && (
        <div className="mt-6">
          <p className="text-green-400">✅ Done</p>
          <a
            href={message}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 underline font-bold"
          >
            📥 Download Updated Document
          </a>
        </div>
      )}

      {message && !message.startsWith('http') && (
        <div className="mt-6">
          <p className={message.startsWith('❌') ? "text-red-400" : "text-yellow-400"}>
            {message}
          </p>
        </div>
      )}
    </div>
  );
}