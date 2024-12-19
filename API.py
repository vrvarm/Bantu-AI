from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from NL_process import get_response

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/get-response/")
def process_request(item: Item):
    response = get_response(item.text)
    return {"response" : response}

def start_api_server(input_text):
    uvicorn.run(app, host = "271.0.0.1", port = "5000")