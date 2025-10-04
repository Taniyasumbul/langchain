from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",       # or "gemini-1.5-flash-8b"
    google_api_key=api_key
)
result = llm.invoke("Which is the biggest state of india")
print(result.content)

