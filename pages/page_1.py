import streamlit as st
from question import Question
import json_handler as jh
from general_func import reset_state, generate_navigation_menu
from random import shuffle


# import asyncio

# async def test(label: any) -> None:
#     count = int(st.session_state.param_timer_difficulty[:-1])
#     st.session_state.current_question_timed_out = False
#     while count > 0:
#         count -= 1
#         label.markdown(f"Chronomètre : {count}")
#         await asyncio.sleep(1)
#     st.session_state.current_question_timed_out = True
#     st.session_state.param_timer = True
        

#Display the navigation side bar.
generate_navigation_menu()

#If no quiz is loaded, load the quiz and reset the game state.
if not "question_list" in st.session_state or st.session_state.question_list == []:
    reset_state()
    st.session_state.question_list = Question.return_questions_as_list(jh.get_dataset())

#Setting screen
if st.session_state.quiz_state == -1:
    st.session_state.test_bool = False
    st.header("Choisissez les paramètres de votre partie :", divider="blue")
    st.checkbox("Ordre aléatoire des questions", key="param_random_order")   
    st.checkbox("Seuil maximal de questions", key="param_maximum")
    if st.session_state.param_maximum:
        st.slider("Max", 1, 100, 1, 1, key="param_maximum_slider")
    st.checkbox("Questions chronométrées", key="param_timer")
    if st.session_state.param_timer:
        st.radio("Difficulté ⏳", ["5s", "15s", "30s"], key="param_timer_difficulty", index=0, horizontal=True)
    
    if st.button("Commencer"):
        if st.session_state.param_random_order :
            shuffle(st.session_state.question_list)
        if st.session_state.param_maximum:
            while len(st.session_state.question_list) > st.session_state.param_maximum_slider:
                st.session_state.question_list.pop()
        st.session_state.quiz_state = 0
        st.rerun()

#Main game loop (Each question is asked one after the other)
if st.session_state.quiz_state == 0:
    
    st.title(f"Question N°{st.session_state.question_index+1}")
    #Display the possible answers as radio buttons
    if st.session_state.reset_radio:
        question = st.radio(
            st.session_state.question_list[st.session_state.question_index].title,
            st.session_state.question_list[st.session_state.question_index].answers
        )

    #Store the correct answer's index for ease of read.
    c_answer = int(st.session_state.question_list[st.session_state.question_index].correct_answer)-1

    #Next question button logic
    if st.button("Question suivante"):
        #Assign good or bad points depending on user answer.
        if question == st.session_state.question_list[st.session_state.question_index].answers[c_answer]:
            st.session_state.good_answers += 1
        else:
            st.session_state.bad_answers += 1
        
        #Store user answer then step to next question.
        st.session_state.user_answers.append(st.session_state.question_list[st.session_state.question_index].answers.index(question))
        st.session_state.question_index += 1
        
        #If there are no more questions in current quiz, step to end of game state.
        if st.session_state.question_index >= len(st.session_state.question_list):
            st.session_state.quiz_state = 1
        #Else reset the radio buttons for the next question.
        else:
            st.session_state.reset_radio = True
        
        #Reload the script.
        st.rerun()

#End of game screen (results)        
if st.session_state.quiz_state == 1:
    
    #Score block. Display good answers, bad answers, score in % and a small caption depending on said score.
    col1, col2 = st.columns(2)
    with st.container():
        with col1:
            st.subheader(f"✅ Bonnes réponses : {st.session_state.good_answers}", divider="green")
        with col2:
            st.subheader(f"❌ Mauvaises réponses : {st.session_state.bad_answers}", divider="red")
        percent_answer = (st.session_state.good_answers/(len(st.session_state.user_answers)/100))
        st.subheader(f"Taux de réussite : {percent_answer:.2f}%")
        if percent_answer < 50:
            st.subheader("Peut mieux faire. 🥉")
            st.image("images/lepers_non.gif")
            st.audio("sounds/lepers_cest_non.mp3", autoplay=True)
        elif percent_answer >= 100:
            st.subheader(":rainbow[Parfait !] 🏆")
            st.image("images/lepers_ouioui.gif")
            st.audio("sounds/lepers_ouioui.mp3", autoplay=True)
        elif percent_answer >= 75:
            st.subheader("Excellent! 🥇")   
            st.image("images/lepers_3points.gif")
        else:
            st.subheader("Bien ! 🥈")
            st.image("images/lepers_1point.gif")
    
    #Display the details of the quiz questions in an expendable container.
    #Display each question with the user's answer. Display the correct answer for wrong answers.
    with st.expander("Détails des réponses"):
        count = 1
        for item, answer in zip(st.session_state.question_list, st.session_state.user_answers):
            st.write(f"{count}°) {item.title}")
            if item.correct_answer-1 != answer:
                st.write(f":red-background[Faux !] \n\n Vous avez répondu : :red[{item.answers[answer]}]. La bonne réponse était : :green[{item.answers[item.correct_answer-1]}]")
            else:
                st.write(f":green-background[Bonne réponse !]\n\n Vous avez répondu : :green[{item.answers[item.correct_answer-1]}]")
            if count < len(st.session_state.user_answers):
                st.divider()
            count += 1
    
    #Creature empty space for clarity
    st.divider()
    
    #Use columns to center the button
    col1, col2, col3 = st.columns(3)
    
    #Restart button. Launch the quiz back from question 1.
    with col2:
        if st.button("Recommencer"):
            reset_state()
            st.rerun()

# if st.session_state.param_timer and st.session_state.quiz_state == 0:
#         test_async = st.empty()
#         asyncio.run(test(test_async))
#         if st.session_state.current_question_timed_out:
            
#             st.session_state.user_answers.append(-1)
#             st.session_state.bad_answers += 1
#             st.session_state.question_index += 1
            
#             st.session_state.popup_message = "TIMED OUT"
            
#             #If there are no more questions in current quiz, step to end of game state.
#             if st.session_state.question_index >= len(st.session_state.question_list):
#                 st.session_state.quiz_state = 1
#             #Else reset the radio buttons for the next question.
#             else:
#                 st.session_state.reset_radio = True
                
#             st.rerun()





