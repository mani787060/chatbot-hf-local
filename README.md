# Local Chatbot with Hugging Face & LangChain
[![Generative AI](https://img.shields.io/badge/Domain-Generative%20AI-blueviolet)](https://huggingface.co/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)](https://www.langchain.com/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/models)

## 🏗️ Project Overview
This repository demonstrates how to build a functional chatbot using open-source Large Language Models (LLMs). Instead of relying on closed-source APIs, this project utilizes the **Hugging Face** ecosystem. By leveraging LangChain's **`ChatHuggingFace`** wrapper, we transform raw text-completion models into sophisticated conversational agents capable of maintaining message history and following complex instructions.

---

## 🛠️ Key Technical Implementations

### 1. The `ChatHuggingFace` Bridge
Standard models on Hugging Face often require manual prompt engineering. This implementation uses the `ChatHuggingFace` wrapper, which:
*   **Standardizes Input:** Converts LangChain `BaseMessage` objects (System, Human, AI) into the specific format required by the model.
*   **Prompt Templating:** Automatically applies the correct chat templates (like Llama-3 or Mistral formats) to ensure the model responds as a chatbot rather than a text-completer.

### 2. Model Ingestion
* **HuggingFaceHub Integration:** Accessing state-of-the-art models via the Inference API for rapid prototyping.
* **Local Pipeline Readiness:** Providing the foundation to switch to local execution using `transformers` for total data privacy and zero-latency inference.

### 3. Conversational Architecture
* **Message Roles:** Clearly defining the `SystemMessage` to set the chatbot's personality and the `HumanMessage` for user input.
* **Streaming & Response Handling:** Managing the output stream to provide a seamless interaction experience.

---

## 💻 Tech Stack
* **Language:** Python 3.9+
* **Orchestration:** LangChain (`langchain-huggingface`)
* **Model Provider:** Hugging Face Hub
* **Environment:** `python-dotenv`, Jupyter Notebook

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/local-chatbot-huggingface-langchain.git](https://github.com/your-username/local-chatbot-huggingface-langchain.git)

2. **Install Dependencies:**
   ```bash
   pip install -U langchain-huggingface huggingface_hub python-dotenv

3. **Configure Access:**
   Create a `.env` file and add your Hugging Face Token:
   ```text
   HUGGINGFACEHUB_API_TOKEN=your_token_here
    
4. **Run the Chatbot:**
   Open chatbot_hf_local.ipynb and start interacting with the model.
