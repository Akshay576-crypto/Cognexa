import { apiRequest } from "./client";
import { getAccessToken } from "./auth";

export async function askCognexa({
    question,
    context = "User is interacting with Cognexa Intelligence.",
    sources = "",
}) {
    const token = getAccessToken();

    if (!token) {
        throw new Error(
            "Authentication required. Please log in."
        );
    }

    return apiRequest("/api/v1/consulting/", {
        method: "POST",
        token,
        body: {
            question,
            context,
            sources,
        },
    });
}
