🛡️ Privacy-First Medical Assistant
A secure, local-first AI framework for clinical inquiries.

🚀 Overview
Privacy-First Medical Assistant is an AI-powered chat interface designed to demonstrate how Large Language Models (LLMs) can be deployed in sensitive environments like healthcare. Unlike cloud-based solutions, this assistant runs entirely on your local hardware, ensuring that medical queries and data remain private and secure.

💡 Current Status: v1.0 (Interactive Chat)
The current build serves as a secure conversational agent. It allows users to:

Interact with local LLMs (Llama 3.2, Mistral, etc.) via a clean web UI.

Discuss general medical concepts and research without data egress.

Experience zero-latency issues associated with cloud APIs.

✨ Features
100% Offline Inference: Powered by Ollama, ensuring no data ever leaves your machine.

Low-Resource Optimization: Configured to run on consumer-grade laptops (8GB+ RAM).

Medical-Grade Guardrails: Custom system prompts to encourage a professional, clinical tone.

Streamlit Interface: A fast, responsive, and minimalist chat UI.

🛠️ Tech Stack
LLM Engine: Ollama

Orchestration: LangChain

Interface: Streamlit

Language: Python 3.10+

⚙️ Installation
1. Install the LLM Engine
Download and install Ollama from ollama.com. Once installed, open your terminal and run:

Bash
ollama pull llama3.2

2. Setup the Repository

Bash
git clone https://github.com/prakyathshetty25/Privacy-First-Medical-Assistant.git
cd Privacy-First-Medical-Assistant

# Create and activate virtual environment

python -m venv venv
source venv/bin/activate 
# Windows: venv\Scripts\activate

# Install dependencies

pip install streamlit langchain langchain_community ollama

3. Run the App
Bash
streamlit run app.py

🏗️ Technical Roadmap: Phase 2 (Under Development)
We are currently transitioning this project into a RAG (Retrieval-Augmented Generation) system. This will allow the assistant to "read" and analyze specific medical documents (PDFs/Research Papers) uploaded by the user.

Upcoming Features:

[ ] PDF Ingestion Pipeline: Support for uploading medical records or journals.

[ ] Local Vector Store: Implementing FAISS or ChromaDB for in-memory document search.

[ ] Contextual Retrieval: The AI will base its answers only on the facts found within the uploaded files.

[ ] Source Citation: The assistant will cite the exact page and paragraph from the PDF used to generate its response.

🤝 Contributing
I am actively seeking feedback on clinical accuracy and local optimization. If you'd like to help build the RAG pipeline or improve the UI, please open an issue or submit a pull request!
