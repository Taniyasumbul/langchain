from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("BAJHLIP23020V012223.pdf")
docs=loader.load()
print(docs)
print(docs[0].page_content)
print(docs[1].metadata)