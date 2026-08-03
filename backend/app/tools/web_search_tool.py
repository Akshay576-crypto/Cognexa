from ddgs import DDGS
from langchain_core.tools import tool


@tool
def web_search_tool(query: str, max_results: int = 8) -> str:
    """
    Search the live web based on the user's research query.

    Returns relevant web results with title, snippet, source,
    URL, and publication date when available.
    """

    try:
        query = query.strip()

        if not query:
            return "Error: Search query cannot be empty."

        max_results = max(1, min(max_results, 20))

        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for item in search_results:
                results.append({
                    "title": item.get("title"),
                    "snippet": item.get("body"),
                    "url": item.get("href"),
                    "source": item.get("source"),
                    "published_at": item.get("date"),
                })

        if not results:
            return (
                f"No web results found for query: {query}"
            )

        output = {
            "tool": "web_search_tool",
            "query": query,
            "result_count": len(results),
            "results": results
        }

        import json

        return json.dumps(
            output,
            indent=2,
            ensure_ascii=False
        )

    except Exception as e:
        return (
            f"Web search failed for query "
            f"'{query}': {str(e)}"
        )