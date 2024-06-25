import os
import math_helper as math_helper
import reading_helper as reading_helper
import science_helper as science_helper
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

subject_type = st.sidebar.selectbox("what subject do you want to study" , ("Math", "English","Reading", "Science"))
st.title('ACT problems')
#second sidebar
if subject_type == "Math":
    topic_type=st.sidebar.selectbox("What topic of Math do you want to study", ("General ACT Math","Elementary Algebra and Intermediate", "Plane and coordiante Geometry", "Trigonometry"))

if subject_type == "English":
    topic_type=st.sidebar.selectbox("What topic of English do you want to study", ("Algebra", "Geometry", "Matricies", "System of Equations", "Trigonometry"))

if subject_type == "Reading":
    topic_type=st.sidebar.selectbox("What passage of Reading do you want to Practice", ("Prose Fiction", "Social Science", "Humanities","Natural Science"))

if subject_type == "Science":
    topic_type=st.sidebar.selectbox("What topic of math do you want to study", ("Data Representation","Confliting Viewpoints","Research Summaries"))
    dual_passage = st.sidebar.checkbox("Dual Passage")
    
if subject_type == "Math":
   response = math_helper.generate_math_problems(subject_type,topic_type)
#while subject_type == "Reading":
    #response = reading_helper.get_questions(reading_helper.create_transcript())
if subject_type == "Science":
    response = science_helper.generate_questions(science_helper.generate_conflicting_viewpoints(topic_type))
