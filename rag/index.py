from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path =  Path(__file__).parent / "Teach Yourself C++ By Herbert Schildt.pdf"

#Load This File into python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

print(docs[1])
