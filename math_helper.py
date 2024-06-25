import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey
#Math
def generate_math_problems(subject_type, topic_type):
    title_template = PromptTemplate(
        input_variables=["topic_type","subject_type"],
        template="Write me three ACT style {subject_type} problems about {topic_type} make it a multiple choice question, include nothing but the question and the multiple answers and Format the question to have the answers separated by lines"
    )

    llm = OpenAI(temperature=0.5)
    title_chain = LLMChain(llm=llm, prompt=title_template)
    response = title_chain.run({"topic_type": topic_type,"subject_type": subject_type})
    st.write(response)



def generate_reading_problems(subject_type, topic_type):
    if topic_type == "Prose Fiction":
        title_template = PromptTemplate(
         input_variables=["topic_type","subject_type"],
            template="Write me an intermediate reading-level story with themes about one of these topics: diversity, family relationships, childhood memory. This must be 800 words"
            )
        
    llm = OpenAI(temperature=0.5)
    title_chain = LLMChain(llm=llm, prompt=title_template)
    response = title_chain.run({"topic_type": topic_type,"subject_type": subject_type})
    st.write(response)
