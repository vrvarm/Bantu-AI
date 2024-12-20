from speech_recognition import speech_to_text
from NL_process import get_response
from text_to_speech import text_to_speech
from API import start_api_server
from Record_Audio import record_audio
from Logging_config import setup_logging
import threading
import logging
import time
import ctypes 
def load_shared_library(libc_name): 
    if libc_name is None: 
        logging.error("libc_name is None. Cannot load shared library.") 
        print("Error: libc_name is None. Cannot load shared library.") 
        return None 
    try: 
        logging.debug(f"Loading shared library: {libc_name}") 
        lib = ctypes.CDLL(libc_name) 
        logging.debug("Shared library loaded successfully.") 
        return lib 
    except Exception as e: 
        logging.error(f"Error loading shared library: {str(e)}") 
        print(f"Error: {str(e)}") 
        return None 
def main(): 
    # Set up logging 
    setup_logging() 
    # Example: Load a shared library (adjust the path as needed)
    libc_name = "D:\Bantu_audio_files" 

    # Replace with actual value 
    lib = load_shared_library(libc_name)

    setup_logging()

    # Start the Flask API server in a separate thread
    api_thread = threading.Thread(target = start_api_server, args = ("input_text",))
    api_thread.start()

    start_time = time.time()
    time_limit = 2 * 60 #2 mins delay

    while True:
        time_used = time.time() - start_time
        if time_used > time_limit:
            logging.info("Times up")
            print ("Time's up")
            break
        
        print("Listening for audio input...")
        audio_file = 'captured_audio.wav'
        record_audio(audio_file,duration = 3)

        user_input = speech_to_text(audio_file)
        if user_input.startswith('Error'):
            print(f"Error at -- {user_input}")
        else:
            print (f"User said: {user_input}")
            response = get_response(user_input)
            print (f"Bantu: {response}") #Also gives output in text form
            text_to_speech(response)

if __name__ == "__main__":
    main()