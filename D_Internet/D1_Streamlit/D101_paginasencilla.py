""" Creamos una página sencilla con streamlit

    Para ejecutar el código usamos
        streamlit run main.py
"""

import streamlit as st

st.title('Pagina con StreamLit')
st.write('Hola mundo')

st.text_input('Ingresa tu nombre')
#nombre = st.text_input('Ingresa tu nombre')  # tambien funciona

