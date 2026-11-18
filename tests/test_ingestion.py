
from app.ingestion.chunker import split_documents
from app.ingestion.cleaner import clean_documents
from app.ingestion.loader import load_document

file_path = "data/uploads/sample.pdf"

documents = load_document(file_path)
cleaned = clean_documents(documents)
chunks = split_documents(cleaned)

print("\n===== INGESTION TEST =====")
print("Document:", file_path)
print("Pages / sections:", len(documents))
print("Cleaned sections:", len(cleaned))
print("Total chunks:", len(chunks))

for chunk in chunks[:3]:
    print("\n--- CHUNK ---")
    print("Metadata:", chunk.metadata)
    print(chunk.page_content[:300])

print("\nINGESTION TEST PASSED")
