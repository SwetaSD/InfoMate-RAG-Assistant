import streamlit as st
from pathlib import Path

from embeddings import create_faiss_index
from qa_chain import build_qa_chain
from loader import load_documents

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# -----------------------------
# App UI
# -----------------------------
st.set_page_config(page_title="InfoMate – RAG Assistant", layout="wide")
st.title("📘 InfoMate – RAG Assistant")

# -----------------------------
# Configuration Sidebar
# -----------------------------
st.sidebar.header("⚙️ Advanced Settings")
st.sidebar.markdown("Adjust these parameters to balance between precision and deep context.")

chunk_size = st.sidebar.slider("Chunk Size (Characters)", min_value=200, max_value=2000, value=1000, step=100)
chunk_overlap = st.sidebar.slider("Chunk Overlap", min_value=0, max_value=500, value=150, step=50)
retriever_k = st.sidebar.slider("Retriever 'k' (Context Chunks)", min_value=1, max_value=10, value=5, step=1)

# -----------------------------
# FAISS index path
# -----------------------------
index_path = Path("faiss_index")

# -----------------------------
# File upload section
# -----------------------------
st.subheader("📂 Upload documents")

pdf_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

docx_files = st.file_uploader(
    "Upload Word documents",
    type=["docx"],
    accept_multiple_files=True
)

# -----------------------------
# Process documents
# -----------------------------
if st.button("🚀 Process Documents"):
    if not (pdf_files or docx_files):
        st.warning("Please upload at least one PDF, DOCX, or image file.")
    else:
        with st.spinner("Reading files and creating index..."):
            # Load text from documents
            texts = load_documents(pdf_files, docx_files)

            # Create FAISS index (PASSING THE SLIDER VARIABLES HERE)
            vectorstore = create_faiss_index(
                texts,
                index_path=str(index_path),
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

            # Build QA chain (PASSING THE SLIDER VARIABLE HERE)
            st.session_state.qa = build_qa_chain(vectorstore, k=retriever_k)

        st.success("✅ Documents processed and indexed successfully!")

# -----------------------------
# Load existing index (if any)
# -----------------------------
if "qa" not in st.session_state and index_path.exists():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.load_local(
        str(index_path),
        embeddings,
        allow_dangerous_deserialization=True
    )
    # Build QA chain (PASSING THE SLIDER VARIABLE HERE)
    st.session_state.qa = build_qa_chain(vectorstore, k=retriever_k)

# -----------------------------
# Question answering
# -----------------------------
st.subheader("💬 Ask a question")

query = st.text_input("Ask something from your uploaded documents")

if query:
    if "qa" not in st.session_state:
        st.warning("Please upload and process documents first.")
    else:
        response = st.session_state.qa.invoke({"question": query})
        st.write("### 📌 Answer")
        st.write(response)
