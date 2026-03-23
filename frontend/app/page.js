export default function Home() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">📊 Dashboard</h1>

      <div className="grid grid-cols-3 gap-6">
        
        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="text-lg">Total Documents</h2>
          <p className="text-3xl font-bold mt-2">12</p>
        </div>

        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="text-lg">Processed</h2>
          <p className="text-3xl font-bold mt-2">8</p>
        </div>

        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="text-lg">Pending</h2>
          <p className="text-3xl font-bold mt-2">4</p>
        </div>

      </div>
    </div>
  );
}