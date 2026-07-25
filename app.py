import streamlit as st
from googletrans import Translator

st.title("Language Translation Tool")

text = st.text_area("Enter text")

source = st.text_input("Source language code (example: en)")
target = st.text_input("Target language code (example: ta)")

if st.button("Translate"):
    translator = Translator()
    result = translator.translate(text, src=source, dest=target)
    st.success(result.text)
