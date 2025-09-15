from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

# Declare the model (temperature=0 for deterministic responses)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Define the template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms what is {topic}.")
])

# Helper function to generate and run prompts
def generate_prompt(domain, topic):
    # Fill in placeholders
    final_prompt = chat_template.invoke({"domain": domain, "topic": topic})
    
    # Print the generated prompt
    print("Generated Prompt:")
    for msg in final_prompt:
        print(f"{msg.type.capitalize()}: {msg.content}")
    
    print("\nResponse from LLM:\n")
    
    # Call the model with the prompt
    response = llm.invoke(final_prompt)
    print(response.content)

    print("\n" + "="*40 + "\n")

# Examples
generate_prompt("cricket", "second innings")
generate_prompt("medical", "vaccination")
