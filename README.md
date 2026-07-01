# 🏢 EnterpriseIQ – Agentic AI Knowledge Worker for Enterprises

EnterpriseIQ is an AI-powered Enterprise Knowledge Management System that enables organizations to upload internal documents, index them using semantic embeddings, and ask natural language questions to retrieve accurate, source-backed answers.

The system uses Retrieval-Augmented Generation (RAG) to search enterprise documents and generate responses with source citations, making knowledge retrieval faster, reliable, and explainable.

---

# 🚀 Features

## 📄 Document Management
- Upload PDF and DOCX documents
- Automatic text extraction
- Document chunking
- Store document metadata in MongoDB
- View uploaded documents
- View individual document details
- Delete uploaded documents

---

## 🤖 AI-Powered Knowledge Retrieval

- Semantic search using Sentence Transformers
- Vector storage using ChromaDB
- Retrieval-Augmented Generation (RAG)
- Groq LLM integration
- Context-aware question answering
- Source citations for every answer

Example:

Question:
> What programming languages does Nikhitha know?

Answer:
> Python, Java and C.

Sources:
- Resume.docx (Chunk 0)

---

## 💬 Chat History

- Save every conversation
- Store questions and answers
- Save source citations
- Retrieve previous conversations

---

# 🛠 Tech Stack

## Backend
- FastAPI
- Python

## AI / Machine Learning
- Sentence Transformers
- all-MiniLM-L6-v2
- Groq API
- Retrieval-Augmented Generation (RAG)

## Databases
- MongoDB
- ChromaDB (Vector Database)

## Libraries
- PyMuPDF
- LangChain Text Splitters
- Hugging Face Transformers
- Sentence Transformers
- Uvicorn

---

# 📂 Project Structure

```
EnterpriseIQ/
│
├── backend/
│
├── api/
│   ├── upload.py
│   ├── chat.py
│   ├── search.py
│   ├── documents.py
│   └── history.py
│
├── services/
│   ├── pdf_service.py
│   ├── chunk_service.py
│   ├── embedding_service.py
│   ├── vector_service.py
│   ├── search_service.py
│   ├── rag_service.py
│   └── history_service.py
│
├── models/
│   ├── document.py
│   └── chat.py
│
├── database/
│   └── mongodb.py
│
├── config/
│   └── settings.py
│
├── uploads/
├── vector_db/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ System Architecture

```
               Upload Document
                      │
                      ▼
             Text Extraction
                      │
                      ▼
               Text Chunking
                      │
                      ▼
          Sentence Embeddings
                      │
                      ▼
                 ChromaDB
                      │
                      ▼
            Semantic Retrieval
                      │
                      ▼
                Groq LLM
                      │
                      ▼
            AI Generated Answer
                      │
                      ▼
             Source Citations
                      │
                      ▼
             Chat History Storage
```

---

# 🔄 Workflow

1. Upload enterprise documents
2. Extract text from documents
3. Split text into semantic chunks
4. Generate embeddings
5. Store embeddings in ChromaDB
6. Store metadata in MongoDB
7. Ask questions in natural language
8. Retrieve relevant document chunks
9. Generate AI response using Groq
10. Display source citations
11. Save conversation history

---

# 📌 API Endpoints

## Upload

```
POST /upload
```

Upload a PDF or DOCX document.

---

## Chat

```
POST /chat
```

Ask questions about uploaded documents.

---

## Search

```
POST /search
```

Semantic search over uploaded documents.

---

## Documents

```
GET /documents
```

List all uploaded documents.

```
GET /documents/{id}
```

Get document details.

```
DELETE /documents/{id}
```

Delete a document.

---

## Chat History

```
GET /history
```

Retrieve chat history.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Nikhitha25135/EnterpriseIQ.git
```

Move into the project

```bash
cd EnterpriseIQ/backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m uvicorn app:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend folder.

```
GROQ_API_KEY=YOUR_GROQ_API_KEY

MODEL_NAME=llama-3.3-70b-versatile

MONGO_URI=mongodb://localhost:27017/
```

---

# 📈 Current Progress

✅ FastAPI Backend

✅ PDF/DOCX Upload

✅ Text Extraction

✅ Chunking

✅ Embedding Generation

✅ ChromaDB Integration

✅ MongoDB Integration

✅ Semantic Search

✅ Retrieval-Augmented Generation (RAG)

✅ Groq Integration

✅ Source Citation

✅ Document Management APIs

✅ Chat History

⬜ Authentication

⬜ React Frontend

⬜ Multi-Agent AI

⬜ Deployment

---

# 🚀 Future Enhancements

- JWT Authentication
- Role-Based Access Control
- React Dashboard
- Multi-Agent AI Workflow
- Conversation Memory
- Multi-document Reasoning
- OCR Support
- Enterprise Analytics Dashboard
- Cloud Deployment

---

# 👩‍💻 Author

**Nikhitha Budidha Goud**

B.Tech – Computer Science & Machine Learning

Machine Learning | Generative AI | Computer Vision | Full Stack AI Development

GitHub:
https://github.com/Nikhitha25135

LinkedIn:
https://www.linkedin.com/in/nikhitha-budidha-239221368/

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.
