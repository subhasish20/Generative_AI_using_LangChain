from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


# by changing the temperature value the result will not be same at all time
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=1.5) 
result = model.invoke('What is the capital of India')

print(result.content)