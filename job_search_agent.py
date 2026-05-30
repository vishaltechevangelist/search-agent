import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from agent_response_format import AgentResponse, Source
# from tavily import TavilyClient

load_dotenv()   

# llm = ChatGroq(api_key=os.environ.get('GROQ_API_KEY'), model=os.environ.get('LLM_MODEL_NAME'))
llm = ChatOllama(model="llama3.1:8b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-search-agents!")

    result = agent.invoke({"messages":[HumanMessage(content="Search 3 latest walkin for an ai engineer skills langchain in noida area and list their details")]})
    print(result['messages'][-1].content)


if __name__ == "__main__":
    main()
