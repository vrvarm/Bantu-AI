import pyttsx3

# Initializing Text-to-Speech engine with sapi5 engine
engine = pyttsx3.init('sapi5')

# Getting list of available voices in the system
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# command used to change text to speech
def speak(audio):
    engine.say(audio)
    print(f"Jarvis: {audio}")
    engine.runAndWait()

if __name__ == '__main__':
    speak("Hello, I am Jarvis. How can I help you?")