from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("HUGGING_FACE_API_TOKEIN")
print(api_token)

llm = HuggingFaceEndpoint(
    repo_id='janhq/Jan-v1-4B',
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of india ??")

print(result.content)