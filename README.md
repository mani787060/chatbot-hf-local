# Local Chatbot with Hugging Face & LangChain

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Generative AI](https://img.shields.io/badge/Domain-Generative%20AI-purple)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Hugging Face](https://img.shields.io/badge/Model%20Hub-Hugging%20Face-yellow)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)

A beginner-friendly implementation of a locally loaded open-source Large Language Model (LLM) using **Hugging Face Transformers and LangChain**. This project explores how to load an instruction-tuned model, connect it to LangChain's chat interface, and generate responses through a simple Python script.

---

## 📌 Project Overview

This project demonstrates how to integrate a Hugging Face language model with LangChain using the `langchain-huggingface` package.

Instead of calling a hosted chat API, the implementation uses `HuggingFacePipeline.from_model_id()` to load a model through the local Transformers pipeline.

The selected model is:

**`meta-llama/Llama-3.1-8B-Instruct`**

After loading the model, the code wraps it with LangChain's `ChatHuggingFace` class and sends a prompt using the `invoke()` method.

The main purpose is to understand the fundamentals of local LLM integration and the hardware requirements involved in running larger open-source models.

## 🏗️ Project Architecture

The implementation follows this workflow:

```text
User Prompt
    |
    v
HuggingFacePipeline.from_model_id()
    |
    v
Local Hugging Face Transformers Pipeline
    |
    v
ChatHuggingFace Wrapper
    |
    v
model.invoke(prompt)
    |
    v
Generated Response
```

## 🛠️ Key Technical Implementations

### 1. Loading a Hugging Face Model Locally

The project uses:

```python
HuggingFacePipeline.from_model_id()
```

This method initializes a Hugging Face model through the Transformers pipeline interface.

The implementation specifies:

- **Model:** `meta-llama/Llama-3.1-8B-Instruct`
- **Task:** `text-generation`
- **Temperature:** `0.5`
- **Maximum new tokens:** `100`

The model is intended to run locally, so the available system memory and processing hardware directly affect whether it can be loaded successfully.

### 2. LangChain Chat Integration

The loaded pipeline is wrapped using:

```python
from langchain_huggingface import ChatHuggingFace

model = ChatHuggingFace(llm=llm)
```

`ChatHuggingFace` provides a chat-model interface around the Hugging Face language model, making it possible to interact with the model through LangChain.

### 3. Generating Responses with `invoke()`

The project uses LangChain's `invoke()` method to send a prompt and retrieve a generated response.

```python
result = model.invoke("Tell me the birthplace of Lord Ram")
print(result.content)
```

The generated response is accessed through the `content` attribute.

## 💻 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Hugging Face Transformers | Loading and running the language model |
| Hugging Face Hub | Accessing the model repository |
| LangChain | LLM orchestration |
| `langchain-huggingface` | Hugging Face integration with LangChain |
| PyTorch | Deep learning backend used by Transformers |

## 📂 Repository Structure

```text
chatbot-hf-local/
│
├── 5_chatmodel_hf_local.py
│   └── Loads the Llama model and generates a response
│
└── README.md
    └── Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mani787060/chatbot-hf-local.git

cd chatbot-hf-local
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install langchain-huggingface transformers torch accelerate huggingface_hub
```

The exact PyTorch installation command may depend on your operating system and whether you intend to use CPU or a supported GPU.

### 4. Configure Hugging Face Model Access

This project uses the Meta Llama 3.1 8B Instruct model.

Before downloading it:

1. Open the model page: [Meta Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).
2. Review and accept the model's license and access conditions, if required.
3. Authenticate with Hugging Face using the CLI:

```bash
hf auth login
```

Provide your Hugging Face access token when prompted.

Keep your access token private. Never commit it to GitHub or place it directly in your Python source code.

### 5. Run the Project

```bash
python 5_chatmodel_hf_local.py
```

The script attempts to load the model, generate a response to the sample prompt, and print the result.

**Important:** The first run may take time because the model weights need to be downloaded. Sufficient disk space, RAM, and compatible hardware are necessary.

## ⚙️ Hardware Considerations

The selected model contains approximately 8 billion parameters. Running it locally can require substantial memory.

The original experiment encountered hardware limitations and did not run successfully on the available system.

For this reason:

- A machine with limited RAM may fail to load the model.
- CPU inference can be slow.
- A compatible GPU with sufficient VRAM can improve inference performance.
- Quantization may reduce memory requirements, but it is not implemented in the current script.

The repository should therefore be treated as a learning experiment, not as a verified, fully working chatbot deployment.

## 📚 Concepts Learned

This project provides practical exposure to:

- Open-source Large Language Models (LLMs)
- Hugging Face model repositories
- Local model loading with Transformers
- LangChain Hugging Face integration
- `HuggingFacePipeline`
- `ChatHuggingFace`
- Text-generation pipelines
- Prompt-based inference using `invoke()`
- Hardware requirements for local LLM execution

## 🔮 Future Improvements

Possible improvements for future versions include:

- Experimenting with smaller instruction-tuned models.
- Implementing 4-bit or 8-bit quantization.
- Adding GPU-aware model configuration.
- Using `ChatPromptTemplate` for structured prompts.
- Supporting multi-turn conversations with message history.
- Implementing token streaming.
- Creating a simple Streamlit chatbot interface.
- Comparing local inference with hosted Hugging Face inference endpoints.

These are planned improvements, not features currently implemented.

## 🎯 Learning Objective

The objective of this project is to understand how open-source language models can be integrated with LangChain and executed locally using Hugging Face Transformers.

It also highlights an important practical consideration in Generative AI development: **choosing a model that matches the available hardware is just as important as choosing the model architecture.**

---

## 👨‍💻 Author

**Mani Ratan**

- GitHub: [@mani787060](https://github.com/mani787060)
- LinkedIn: [Mani Ratan](https://www.linkedin.com/in/mani-ratan-159963289/)
- Kaggle: [@mani787060](https://www.kaggle.com/mani787060)

If you find this repository useful for learning about Generative AI and LangChain, feel free to explore the code and share your feedback.

⭐ If you find this project helpful, consider giving the repository a star!
