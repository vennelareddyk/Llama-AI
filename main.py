import os
import ollama
import streamlit as st

MODEL = "llama3.2:1b"

st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖", layout="centered")
st.page_title = "Ollama Chatbot"
#Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"you are a helpful assistant, be concise. if you don't know then say - I don't know"}]
#show chat history
# for message in st.session_state.messages:
#     st.chat_message(message["role"],message["content"])
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
user_text = st.chat_input("Type your message...")

if user_text:
    # Add user message to memory + render it
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Call Ollama with full context memory
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            resp = ollama.chat(
                model=MODEL,
                messages=st.session_state.messages
            )
            assistant_text = resp["message"]["content"]
            st.markdown(assistant_text)

    # Save assistant response to memory
    st.session_state.messages.append({"role": "assistant", "content": assistant_text})

# Sidebar actions
with st.sidebar:
    st.subheader("Settings")
    st.write(f"Model: `{MODEL}`")

    if st.button("🧹 Clear chat"):
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant. Be clear and concise."}
        ]
        st.rerun()