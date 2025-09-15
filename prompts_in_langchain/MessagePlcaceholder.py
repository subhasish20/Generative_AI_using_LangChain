from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Initialize model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Past conversation (simulated chat history)
chat_history = [
    HumanMessage(content="I want to request a refund for my order 12345"),
    AIMessage(content="Your refund request for order 12345 has been initiated. You will receive it in 3-5 business days."),
]

# Prompt template with history + new query
template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Current query
query = "Where is my refund?"

# Build final prompt
final_prompt = template.invoke({"chat_history": chat_history, "query": query})

# Show final prompt
for msg in final_prompt:
    print(f"{msg.type.capitalize()}: {msg.content}")

print("\nLLM Response:\n")
response = model.invoke(final_prompt)
print(response.content)
