#Estudo de caso 1 - DSA AI Coder - Criando Seu Assistente de Programação, em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar á API da plataforma Groq e acessa o LLM

from groq import Groq

#Configura as página do Streamlit com titulo ícone, layout e estudo inicial da sidebar

st.set_page_config(
    page_title = "DSA IA Code",
    page_icon= "🤖",
    layout = "wide",
    initial_sidebar_state="expanded"
)
