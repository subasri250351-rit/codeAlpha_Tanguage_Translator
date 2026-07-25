import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter text")

source = st.text_input("Source language code (example: en)")
target = st.text_input("Target language code (example: ta)")

if st.button("Translate"):
    if text:
        result = GoogleTranslator(source=source, target=target).translate(text)
        st.success(result)
