import os
from apikey import apikey
import pypandoc
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredEPubLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import YoutubeLoader

os.environ['OPENAI_API_KEY'] = apikey
#Reading
embeddings = OpenAIEmbeddings()
epub_path = "prose_fiction.epub"
def create_transcript() -> FAISS:
    #loads youtube vid
    loader = UnstructuredEPubLoader(epub_path)
    transcript = loader.load()
    #splits into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=100)
    texts = text_splitter.split_documents(transcript)
    docsearch = FAISS.from_documents(texts, embeddings)
    #spits out passage
    st.write(texts[13].page_content)
    return texts[13].page_content
def get_questions(book:str):
    title_template = PromptTemplate(
        input_variables=["book"],
        template="You are a machine that makes reading section ACT problems. Using the text from {book}, create 10 multiple choice questions to test reading comprehesion similar to what would be on the ACT ")
    llm = OpenAI(temperature=0.5)
    title_chain = LLMChain(llm=llm, prompt=title_template)
    response = title_chain.run({"book": book})
    st.write(response)