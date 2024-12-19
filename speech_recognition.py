import whisper
import logging

# Configure logging
logging.basicConfig(filename='speech_recognition_errors.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def speech_to_text(audio_file):
    logging.debug(f"Attempting to transcribe audio file: {audio_file}")
    
    try:
        model = whisper.load_model("base")
        logging.debug("Whisper model loaded successfully.")
        
        audio = whisper.load_audio(audio_file)
        if audio is None:
            logging.error("Failed to load audio.")
            return "Error: Failed to load audio."

        logging.debug("Audio loaded successfully.")
        
        result = model.transcribe(audio)
        if result is None:
            logging.error(f"Transcription result is None for audio file: {audio_file}")
            return "Error: Transcription result is None."

        logging.debug("Transcription successful.")
        return result['text']
    
    except FileNotFoundError:
        logging.error("File not found: {audio_file}")
        return "Error: Sorry boss, I didn't understand what you said"
    except whisper.WhisperError as e:
        logging.error(f"whisper error: {str(e)}")
        return "Error: Sorry boss, I wasn't able to hear you properly, Can you ask again"
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return "Error: Boss, an unexpected error occurred. please try again. "

