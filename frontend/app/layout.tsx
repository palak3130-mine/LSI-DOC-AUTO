import "./globals.css";
import Link from "next/link";

export const metadata = {
  title: "Document Automation System",
  description: "AI-powered document workflow",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-900 text-white">
        <div className="flex h-screen">

          {/* Sidebar */}
          <aside className="w-64 bg-gray-800 p-5">
            <h2 className="text-xl font-bold mb-6">📄 Doc System</h2>

            <nav className="space-y-3">
              <Link href="/" className="block hover:text-blue-400">Dashboard</Link>
              <Link href="/upload" className="block hover:text-blue-400">Upload</Link>
              <Link href="/workflow" className="block hover:text-blue-400">Workflow</Link>
            </nav>
          </aside>

          {/* Main Area */}
          <div className="flex-1 flex flex-col">

            {/* Navbar */}
            <header className="h-16 bg-gray-800 flex items-center px-6 border-b border-gray-700">
              <h1 className="text-lg font-semibold">Document Automation</h1>
            </header>

            {/* Page Content */}
            <main className="flex-1 p-6 overflow-y-auto">
              {children}
            </main>

          </div>
        </div>
      </body>
    </html>
  );
}