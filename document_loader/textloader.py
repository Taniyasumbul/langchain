from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
    
)
prompt1=PromptTemplate(
    template="Write a summary for the following poem-\n{poem}",
    input_variables=['poem']
)
parser=StrOutputParser()
loader=TextLoader('text.txt',encoding="utf-8")

docs=loader.load()


chain=prompt1|model|parser
print(chain.invoke({'poem':docs[0].page_content}))



