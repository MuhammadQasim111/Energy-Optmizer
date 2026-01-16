'use client';

import { useEffect, useState } from 'react';
import KpiCard from '../../components/KpiCard';
import SpendChart from '../../components/SpendChart';
import { useRouter } from 'next/navigation';

export default function Dashboard() {
    const [data, setData] = useState<any>(null);
    const router = useRouter();

    useEffect(() => {
        const storedData = localStorage.getItem('energyData');
        if (storedData) {
            setData(JSON.parse(storedData));
        }
    }, []);

    const handleReset = () => {
        localStorage.removeItem('energyData');
        setData(null);
        router.push('/upload');
    };

    if (!data) {
        return (
            <main className="p-10 bg-gray-50 min-h-screen flex flex-col items-center justify-center">
                <h1 className="text-2xl font-bold mb-4">No Data API Found</h1>
                <p className="mb-4 text-gray-600">Please upload a file to see analytics.</p>
                <button
                    onClick={() => router.push('/upload')}
                    className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
                >
                    Go to Upload
                </button>
            </main>
        );
    }

    const { summary, monthly_spend, savings } = data;

    return (
        <main className="p-10 bg-gray-50 min-h-screen">
            <div className="flex justify-between items-center mb-8">
                <h1 className="text-3xl font-bold">Executive Dashboard</h1>
                <button
                    onClick={handleReset}
                    className="text-sm text-gray-500 hover:text-red-500 underline"
                >
                    Reset Data
                </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <KpiCard title="Total Spend" value={`$${(summary.total_spend / 1000000).toFixed(2)}M`} />
                <KpiCard title="Potential Savings" value={`$${(savings.total_potential_savings / 1000).toFixed(1)}k`} />
                <KpiCard title="Plants Analyzed" value={summary.plants.toString()} />
            </div>

            <div className="w-full">
                <SpendChart data={monthly_spend} />
            </div>
        </main>
    );
}
