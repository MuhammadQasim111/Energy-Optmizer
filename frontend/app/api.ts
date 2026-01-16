const API_URL = 'http://localhost:8000';

export async function uploadFile(file: File) {
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch(`${API_URL}/upload`, {
        method: 'POST',
        body: formData,
    });

    if (!res.ok) {
        const errorData = await res.json().catch(() => ({ detail: 'Unknown error' }));
        console.error("Server Error:", errorData);
        throw new Error(errorData.detail || 'Upload failed');
    }

    return res.json();
}
