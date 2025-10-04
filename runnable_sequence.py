from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
import os

# Load API key from .env
load_dotenv()

# Ensure your .env has: GOOGLE_API_KEY=your_key_here
api_key = os.getenv("GOOGLE_API_KEY")

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

# Pass model and API key
model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)

parser = StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke-{text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt1, model,parser, prompt2,model,parser)

print(chain.invoke({'topic': 'AI'}))
