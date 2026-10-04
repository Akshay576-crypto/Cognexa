import { apiRequest } from "./client";

export async function signupUser({
    full_name,
    email,
    password,
}) {
    return apiRequest("/api/v1/auth/signup", {
        method: "POST",
        body: {
            full_name,
            email,
            password,
        },
    });
}

export async function loginUser({
    email,
    password,
}) {
    const data = await apiRequest("/api/v1/auth/token", {
        method: "POST",
        form: true,
        body: {
            username: email,
            password,
        },
    });

    if (data?.access_token) {
        localStorage.setItem(
            "cognexa_access_token",
            data.access_token
        );
    }

    return data;
}

export function getAccessToken() {
    return localStorage.getItem(
        "cognexa_access_token"
    );
}

export function logoutUser() {
    localStorage.removeItem(
        "cognexa_access_token"
    );
}

