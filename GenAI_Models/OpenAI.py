from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4o-2024-11-20')

result = llm.invoke("What is the capital of India")

print(result)