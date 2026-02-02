# 🤖 Ollama Chatbot (Streamlit + LLaMA 3.2)

A lightweight conversational AI chatbot built using **Streamlit** and **Ollama**, powered by the **LLaMA 3.2 (1B)** model.  
This app supports **chat memory**, allowing the model to maintain conversational context across messages.

---

## ✨ Features

- 💬 Interactive chat UI using Streamlit
- 🧠 Context-aware conversations (session-based memory)
- ⚡ Runs locally using Ollama (no cloud dependency)
- 🔁 Clear chat option to reset conversation
- 🦙 Uses `llama3.2:1b` model for fast responses

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Ollama**
- **LLaMA 3.2 (1B)**

---

## 📦 Prerequisites

Make sure you have the following installed:

1. **Python 3.9+**
2. **Ollama**  
   Install from: https://ollama.com

3. Pull the LLaMA model:
   ```bash
   ollama pull llama3.2:1b
**-----------------------------------------------------------------------------------**
🚀 Installation & Setup
**-----------------------------------------------------------------------------------**

1️⃣ Clone the Repository
git clone https://github.com/vennelareddyk/Llama-AI
cd Llama-AI

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py

Once started, open your browser at:

http://localhost:8501

**------------------------🧠 How It Works------------------------------**

Chat history is stored in st.session_state.messages

Entire conversation is sent to Ollama on each prompt

System prompt ensures concise responses

Sidebar allows resetting chat memory
