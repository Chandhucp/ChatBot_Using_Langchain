from langchain.llms import OpenAI
import streamlit as st
import os

# Uncomment the line below if you are using a .env file
# from dotenv import load_dotenv
# load_dotenv()

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "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"

## Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = OpenAI(model_name="text-davinci-003", temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY"))
    response = llm(question)
    return response

## Initialize our streamlit app
st.set_page_config(page_title="Q&A Chatbot By Chandrashekar")
st.header("Langchain Application")

input_question = st.text_input("Input: ", key="input")
response = get_openai_response(input_question)

submit = st.button("Ask Me")

## If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
