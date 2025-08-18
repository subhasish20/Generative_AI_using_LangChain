from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.5)


load_dotenv()

st.header("Reasearch Tool")

user_unput = st.text_input("Enter your prompt")

if st.button("Submit"):
    result = llm.invoke(user_unput)
    st.write(result.content)