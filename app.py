import streamlit as st
import random
import json
import os
import time
import pandas as pd

st.title('GRE Word Practice')

df = pd.read_csv("vocab_combined.csv")
df.columns = ["word", "meaning", "example"]
obj = None

def get_random_word():
    global obj
    rand_int = random.randint(0, len(df))
    obj = df.iloc[rand_int]

    return obj.word

def get_answer(word):
    global obj

    with placeholder.container():
        st.write('Answer is:')
        st.write(f'Word: {obj.word}')
        st.write(f'Meaning: {obj.meaning}')
        st.write(f'Example: {obj.example}')

placeholder = st.empty()

with placeholder.container():
    start = st.button('Next Word')
    word = None

    if start:
        word = get_random_word()
        st.write(f'Word: {word}')

with st.form(key='answer'):
    get_answer_button = st.form_submit_button('Get Answer', on_click=get_answer, args=(word,))

