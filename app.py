from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from pathlib import Path
import textwrap

# Import the pipeline from transformers
from transformers import pipeline

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)

# Initialize the Hugging Face pipeline
try:
    pipe = pipeline("text-generation", model="gpt2")
except Exception as e:
    st.error(f"Error loading model: {e}")

## Function to get response from Hugging Face model
def get_huggingface_response(question):
    try:
        response = pipe(question, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return ""

## Initialize our streamlit app
st.set_page_config(page_title="LLM Demo")

st.header("Gemini App")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    response = get_huggingface_response(input)
    st.subheader("The Response is")
    st.write(response)
