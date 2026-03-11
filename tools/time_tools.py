import datetime as dt
from tool_registry import function_tool

@function_tool(
  description="Return the current local date and time",
  parameters={
    "type": "object",
    "properties": {}
  }
)
def get_current_time():
  now = dt.datetime.now()
  return f"The current date and time is {now.strftime('%A, %B %d %Y at %I:%M %p')}"