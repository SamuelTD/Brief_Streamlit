import streamlit as st
from question import Question
import json_handler as jh

def reset_state() -> None:
    st.session_state.good_answers = 0
    st.session_state.bad_answers = 0
    st.session_state.question_index = 0
    st.session_state.next_question = True
    st.session_state.reset_radio = True
    st.session_state.quiz_state = 0

if not "question_list" in st.session_state or st.session_state.question_list == []:
    reset_state()
    st.session_state.question_list = Question.return_questions_as_list(jh.get_dataset())

if st.session_state.quiz_state == 0:
    
    st.title(f"Question N°{st.session_state.question_index+1}")

    if st.session_state.reset_radio:
        question = st.radio(
            st.session_state.question_list[st.session_state.question_index].title,
            st.session_state.question_list[st.session_state.question_index].answers
        )

    c_answer = int(st.session_state.question_list[st.session_state.question_index].correct_answer)-1

    if st.button("Question suivante"):
        if question == st.session_state.question_list[st.session_state.question_index].answers[c_answer]:
            st.session_state.good_answers += 1
        else:
            st.session_state.bad_answers += 1
            
        st.session_state.question_index += 1
        if st.session_state.question_index >= len(st.session_state.question_list):
            st.session_state.quiz_state = 1
        else:
            st.session_state.reset_radio = True
        st.rerun()
        
if st.session_state.quiz_state == 1:
    st.write(f"Bonnes réponses : {st.session_state.good_answers}")
    st.write(f"Mauvaises réponses : {st.session_state.bad_answers}")
    if st.button("Recommencer"):
        reset_state()
        st.rerun()





