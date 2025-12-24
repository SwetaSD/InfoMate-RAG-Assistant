from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_faiss_index(texts, index_path=None):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # 🔹 Text splitter (VERY IMPORTANT)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    documents = []

    for i, text in enumerate(texts):
        chunks = splitter.split_text(text)

        for j, chunk in enumerate(chunks):
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={"source": f"doc_{i}_chunk_{j}"}
                )
            )

    # Create FAISS index from chunks
    vector_store = FAISS.from_documents(documents, embeddings)

    if index_path:
        vector_store.save_local(index_path)

    return vector_store
