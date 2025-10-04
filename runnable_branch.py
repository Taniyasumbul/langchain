from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch,RunnableLambda
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

prompt1=PromptTemplate(
template='write a detail report{topic}',
input_variables=['topic']
)

prompt2=PromptTemplate(
    template='summarize the following text\n{text}',
    input_variables=['text']
)

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)


parser=StrOutputParser()

report_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split()) < 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)


final_chain=RunnableSequence(report_chain,branch_chain)


print(final_chain.invoke({'topic':'ai vs ml'}))



