import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize GPT-4 model
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Streamlit UI Setup
st.header("Research Paper Summarizer")

# User input
selected_paper = st.selectbox("Select a Research Paper:", ["Attention Is All You Need", "Word2Vec", "BERT", "GPT-3"])
explanation_style = st.selectbox("Choose Explanation Style:", ["Simple", "Math Heavy", "Code Heavy"])
explanation_length = st.selectbox("Choose Explanation Length:", ["Short", "Medium", "Long"])

# Define the prompt template
template_string = """
Summarize the paper '{paper_input}' with the following style and length:
Explanation Style: {style_input}
Explanation Length: {length_input}
Provide relevant mathematical formulas, analogies, and code snippets if needed.
"""

research_prompt_template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template=template_string
)

# Handle button click to generate summary
if st.button("Summarize"):
    # Fill the template with user inputs
    final_prompt = research_prompt_template.invoke({
        "paper_input": selected_paper,
        "style_input": explanation_style,
        "length_input": explanation_length
    })

    # Get summary from GPT-4
    with st.spinner("Generating summary..."):
        result = model.invoke(final_prompt)

    # Display the summary
    st.write(result.content)
