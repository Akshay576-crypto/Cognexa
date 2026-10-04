const API_BASE_URL = "http://localhost:8000";

export async function apiRequest(
    endpoint,
    {
        method = "GET",
        body,
        token,
        form = false,
    } = {}
) {
    const headers = {};

    if (form) {
        headers["Content-Type"] =
            "application/x-www-form-urlencoded";
    } else {
        headers["Content-Type"] =
            "application/json";
    }

    if (token) {
        headers["Authorization"] =
            `Bearer ${token}`;
    }

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            method,
            headers,
            body: form
                ? new URLSearchParams(body).toString()
                : body
                    ? JSON.stringify(body)
                    : undefined,
        }
    );

    let data = null;

    try {
        data = await response.json();
    } catch {
        data = null;
    }

    if (!response.ok) {
        throw new Error(
            data?.detail ||
            data?.message ||
            `Request failed with status ${response.status}`
        );
    }

    return data;
}
