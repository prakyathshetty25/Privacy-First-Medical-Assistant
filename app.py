import streamlit as st
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3.2")

# 1. Setup the Page Title
st.title("🛡️ Privacy-First Medical Assistant")
st.write("All data stays on this machine. No cloud, no leaks.")

# 2. Initialize the Local Model
llm = OllamaLLM(model="llama3.2:1b")

# 3. Create the Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Replace your current Step 4 generation logic with this:
if prompt := st.chat_input("Ask a medical question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Use st.write_stream to show words as they are generated
        stream = llm.stream(prompt)
        response = st.write_stream(stream) 
        st.session_state.messages.append({"role": "assistant", "content": response})