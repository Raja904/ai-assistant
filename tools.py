import os
import requests
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_googledrive.tools.google_drive.tool import GoogleDriveSearchTool
from langchain_google_community import GmailToolkit
from langchain_google_community import CalendarToolkit
from fetch_page import fetch_page_text
from Credentials import get_credentials


creds = get_credentials()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

calendar_toolkit = CalendarToolkit(credentials=creds)
gmail_toolkit = GmailToolkit(credentials=creds)
search = GoogleSerperAPIWrapper()
# Tools list
def get_tools():
    tools = [
    Tool(
        name="Google_search",
        func=search.run,
        description="Useful when you need to get info from Google search."
    ),
    Tool(
        name="navigate_urls_in_browser",
        func=fetch_page_text,
        description="Fetch the text content of a webpage by navigating to the URL using a headless browser API."
    )
]
    tools.extend(calendar_toolkit.get_tools())
    tools.extend(gmail_toolkit.get_tools())
    # print("Tools loaded:", [tool.name for tool in tools])
    return tools






