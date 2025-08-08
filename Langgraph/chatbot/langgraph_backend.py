from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from typing import TypedDict, Annotated
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

# State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Graph
graph = StateGraph(ChatState)


def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}


# Node
graph.add_node('chat_node', chat_node)

# Edges
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# Checkpointer
checkpointer = InMemorySaver()

# Compile
workflow = graph.compile(checkpointer=checkpointer)