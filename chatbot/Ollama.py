#LANGCHAIN_API_KEY="lsv2_pt_0ff92976b29dddddddddddddddddd2db9ed59"
#OPENAI_API_KEY="sk-proj-1akat7mxpZpP2ddddddddddddddddddkF91s1"
#LANGCHAIN_PROJECT="Chatbot"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()



## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## creating chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistent. Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework

st.title("Langchain Demo with LLama3 AI API")
input_text=st.text_input("search the topic you want")

# Ollama LLM call
llm=Ollama(model="LLama3")
output_parser=StrOutputParser()

## chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

