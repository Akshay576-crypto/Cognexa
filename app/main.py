from pathlib import Path

import streamlit as st

from app.ingestion.chunker import split_documents
from app.ingestion.cleaner import clean_documents
from app.ingestion.loader import load_document
from app.pipeline.rag_chain import ask_question
from app.vectorstore.qdrant_store import (
    reset_collection,
    store_documents,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPLOAD_DIR = PROJECT_ROOT / "data" / "uploads"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

st.set_page_config(
    page_title="Local RAG Assistant",
    page_icon="📚",
    layout="centered",
)

st.title("📚 Local RAG Assistant")
st.caption("Upload a document and ask questions using AI.")

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx", "txt"],
)

if st.button("Process Document", type="primary"):

    if uploaded_file is None:
        st.warning("Please upload a document first.")

    else:
        file_path = UPLOAD_DIR / Path(uploaded_file.name).name
        file_path.write_bytes(uploaded_file.getvalue())

        try:
            with st.spinner("Processing your document..."):
                documents = load_document(str(file_path))
                cleaned = clean_documents(documents)
                chunks = split_documents(cleaned)

                reset_collection()
                store_documents(chunks)

                st.session_state["indexed_document"] = file_path.name
                st.session_state["chat_history"] = []

            st.success(
                f"Successfully indexed {len(chunks)} chunks!"
            )

        # Streamlit UI boundary: surface errors from document and service layers.
        except Exception as error:  # noqa: BLE001
            st.error(f"Document processing failed: {error}")


if st.session_state.get("indexed_document"):

    st.divider()

    st.success(
        f"Active document: {st.session_state['indexed_document']}"
    )

    st.subheader("Ask your document")

    for message in st.session_state.get("chat_history", []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message.get("sources"):
                st.caption("Sources:")
                for source in message["sources"]:
                    st.write(
                        f"- {source['source']} — Page {source['page']}"
                    )

    question = st.chat_input("Ask a question about your document...")

    if question:

        st.session_state["chat_history"].append({
            "role": "user",
            "content": question,
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"), st.spinner(
            "Searching and generating an answer..."
        ):

            try:
                result = ask_question(question, top_k=4)

                st.markdown(result["answer"])

                if result["sources"]:
                    st.caption("Sources:")
                    for source in result["sources"]:
                        st.write(
                            f"- {source['source']} — Page {source['page']}"
                        )

                st.session_state["chat_history"].append({
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"],
                })

            # Streamlit UI boundary: surface retrieval and generation failures.
            except Exception as error:  # noqa: BLE001
                st.error(f"Question processing failed: {error}")