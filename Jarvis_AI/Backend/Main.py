from Jarvis_AI.Backend.speech_recognition import speech_to_text
from Jarvis_AI.Backend.NL_process import get_response
from text_to_speech import text_to_speech
from Jarvis_AI.Frontend.API import start_api_server
import threading
import time

def main():
    # Start the Flask API server in a separate thread
    api_thread = threading.Thread(target = start_api_server)
    api_thread.start()

    start_time = time.time()
    time_limit = 2 * 60 #2 mins delay

    while True:
        time_used = time.time() - start_time
        if time_used > time_limit:
            print ("Time's up")
            break

        user_input = speech_to_text()
        if user_input:
            response = get_response(user_input)
            print(f"Bantu: {response}") #Also gives output in text form
            text_to_speech(response)

if __name__ == "__main__":
    main()