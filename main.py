import streamlit as st
import pandas as pd
import numpy as np
import json_handler as jh
from question import Question
from general_func import reset_state, generate_navigation_menu
from string import ascii_uppercase
from pydantic import ValidationError

def get_questions_from_input() -> None:
    st.session_state.answers = st.session_state.input_answers.split("\n")

#Reset the game state.
reset_state()
st.session_state.question_list = []

#Create the Question list for current quiz if none exists.
if not "current_question_list" in st.session_state:
    st.session_state.current_question_list = []
    st.session_state.reset_input_fields = False

#Display the navigation sidebar
generate_navigation_menu()

#Reset the input fields when a question has been created or a quiz has been created and display a confirmation popup.
if st.session_state.reset_input_fields :
    st.session_state.current_question = ""
    st.session_state.input_answers = ""
    st.session_state.correct_answer = ""
    st.session_state.reset_input_fields = False
    st.toast(st.session_state.popup_message)

#User text inputs for title, answer options and correct answer.
st.subheader("Intitulé de la question :")
st.text_input("", key="current_question", label_visibility="collapsed")
st.subheader("Options de réponses (séparées par un retour à la ligne) : ")
st.text_area("", key="input_answers", on_change=get_questions_from_input, label_visibility="collapsed")
st.subheader("Numéro de la bonne réponse : ")
st.text_input("", key="correct_answer", label_visibility="collapsed")

#Display both buttons on the same row.
column1, column2 = st.columns(2)

with column1:
    #Create a Question object based on current user inputs and add it to the current list
    if st.button("Ajoutez ma question"):
        #Check if all fields have been written in.
        if st.session_state.current_question != "" and \
            st.session_state.input_answers != "" and \
                st.session_state.correct_answer != "":            
            
            #Validate the parsed datas
            try :      
                # new_question = Question.model_validate({'title':st.session_state.current_question, 'answers': st.session_state.answers, 'correct_answer':st.session_state.correct_answer})     
                new_question = Question(title= st.session_state.current_question, answers= st.session_state.answers, correct_answer =st.session_state.correct_answer)     
                
                #Check if fielded answer index is within possible range.
                if (new_question.correct_answer > len(new_question.answers)):
                    st.write(f":red[La bonne réponse ne se situe pas dans le spectre des réponses possibles.]") 
                else:   
                    st.session_state.current_question_list.append(new_question)
                    st.session_state.popup_message = f"Question ajoutée avec succès.\nIl y a {len(st.session_state.current_question_list)} questions dans le quiz."
                    st.session_state.reset_input_fields = True
                    st.rerun()
            except ValidationError as e:      
                st.error(f":red[{e.errors()[0]["msg"].replace("Value error, ", "")}]")     
        
        else:    
            st.error(":red[Invalide : Un ou plusieurs champs sont vides.]")
        

with column2:   
    #If there is at least one Question object in the list, write the list as JSON file. 
    if st.button("Créer le quiz"):
        if len(st.session_state.current_question_list) == 0:
            st.error(":red[Ajoutez au moins une question pour créer le quiz.]")
        else:
            jh.write_dataset(st.session_state.current_question_list)
            st.session_state.popup_message = f"Le quiz a été créé avec {len(st.session_state.current_question_list)} questions !"
            st.session_state.current_question_list = []
            st.session_state.reset_input_fields = True
            st.rerun()

#Display all current questions in the Quiz with a button to delete them.
if len(st.session_state.current_question_list) > 0:
    with st.expander("Questions en cours de validation :"):
            index = 0            
            for item in st.session_state.current_question_list:
                sub_index = 0
                st.subheader(f"{index+1}°) {item.title}")
                for q in item.answers:
                    st.write(f"{ascii_uppercase[sub_index]}°) {q}")
                    sub_index+=1
                st.write(f":green[**Réponse : {item.answers[int(item.correct_answer)-1]}**]")
                if st.button("Supprimer", key=f"q_{index}"):
                    st.session_state.current_question_list.pop(index)  
                    st.rerun()                  
                if index < len(st.session_state.current_question_list)-1:
                    st.divider()
                index += 1
    



