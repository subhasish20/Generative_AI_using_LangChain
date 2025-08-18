from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

st.header("LLM topic summarizer")

topic_name = st.selectbox("Select the topic name",['Lang_chain_components','Lang_chain_models','RAG','Vector Store'])
output_style = st.selectbox("Select the text outpu type ",['Beginner-Fiendly','Technical','Code-Oriented','Mathematical'])
length = st.selectbox("Select your Explanation Length",['Short Type (1-2 paragraphs)',"Medium (3-5 paragraph)","long type (6-8 paragraph)"])

# declaring the template for description
template = PromptTemplate(
    template="""
    please summarize the reasearch paper having title title {topic_name} in langchain with the following specification :
    explanation style : {output_style}
    explanation length : {length}""",
    input_variables=['topic_name','output_style','length'],
    validate_template=True # if there is any parameter is misssing then it will generate an error or if any extra parameter is given to
)

#place holder
prompt = template.invoke({
    'topic_name':topic_name,
    'output_style':output_style,
    'length' : length
})


if st.button("Submit"):
    result = model.invoke(prompt)
    st.write(result.content)