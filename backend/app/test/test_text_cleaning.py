#from app.services.text_cleaning_service import TextCleaningService
from app.services.text_cleaning_service import TextCleaningService

def main():
    cleaner = TextCleaningService()

    raw_text = """
    Hello



            World!



    AI        is        transforming      industries.


    This\tis\ta\ttest.

    """

    print("=" * 60)
    print("RAW TEXT")
    print("=" * 60)
    print(raw_text)

    cleaned_text = cleaner.clean_text(raw_text)

    print("\n" + "=" * 60)
    print("CLEANED TEXT")
    print("=" * 60)
    print(cleaned_text)


if __name__ == "__main__":
    main()