import uuid
import streamlit as st
from langgraph_backend import workflow
from langchain_core.messages import HumanMessage

# ************************************** Utility Functions ************************
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_converstion(thread_id):
    return workflow.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']

# ************************************* Session Setup *****************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])



# ************************************ Sidebar UI *********************************
st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('Chats')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_converstion(thread_id)

        temp_messages = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})
        
        st.session_state['message_history'] = temp_messages



# ************************************ Main UI ************************************

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input(placeholder="Type Here")

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    with st.chat_message('assistant'):
        
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': HumanMessage(content=user_input)},
                config = {'configurable': {'thread_id': st.session_state['thread_id']}},
                stream_mode='messages',
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})