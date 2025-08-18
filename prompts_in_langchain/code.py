from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print(api_token)
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm=llm)

result = model.invoke('What is the capital of India?')
print(result.content)