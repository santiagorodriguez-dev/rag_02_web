
import streamlit as st # type: ignore
import uuid
from src import support as sp

# Show title and description.
st.title("💬 Chatbot RAG'S")
st.write(
    "Chatbot con información de Rags de Historia, Presente, Futuro de la IA (gpt-4o-mini de openai)"
)

if st.secrets['security']['SECRET'] != "":
    secret = st.secrets['security']['SECRET']
else:
    secret = ""

secret = st.text_input("Introduce Secret para poder continuar", type="password")

if not secret:
    pass
else:
    thread_id = str(uuid.uuid4())
    user = "user_" + str(uuid.uuid4())
    prompt = st.chat_input("What is up?")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
         with st.chat_message(message["role"]):
              st.markdown(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        api_url = st.secrets['security']['API_URL']
        data = {
            "code":secret,
            "input_message":prompt,
            "thread_id":thread_id,
            "user_id":user
        }
        resultado = sp.post_request(api_url, data)

        if resultado.get('status_code') == 401:
            with st.chat_message("assistant"):
                st.markdown("Secret es incorrecto, indique uno valido válido")
            st.stop()

        if resultado.get('status_code') == 500:
            with st.chat_message("assistant"):
                st.markdown("Error al procesar la solicitud, intente de nuevo")
            st.stop()

        if resultado.get('mesajes_trazas'):
            with st.chat_message("ia", avatar="💻"):
                st.markdown(resultado.get('mesajes_trazas'))
                st.session_state.messages.append({"role": "ia", "content": resultado.get('mesajes_trazas')})

        with st.chat_message("assistant"):
            st.markdown(resultado.get('content'))
            st.session_state.messages.append({"role": "assistant", "content": resultado.get('content')})
