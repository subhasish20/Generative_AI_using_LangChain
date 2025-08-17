from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
while True:
    user_inupt  = input("Enter your expression :")
    result = model.invoke(user_inupt)

    print(result.content)       