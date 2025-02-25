import streamlit as st
import random
import re

def get_questions_from_text(text):

    return re.findall(r"\d+\.\s[^\n]+", text)

def select_random_questions(files):
    
    selected_questions = {}

    for file in files:
        text = file.getvalue().decode("utf-8")  
        questions = get_questions_from_text(text)

        if questions:
            selected_questions[file.name] = random.choice(questions)
        else:
            selected_questions[file.name] = "Вопросов НЕТ!"

    return selected_questions

st.title("Вопросы по Теоретической и Прикладной Лингвистике")
st.write("Загрузите файлы и программа выберет по одному вопросу из каждого.")

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = None

uploaded_files = st.file_uploader("Загрузите файлы", accept_multiple_files=True, type="txt")

if uploaded_files:
    st.session_state.uploaded_files = uploaded_files

if st.session_state.uploaded_files:
    selected_questions = select_random_questions(st.session_state.uploaded_files)
    st.subheader("Вопросы:")

    for doc, question in selected_questions.items():
        st.write(f"📄 **{doc}**: {question}")
    
if st.button("Начать заново"):
    st.session_state.uploaded_files = None  
    st.rerun()  

