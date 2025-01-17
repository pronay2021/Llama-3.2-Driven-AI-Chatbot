from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", ""),
        ("user", "Question:{question}")
    ]
)

## Streamlit Framework
st.header("Llama 3.2-Driven AI Chatbot")

input_text = st.text_input("Input your text")

#Enter Button
if st.button("Enter"):
    if input_text.strip():  # Ensuring input is not empty
        # Ollama LLama3.2 LLM
        llm = Ollama(model="llama3.2:1b")
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        
        # Displaying Output
        st.write(chain.invoke({"question": input_text}))
    else:
        st.warning("Please enter a question before clicking Enter.")
