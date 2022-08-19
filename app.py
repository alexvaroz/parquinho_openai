import streamlit as st
from openai_conn import request_openai


st.title("Parquinho para OpenAi")

st.write('Digite um texto e o complemento será gerado "automagicamente"... ')
text_content = ""
text = st.text_input(text_content)

words = []
if len(text) > 1:
    st.write(text)
    st.write(request_openai(text))

st.sidebar.header("About")
st.sidebar.subheader("Essa aplicação foi desenvolvida por Alexandre Vaz")
if st.sidebar.checkbox('Mostrar texto completo:'):
    st.subheader("Texto completo:")
    st.write(text)
st.sidebar.subheader("Parâmetros para a geração do texto:")
