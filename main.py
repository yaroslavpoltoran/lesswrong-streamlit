import logging
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

import config as cfg
from utils import get_response_from_query

load_dotenv()
logging.basicConfig(level=logging.INFO)

embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings)
logging.info("Loaded FAISS index")


st.header(
    "Hello, I am a bot, who read all the publications of Eliezer Yudkowsky "
    "on his [LessWrong](https://www.lesswrong.com/) website "
    "and knows all the answers to your questions about his work"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    logging.info(f"User input: {prompt}")

    response = get_response_from_query(
        db=db, query=prompt, model=cfg.MODEL, n_dosc=cfg.N_DOSC, n_urls=cfg.N_URLS
    )

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    logging.info(f"Assistant response: \n{response[:200]}")
