import speech_recognition as sr
import os
# import cohere
# from cohere.classify import Example
# co = cohere.Client('KcujpY0yBg7MG7MJUXf99foQFb3IBbjAZ7NQpxYX')

r = sr.Recognizer()
# use recognize_google() for google web speech api (no install req)
# limited to 50 requests per day so we might need to use recognize_sphinx
input_finshed = False
mic = sr.Microphone(device_index=2) # index 2 because for me thats macbook mic (might differ for you)
while not input_finshed: 
    # try catch statement to handle audio that cannot be transcribed
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            speech = r.recognize_google(audio)
            print(speech)
            # testing to make it so that the system speaks something (won't be in this format)
            # look for alternatives to this it sounds too robot(y)
            os.system(f"say '{speech}'") # speaks out loud on the computer
    except:
        pass