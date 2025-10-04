from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)