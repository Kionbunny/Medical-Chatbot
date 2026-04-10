# 🏥 Medical Chatbot using RAG (LLMs + LangChain + Pinecone + Flask)

An end-to-end Retrieval-Augmented Generation (RAG) chatbot that answers medical queries using custom medical documents.
The system uses semantic search over vector embeddings stored in Pinecone and generates context-aware responses using LLMs.

---

## 🚀 Features

* 🔍 Semantic search using Pinecone
* 🧠 LLM-powered responses (OpenAI / Groq / HuggingFace)
* 📄 PDF ingestion and processing
* 💬 Interactive chat UI using Flask
* 🐳 Docker support for containerized deployment

---

## 🧠 Tech Stack

* Python
* LangChain
* Flask
* Pinecone (Vector Database)
* HuggingFace / OpenAI / Groq (LLMs)
* Docker

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kionbunny/Medical-Chatbot.git
cd Medical-Chatbot
```

---

### 2️⃣ Create Conda Environment

```bash
conda create -n chat python=3.10 -y
conda activate chat
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

Create a `.env` file in the root directory and add:

```env
PINECONE_API_KEY=your_key
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
```

---

### 5️⃣ Store Embeddings in Pinecone

```bash
python store_index.py
```

---

### 6️⃣ Run the Application

```bash
python app.py
```

👉 Open in browser: http://localhost:8080

---

## 🐳 Docker Setup

### 1️⃣ Build Docker Image

```bash
docker build -t medical-chatbot .
```

---

### 2️⃣ Run Docker Container

```bash
docker run -p 8080:8080 --env-file .env medical-chatbot
```

👉 Open in browser: http://localhost:8080

---

## 🚀 Deployment Options

* **Docker (Recommended)** → Run locally or on any cloud (AWS, Azure, GCP)
* **AWS** → EC2 (compute) + ECR (container registry)
* **Azure** → ACR (container registry) + App Service / VM

---

## 🔐 Environment Variables

| Variable         | Description      |
| ---------------- | ---------------- |
| PINECONE_API_KEY | Pinecone API Key |
| OPENAI_API_KEY   | OpenAI API Key   |
| GROQ_API_KEY     | Groq API Key     |

---

## 📌 Important Notes

* Do NOT commit `.env` file (contains secrets)
* Use `.env.example` for sharing configuration
* Rotate API keys if exposed
* Ensure Docker is installed before running containers

---

## 🚀 Future Improvements

* Streaming responses
* Chat memory (conversation history)
* Source citations in UI
* CI/CD pipeline using GitHub Actions
* Kubernetes deployment

---

## 💡 Project Overview

This project demonstrates a full-stack Generative AI application using Retrieval-Augmented Generation (RAG).
It enables context-aware question answering over domain-specific medical documents.

---

## 👨‍💻 Author

Ajay (NIT Warangal)
