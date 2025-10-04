from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

# ✅ Corrected: using keyword argument
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chat_history=[
    SystemMessage(content='you are a helpful AI assistent')
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI:", result.content)

    print(chat_history)
