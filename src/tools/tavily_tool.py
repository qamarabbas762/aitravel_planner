from langchain_tavily import TavilySearch
from src.utils.logger import get_logger
from src.config.config import TAVILY_API_KEY

logger = get_logger(__name__)

def tavily_search_tool(query:str) -> str:
    """Search the web using Tavily Search. for travel,tips,attractions,hotels, etc"""
    try:
        tavily_search = TavilySearch(max_results=5,toipc='general' ,tavily_api_key=TAVILY_API_KEY)
        result = tavily_search.invoke(query)
        logger.info(f"Tavily Search successful for query: {query}")
        return result
    except Exception as e:
        logger.error(f"Error in Tavily Search for query: {query} | Error details: {str(e)}")
        return "Sorry, I couldn't fetch the information right now."

logger.info("Tavily Search tool is ready")