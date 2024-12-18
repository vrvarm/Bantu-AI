from fastapi import FastAPI
from pydantic import BaseModel
from Jarvis_AI.Backend.NL_process import get_response
import uvicorn

app = FastAPI()

class Item(BaseModel):
    text: str
@app.post("/get-response/")
def process_request(item: Item):
    response = get_response(item.text)
    return {"response" : response}

def start_api_server(input_text):
    uvicorn.run(host = "271.0.0.1", post = "5000")