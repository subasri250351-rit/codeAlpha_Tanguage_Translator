import streamlit as st
import requests

st.title("Language Translation Tool")

text = st.text_area("Enter text")

source = st.text_input("Source language code (example: en)")
target = st.text_input("Target language code (example: ta)")

if st.button("Translate"):
    url = "https://translate.googleapis.com/translate_a/single"

    params = {
        "client": "gtx",
        "sl": source,
        "tl": target,
        "dt": "t",
        "q": text
    }

    response = requests.get(url, params=params)
    result = response.json()

    translated = result[0][0][0]
    st.success(translated)
