"""
We are using the "speech_recognition" module in Python for voice_based tasks. This module offers several APIs [Application Programming Interface] to work with audio.
We have used the "recognise_google()" API for our purpose.

"""


import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def startListening():
    with microphone as audio_source:
        user_voice_in_chunks= recognizer.listen(audio_source)
    
    convertInputChunksToWavFile(user_voice_in_chunks)
    
def convertInputChunksToWavFile(user_voice_in_chunks):
    with open("microphone_results.wav", "wb") as f:
        f.write(user_voice_in_chunks.get_wav_data()) #writes the byte string to wav file
        
def returnPathToFile():
    pathToFile = "microphone_results.wav"
    return pathToFile

def returnAudioWavFile():
    return sr.AudioFile(returnPathToFile())

def returnAudioDataObject():
    with audio_wav_file as source:
        audio_data_object = recognizer.record(source)
    return audio_data_object

if __name__ == "__main__":
    
    startListening()

    audio_wav_file = returnAudioWavFile()

    audio_data_object = returnAudioDataObject()

    actual_text_obtained_from_user = recognizer.recognize_google(audio_data_object)
    
    print(actual_text_obtained_from_user)

