from langgraph.prebuilt import create_react_agent
from tools import get_tools
from langchain_mistralai.chat_models import ChatMistralAI
import os
from langchain_core.runnables.history import RunnableWithMessageHistory
import asyncio
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from pytz import timezone 
from datetime import datetime

ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')

checkpointer = InMemorySaver()

llm = ChatMistralAI(
    model="open-mistral-nemo",
    mistral_api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.7
)

tools = get_tools()
prompt = f"""You are an AI assistant, that can reason, search through internet, navigate urls, can create, see or draft emails and also can create events in google calendar using
     different tools.
    Current time is {ind_time}, refer this time while creating the events.
    Given a chat history and the latest user question which might reference context in the chat history.
     """
graph = create_react_agent(llm, 
            tools=tools, 
            prompt=prompt, 
            checkpointer=checkpointer)


# You need to provide a session_id when using get_session_history
# For demonstration, let's use a fixed session_id "default_session"
# agent_with_history = RunnableWithMessageHistory(
#     agent_executor,
#     lambda session_id: get_session_history(session_id),
#     input_messages_key="input",
#     history_messages_key="messages",
# )

def func(query, session_id="default_session"):
    try:
        print(f"⚡ func started with query: {query}, session_id: {session_id}")
        
        events = graph.stream(
            {"messages": [{"role": "user", "content": query}]},
            config={"configurable": {"thread_id": session_id}},
        )
        
        for event in events:
            print(f"⚡ got event: {event}")  # DEBUG
            if "agent" in event and "messages" in event["agent"]:
                for message in event["agent"]["messages"]:
                    if isinstance(message, AIMessage):
                        print(f"⚡ yielding: {message.content}")
                        yield message.content
            elif "output" in event:
                print(f"⚡ final output: {event['output']}")
                yield event["output"]

    except Exception as e:
        print("❌ Exception occurred:", e)
        import traceback
        traceback.print_exc()
        yield "Sorry, an error occurred."

# print(func("Who are you"))

# config = {"configurable": {"thread_id": "1"}}
# response = graph.invoke(
#     {"messages": [{"role": "user", "content": "Hello, how are you feeling"}]},
#     config  
# )
