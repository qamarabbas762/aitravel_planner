from langchain_community.utilities import GoogleSerperAPIWrapper
from src.config.config import SERPER_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def google_serper_tool(query:str) -> str:
    """Search the web using Google Serper. for travel,tips,attractions,hotels, etc"""
    try:
        google_search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)
        result = google_search.run(query)
        logger.info(f"Google Serper search successful for query: {query}")
        return result
    except Exception as e:
        logger.error(f"Error in Google Serper search for query: {query} | Error details: {str(e)}")
        return "Sorry, I couldn't fetch the information right now."
    
logger.info("Google Serper tool is ready")
