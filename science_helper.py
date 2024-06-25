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

## conflicting viewpoints
def generate_conflicting_viewpoints(topic_type):
    title_template = PromptTemplate(
        input_variables=["topic_type","subject_type"],
        template="You are in charge of writing the conflicting viewpoints science passage for every ACT test" +
        " Develop two passages that present independent viewpoints on any chosen scientific topic. Each passage should advocate for a different hypothesis or theory, supported by unique scientific evidence and principles. The first passage should articulate one scientific perspective, using relevant data and research to substantiate its claims. The second passage should endorse an alternative scientific perspective, also supported by distinct evidence and reasoning. Each passage should be about 250 words, crafted to stand alone without directly referencing or contrasting the other viewpoint. The goal is to help students understand, analyze, and compare these alternative viewpoints or hypotheses independently. Ensure that the language and scientific concepts are appropriate for high school students preparing for the ACT test, focusing on enhancing their critical thinking and analytical skills. Do not write a conclusion after the passages."
    )
    llm = OpenAI(temperature=1.0,max_tokens=3800)
    title_chain = LLMChain(llm=llm, prompt=title_template)
    response = title_chain.run({"topic_type": topic_type})
    st.write(response)
    return response
def generate_questions(text: str):
    title_template = PromptTemplate(
        input_variables=["text"],
        template="Generate a set of 10 multiple-choice questions based on two independent passages that present differing scientific viewpoints on a selected topic. Each question should be crafted to evaluate the student’s understanding and analysis of the viewpoints presented: One question should identify the major point of difference between the two viewpoints.Include questions that ask students to identify specific arguments or evidence used by each scientist.Create questions that require comparison of the scientific merits or drawbacks of each viewpoint without implying direct opposition within the passages.Develop questions that test the students’ ability to apply the viewpoints to hypothetical scenarios or predict the implications of new data.Ensure some questions assess the understanding of terms and concepts specific to the scientific disciplines discussed.Incorporate a question where students must identify a statement or concept that both viewpoints would likely agree upon.Add questions that prompt students to determine which viewpoint a new piece of evidence would support or contradict.Ensure questions range in complexity, from straightforward identification to more complex analytical thinking.Each question should include four plausible answer choices, challenging the student’s comprehension and analytical skills.Make sure the language and format align with the standards of the ACT test, suitable for high school students preparing for the exam. Make sure to format the multiple choice answers to have alot of space between eachother for clarity. Must include an answer key at the end"
                )
    llm = OpenAI(temperature=0.8,max_tokens=3800)
    title_chain = LLMChain(llm=llm, prompt=title_template)
    response = title_chain.run({"text": text})
    st.write(response)

## research summaries
## data representation