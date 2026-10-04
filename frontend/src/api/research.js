import { apiRequest } from "./client";
import { getAccessToken } from "./auth";

export async function researchQuestion(
    question,
    documentId = null,
    topK = 5
) {
    return apiRequest("/api/v1/research/", {
        method: "POST",
        token: getAccessToken(),
        body: {
            question,
            document_id: documentId,
            top_k: topK,
        },
    });
}