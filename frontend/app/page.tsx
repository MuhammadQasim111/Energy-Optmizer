import Link from 'next/link';

export default function Home() {
  return (
    <main className="p-10 flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <div className="max-w-3xl text-center space-y-6">
        <h1 className="text-5xl font-bold tracking-tight text-gray-900">
          Find 5–12% Energy Savings From Your Utility Bills
        </h1>
        <p className="text-xl text-gray-600">
          Upload invoices. Get savings. No ERP integration.
        </p>
        <div className="flex gap-4 justify-center mt-8">
            <Link href="/upload" className="px-6 py-3 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition">
              Get Started
            </Link>
            <Link href="/dashboard" className="px-6 py-3 bg-white border border-gray-300 text-gray-700 rounded-lg font-medium hover:bg-gray-50 transition">
              View Demo
            </Link>
        </div>
      </div>
    </main>
  );
}
