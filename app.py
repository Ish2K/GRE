import streamlit as st
import random
import json
import os
import time

st.title('GRE Word Practice')

with open("vocab.json", "r", encoding="utf-8") as f:
    words = json.load(f)

def get_random_word():
    word = random.choice(list(words.keys()))
    return word

def get_answer(word):
    ans = words[word]

    with placeholder.container():
        st.write('Answer is:')
        st.write(f'Word: {word}')
        st.write(f'Meaning: {ans["meaning"]}')
        st.write(f'Example: {ans["example"]}')

placeholder = st.empty()

with placeholder.container():
    start = st.button('Next Word')
    word = None

    if start:
        word = get_random_word()
        st.write(f'Word: {word}')

with st.form(key='answer'):
    get_answer_button = st.form_submit_button('Get Answer', on_click=get_answer, args=(word,))