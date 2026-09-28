from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader = PyPDFLoader("check2.pdf")
documents = loader.load()
print("this is the first page data:")
print(documents[0].page_content)
print("this is the second page data:")
print(documents[1].page_content)
