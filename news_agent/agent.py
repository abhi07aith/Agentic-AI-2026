from google.adk.agents.llm_agent import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool
 
news_scrap_tool = CrewaiTool(
    name="check_news_scrap",
    description=(
        "Scrapes the latest Times of india technology news from the official Times of india website."
        "Use it to answer questions about recent Times of india technology news."
    ),
    tool=ScrapeWebsiteTool("https://www.jagran.com/uttar-pradesh"),
)
 
 
root_agent = Agent(
    model='gemini-2.5-flash',
    name='news_agent',
    description='A helpful assistant for user on latest tech news.',
    instruction='Answer user questions based on given news scrap tool only',
    tools=[news_scrap_tool]
)
 