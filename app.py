import streamlit as st
import random
import time
from agent import func # Assuming 'func' is your AI agent functionA
import uuid

st.set_page_config(page_title="AI Assistant - for Emails, Calendar and Web Browsing", layout="centered")

st.title("AI Assistant - for Emails, Calendar and Web Browsing")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    print(f"New session created: {st.session_state.session_id}")
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
# def response_generator(prompt_input, session_id):
#     full_response = func(prompt_input, session_id) # Call func here to get the complete response string
#     for word in full_response.split():
#         yield word + " "
#         time.sleep(0.05) # Adjust sleep time for desired streaming speed
        


# Accept user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_chunks = []  # to collect streamed chunks
        for chunk in st.write_stream(func(prompt, st.session_state.session_id)):
            response_chunks.append(chunk)
        full_response = "".join(response_chunks)

    st.session_state.messages.append({"role": "assistant", "content": full_response})


