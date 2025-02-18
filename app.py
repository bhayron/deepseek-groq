import re
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key="sua_api_key")

st.set_page_config(page_title="Chat Deep", layout="centered")

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("DeepSeek do Bhayron")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
    
messages = st.session_state["messages"]
for type, content in messages:
    chat = st.chat_message(type)
    chat.markdown(content)

in_message = st.chat_input("Envie sua dúvida")
if in_message:
    messages.append(("human", in_message))
    chat = st.chat_message("human")
    chat.markdown(in_message)
    
    response = llm.invoke(messages).content

    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

    messages.append(("ai", response))
    
    chat = st.chat_message("ai")
    chat.markdown(response)
