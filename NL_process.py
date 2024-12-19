from transformers import pipeline

def get_response(input_text):
    nlp_pipline = pipeline('conversational', model = 'microsoft/DialoGPT-medium')
    response = nlp_pipline(input_text)
    return response