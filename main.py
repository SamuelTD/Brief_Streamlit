import streamlit as st
import pandas as pd
import numpy as np
import json_handler as jh
from question import Question

#RESET QUIZ STATE
st.session_state.good_answers = 0
st.session_state.bad_answers = 0
st.session_state.question_index = 0
st.session_state.question_list = []
st.session_state.next_question = True
st.session_state.reset_radio = True
st.session_state.quiz_state = 0

if not "current_question_list" in st.session_state:
    st.session_state.current_question_list = []

title = st.text_input("Question")
answers = st.text_area("Answers")
correct_answers = st.text_input("Correct answer")

st.session_state.current_question = title
st.session_state.answers = answers.split("\n")
st.session_state.correct_answer = correct_answers

column1, column2 = st.columns(2)

with column1:
    if st.button("Ajoutez ma question"):
        if st.session_state.current_question != "" and \
            st.session_state.answers != "" and \
                st.session_state.correct_answer != "":
            st.session_state.current_question_list.append(Question(st.session_state.current_question, st.session_state.answers, st.session_state.correct_answer))
            st.write(f"Question ajoutée avec succès.\nIl y a {len(st.session_state.current_question_list)} questions dans le quiz.")
        else:    
            st.write("Invalide : Un ou plusieurs champs sont vides.")
        

with column2:    
    if st.button("Créer le quiz"):
        if len(st.session_state.current_question_list) == 0:
            st.write("Il n'y a aucune question dans le quiz.")
        else:
            jh.write_dataset(st.session_state.current_question_list)
            st.write(f"Le quiz a été créé avec {len(st.session_state.current_question_list)} questions !")
            st.session_state.current_question_list = []
    



