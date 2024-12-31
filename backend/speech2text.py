from text2speech import speak
import speech_recognition as sr

# function used to change speech to text
def commands():
    r = sr.Recognizer() 

    # capture audio from the microphone and convert it to text. 
    # 1 second pause is used between each capture to allow the microphone 
    # to adjust to the ambient noise level.

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r. adjust_for_ambient_noise (source, duration = 1)
        audio = r.listen(source)
    
    try: 
        print("Wait for few minutes ...")
        query = r.recognize_google(audio, language = 'en-in')   # The recognizer is configured to 
                                                                #understand the English language.
        print(f"Ravi: {query}\n")

    except Exception as e:  #Captures errors 
        print(e)
        speak("I didn't hear you boss. Repeat what you said? ")
        query = "none"
    
    return query