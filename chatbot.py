from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load the environment variables
load_dotenv()

#streamlit page configuration
st.set_page_config(
    page_title="💬 Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Generative AI Chatbot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat history on screen
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#initiate llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

#user input
user_prompt = st.chat_input("Ask chatbot anything...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response =llm.invoke(
        input = [{"role":"system", "content":"You are a helpful assistant."}, *st.session_state.chat_history]
    )

    assistant_response = response.content

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
