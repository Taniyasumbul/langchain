from langchain_community.document_loaders import WebBaseLoader
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
    template="Write a summary for the following text-\n{text}",
    input_variables=['text']
)

url='https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TE-uis8pT64yYPTiKE7MrExMLEoEAGlACHA&q=saiyaara&oq=sai&gs_lcrp=EgZjaHJvbWUqCggBEC4YsQMYgAQyBggAEEUYOTIKCAEQLhixAxiABDIMCAIQIxgnGIAEGIoFMgoIAxAAGLEDGIAEMg0IBBAuGIMBGLEDGIAEMgoIBRAAGLEDGIAEMg0IBhAAGLEDGIAEGIoFMgoIBxAAGLEDGIAEMgoICBAuGLEDGIAEMgcICRAAGI8C0gEKMTYyNDlqMGoxNagCCLACAfEFH0d798E2BbfxBR9He_fBNgW3&sourceid=chrome&ie=UTF-8'
loader=WebBaseLoader(url)
docs=loader.load()
parser=StrOutputParser()
chain=prompt1|model|parser
print(chain.invoke({"question":'what is the topic','text':docs[0].page_content}))
