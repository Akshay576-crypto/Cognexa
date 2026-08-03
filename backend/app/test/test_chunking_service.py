from app.services.chunking_service import ChunkingService


def test_count_tokens():
    """
    Test the HAC token counting function.
    """

    service = ChunkingService()

    test_cases = [
        "",
        "Hello",
        "Hello World",
        "Artificial Intelligence is transforming industries.",
        "Machine Learning is a subset of Artificial Intelligence.",
        """
        Artificial Intelligence

        Machine Learning

        Deep Learning
        """
    ]

    print("=" * 60)
    print("HAC TOKEN COUNT TEST")
    print("=" * 60)

    for index, text in enumerate(test_cases, start=1):
        tokens = service._count_tokens(text)

        print(f"\nTest Case {index}")
        print("-" * 40)
        print(f"Input : {repr(text)}")
        print(f"Estimated Tokens : {tokens}")

    print("\n")
    print("=" * 60)
    print("All Token Count Tests Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    test_count_tokens()