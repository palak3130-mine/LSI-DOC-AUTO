"use client";

import { useState, useEffect } from "react";
import axios from "axios";

export default function WorkflowPage() {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDocs = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/documents/list/");
        setDocuments(res.data);
      } catch (err) {
        console.error("Failed to fetch documents", err);
      } finally {
        setLoading(false);
      }
    };
    fetchDocs();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">⚙️ Workflow Status</h1>
      
      <div className="bg-gray-800 rounded-xl overflow-hidden">
        <table className="w-full text-left">
          <thead className="bg-gray-700">
            <tr>
              <th className="p-4">ID</th>
              <th className="p-4">Type</th>
              <th className="p-4">Uploaded At</th>
              <th className="p-4">File</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan="4" className="p-4 text-center">Loading...</td></tr>
            ) : documents.length === 0 ? (
              <tr><td colSpan="4" className="p-4 text-center">No documents found</td></tr>
            ) : (
              documents.map((doc) => (
                <tr key={doc.id} className="border-t border-gray-700">
                  <td className="p-4">{doc.id}</td>
                  <td className="p-4">
                    <span className={`px-2 py-1 rounded text-xs font-bold ${doc.doc_type === 'MAIN' ? 'bg-blue-900 text-blue-200' : 'bg-green-900 text-green-200'}`}>
                      {doc.doc_type}
                    </span>
                  </td>
                  <td className="p-4">{new Date(doc.uploaded_at).toLocaleString()}</td>
                  <td className="p-4">
                    <a href={`http://127.0.0.1:8000${doc.file}`} target="_blank" className="text-blue-400 hover:underline">
                      View File
                    </a>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
