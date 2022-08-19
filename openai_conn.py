import streamlit as st
import openai


openai.api_key = st.secrets["OPENAI_KEY"]


def request_openai(text, temp=0.7, max_tokens=1079):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=text,
      temperature=temp,
      max_tokens=max_tokens,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response["choices"][0]["text"]