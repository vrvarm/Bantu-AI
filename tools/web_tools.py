import webbrowser
import urllib.parse
from tool_registry import function_tool

@function_tool(
  description="Searchs the web for a given query.",
  parameters={
    "type": "object",
    "properties":{
      "query": {"type":"string"}
    },
    "required":["query"]
  }
)
def search_web(query: str):
  url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
  webbrowser.open(url)
  return f"I have opeend Google search for '{query}'."