import speech_recognition as sr
import wave

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source)

        # Save the audio input as a WAV file
        with wave.open(audio_file, 'wb') as f:
            f.setnchannels(source.get_num_channels())
            f.setsampwidth(source.get_sample_width())
            f.setframerate(source.get_sample_rate())
            f.writeframes(audio.get_raw_data())
    try:
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry boss, I didn't understand what you are trying to say")
    except sr.RequestError as e:
        print(f"due to network Issues, Audio Quality, or Service Unavailability, I can't here you: {e}")
