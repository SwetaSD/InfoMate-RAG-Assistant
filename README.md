# 📘 InfoMate – Document-Based RAG Assistant

InfoMate is a **local Retrieval-Augmented Generation (RAG) application** that allows users to upload documents and ask questions grounded strictly in their content.  
It is designed for **accuracy, reliability, and offline use**, avoiding cloud APIs and external LLM services.

## ✨ Features

-  Upload **PDF** and **Word (DOCX)** documents  
-  Semantic search using **FAISS vector database**  
-  Local embeddings via **Ollama (`nomic-embed-text`)**  
-  Local LLM inference using **`phi3:mini`**  
-  Multi-document understanding  
-  Chunking-based retrieval for large documents  
-  No hallucinations — answers are grounded in document context  
-  Runs completely **offline**

---

## 🏗️ Architecture Overview

Documents (PDF/DOCX) -> Text Extraction -> Text Chunking -> Vector Embeddings (Ollama) -> FAISS Vector Store -> Retriever (Top-K chunks) -> Local LLM (phi3:mini) -> Grounded Answer

---

## 🛠️ Tech Stack

| Component      | Technology |
|---------------|------------|
| Frontend      | Streamlit |
| Embeddings    | Ollama (`nomic-embed-text`) |
| LLM           | Ollama (`phi3:mini`) |
| Vector DB     | FAISS |
| Text Parsing  | PyPDF2, python-docx |
| Framework     | LangChain (community + core) |

---

## 🚀 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SwetaSD/InfoMate-RAG-Assistant.git
cd InfoMate
```

### 2️⃣ Create a virtual environment
```bash
python -m venv rag_env
rag_env\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧠 Ollama Setup 
Install Ollama from:
👉 [https://ollama.com](https://ollama.com)

### Pull the Required Models
```bash
ollama pull nomic-embed-text
ollama pull phi3:mini
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

---

## 📌 Usage
1. Upload one or more PDF or DOCX files
2. Click Process Documents
3. Ask questions about the uploaded content
4. Receive answers grounded strictly in the documents 

---

## 🧪 Limitations
1. Scanned PDFs and images are not supported (OCR intentionally excluded)
2. Performance depends on local hardware
3. Large documents may take time during indexing

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests.  
All contributions are welcome!






