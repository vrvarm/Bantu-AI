import pyaudio  #Used for audio input and output
import wave     #Used for reading and writing files
import logging  #Used to logging errors and debugging operations
import os 

# Configure logging 
logging.basicConfig(filename='audio_recording.log', level=logging.DEBUG, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
def record_audio(output_file, duration = 3): #default recording is 3 secs
    try:
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNCK = 1024
        RECORD_SECONDS = duration
        WAVE_OUTFILE = output_file
    
        audio = pyaudio.PyAudio()

        stream = audio.open(format = FORMAT, channel = CHANNELS, 
                           rate = RATE, input = True, frames_per_buffer = CHUNCK )

        frames = [] #Used to store audio frames in a list

        for _ in range (0, int(RATE / CHUNCK * RECORD_SECONDS)):
            data = stream.read(CHUNCK)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(WAVE_OUTFILE, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        logging.debug(f"Recording saved to: {WAVE_OUTFILE}")
        print ("Recording saved to: ", WAVE_OUTFILE)

    except Exception as e:
        logging.error(f"Error during audio recrding: {str(e)}")
        print ("Error during audio recording: ", str(e))

if __name__ == "__main__": 
    output_file = 'captured_audio.wav' # You can name it anything you like 
    record_audio(output_file, duration=3)