from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt= PromptTemplate(
    template='Generate 5 innteresting facts anout{topic}',
    input_variables=['topic']
)

model=GoogleGenerativeAI(model='gemini-1.5-flash')

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({'topic':'women'})

print(result)
chain.get_graph().print_ascii()
