import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()   

tavily = TavilyClient(api_key=os.environ.get('TAVILY_API_KEY'))

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search on internet
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatGroq(api_key=os.environ.get('GROQ_API_KEY'), model=os.environ.get('LLM_MODEL_NAME'))
# llm = ChatOllama(model="llama3.1:8b")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-search-agents!")
    result = agent.invoke({"messages":[HumanMessage(content="Search 3 latest job postings for an ai engineer skills langchain in noida area and list their details")]})
    print(result)


if __name__ == "__main__":
    main()
