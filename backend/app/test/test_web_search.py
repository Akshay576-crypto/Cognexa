from app.tools.web_search_tool import web_search_tool


def main():
    query = (
        "Indian electric vehicle market growth "
        "2025 latest"
    )

    result = web_search_tool.invoke({
        "query": query,
        "max_results": 8
    })

    print("\n" + "=" * 80)
    print("COGNEXA USER-SPECIFIC WEB SEARCH TEST")
    print("=" * 80)
    print(result)
    print("=" * 80)


if __name__ == "__main__":
    main()