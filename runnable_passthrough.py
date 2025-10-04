from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic'])

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)

parser = StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke-{text}',
    input_variables=['text']
)
joke_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'Expalanation':RunnableSequence(prompt2,model,parser)}
    )
final_chain=RunnableSequence(joke_chain,parallel_chain)
print(final_chain.invoke({'topic': 'AI'}))