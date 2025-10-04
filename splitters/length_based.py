from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('BAJHLIP23020V012223.pdf')
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''

)
docs=loader.load()
result = splitter.split_text(docs[0].page_content)

print(result)