import inspect

tool_registry = {}
tool_schemas = []

# function used to auto register tools
def function_tool(description: str, parameters: dict):
  def decorator(func):
    tool_name = func.__name__

    # Register callable
    tool_registry[tool_name] = func

    # Build schema for groq
    tool_schemas.append(
      {
        "type": "function",
        "function": {
          "name": tool_name,
          "description": description,
          "parameters": parameters
        }
      }
    )

    return func
  return decorator