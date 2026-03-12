import subprocess
import shutil
from tool_registry import function_tool

def _launch_app(app):
  if shutil.which(app.lower()):
    subprocess.Popen([app.lower()])
  else:
    subprocess.Popen(["start", app], shell=True)

@function_tool(
  description="Opens a desktop application by name. ",
  parameters={
    "type": "object",
    "properties":{
      "app_name": {"type": "string"}
    },
    "required": ["app_name"]
  }
)
def open_application(app_name: str):
  _launch_app(app_name)
  return f"{app_name} opened successfully."