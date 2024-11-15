import streamlit as st

#Streamlit-based functions used in multiple pages.

def generate_navigation_menu() -> None:
    """
    Display the navigation sidebar.
    """
    # st.set_page_config(
    #     page_title="Mon Quiz",
    #     layout="wide",
    #     initial_sidebar_state="expanded",
    #     )
    
    with st.sidebar:
        st.subheader("Navigation")
        st.page_link("main.py", label="Créer un quiz", icon="🛠️")
        st.page_link("pages/page_1.py", label="Jouer un Quiz", icon="🎲")

def reset_state() -> None:
    """
    Reset the game state.
    """
    st.session_state.good_answers = 0
    st.session_state.bad_answers = 0
    st.session_state.question_index = 0
    st.session_state.next_question = True
    st.session_state.reset_radio = True
    st.session_state.quiz_state = -1
    st.session_state.user_answers = []
    
