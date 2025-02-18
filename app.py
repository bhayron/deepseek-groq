from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key="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")

st.set_page_config(page_title="Chat Deep", layout="centered")
st.title("Teste com DeepSeek")

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
    messages.append(("ai", response))
    
    chat = st.chat_message("ai")
    chat.markdown(response)