"""
We are using the "speech_recognition" module in Python for voice_based tasks. This module offers several APIs [Application Programming Interface] to work with audio.
We have used the "recognise_google()" API for our purpose.

"""


import speech_recognition as sr
import pyttsx3


class AudioInputHandler:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.actual_text_obtained_from_user = ""
        

    def startListening(self):
        self.startListeningToAudioInput()

        self.audio_wav_file = self.returnAudioWavFile()

        self.audio_data_object = self.returnAudioDataObject()

        self.actual_text_obtained_from_user = self.recognizer.recognize_google(self.audio_data_object)

        return self.actual_text_obtained_from_user

    
    def startListeningToAudioInput(self):
        with self.microphone as self.audio_source:
            self.user_voice_in_chunks= self.recognizer.listen(self.audio_source)
    
        self.convertInputChunksToWavFile(self.user_voice_in_chunks)
    

    def convertInputChunksToWavFile(self, user_voice_in_chunks):
        with open("microphone_results.wav", "wb") as f:
            f.write(self.user_voice_in_chunks.get_wav_data()) #writes the byte string to wav file


    def returnAudioWavFile(self):
        return sr.AudioFile(self.returnPathToFile())

    def returnPathToFile(self):
        self.pathToFile = "microphone_results.wav"
        return self.pathToFile


    def returnAudioDataObject(self):
        with self.audio_wav_file as self.source:
            self.audio_data_object = self.recognizer.record(self.source)
        return self.audio_data_object

    
    def returnActualTextObtainedFromDataObject(self, audio_data_object):
        self.actual_text_obtained_from_user = self.recognizer.recognize_google(audio_data_object)
        return self.actual_text_obtained_from_user


    

class ProgramTalkback:
    
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def speak(self, textToBeSpoken):
        self.engine.say(textToBeSpoken)
        self.engine.runAndWait()
        
        
##def startListening():
##    with microphone as audio_source:
##        user_voice_in_chunks= recognizer.listen(audio_source)
##    
##    convertInputChunksToWavFile(user_voice_in_chunks)
##    
##def convertInputChunksToWavFile(user_voice_in_chunks):
##    with open("microphone_results.wav", "wb") as f:
##        f.write(user_voice_in_chunks.get_wav_data()) #writes the byte string to wav file
##        
##def returnPathToFile():
##    pathToFile = "microphone_results.wav"
##    return pathToFile
##
##def returnAudioWavFile():
##    return sr.AudioFile(returnPathToFile())
##
##def returnAudioDataObject():
##    with audio_wav_file as source:
##        audio_data_object = recognizer.record(source)
##    return audio_data_object

if __name__ == "__main__":


    audio_input_handler = AudioInputHandler()
    
    textSpokenByUser = audio_input_handler.startListening()
    
   
    print(textSpokenByUser)

    program_talkback = ProgramTalkback()
    program_talkback.speak("Ayush")
    


##    
##    startListening()
##
##    audio_wav_file = returnAudioWavFile()
##
##    audio_data_object = returnAudioDataObject()
##
##    actual_text_obtained_from_user = recognizer.recognize_google(audio_data_object)
##    
##    print(actual_text_obtained_from_user)
##
