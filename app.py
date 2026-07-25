import streamlit as st
from translate import Translator

# Page settings
st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")

st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages.")

# Language dictionary
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

# Input text
text = st.text_area("Enter text to translate:")

# Language selection
source_language = st.selectbox("Select Source Language", list(languages.keys()))
target_language = st.selectbox("Select Target Language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    elif source_language == target_language:
        st.warning("Source and Target languages cannot be the same.")
    else:
        try:
            translator=Translator()
            translated=translator.translate(text,src=source,dest=target).text

            st.success("Translation Successful!")
            st.subheader("Translated Text")
            st.write(translated_text)

        except Exception as e:
            st.error(f"Error: {e}")
