import streamlit as st
from langchain_ollama import OllamaLLM

# 1. Setup the Page Title
st.set_page_config(page_title="Privacy-First Medical Assistant", page_icon="🛡️")
st.title("🛡️ Privacy-First Medical Assistant")
st.write("All data stays on your machine. No cloud, no leaks.")

# --- DEPLOYMENT FIX: SIDEBAR FOR NGROK ---
with st.sidebar:
    st.header("Connection Settings")
    # This allows you to paste the link ngrok gives you (e.g., https://xxxx.ngrok-free.app)
    ngrok_url = st.text_input("Enter Ngrok URL", placeholder="https://your-url.ngrok-free.app")
    st.info("Run 'ngrok http 11434' on your local machine to get this URL.")

# 2. Initialize the Local Model
# We only initialize if the URL is provided
if ngrok_url:
    llm = OllamaLLM(model="llama3.2:1b", base_url=ngrok_url)

    # 3. Create the Chat Interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 4. Generation Logic with Streaming
    if prompt := st.chat_input("Ask a medical question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Use st.write_stream to show words as they are generated
            try:
                stream = llm.stream(prompt)
                response = st.write_stream(stream) 
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Connection Error: {e}")
                st.write("Make sure your local Ollama is running and Ngrok is active.")
else:
    st.warning("👈 Please enter your Ngrok URL in the sidebar to start.")
