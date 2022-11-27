import cohere
import speech_recognition as sr
import os
import tkinter as tk
from playsound import playsound
# from dotenv import load_env

# load_env()
co = cohere.Client("")

r = sr.Recognizer()
# limited to 50 requests per day so we might need to use recognize_sphinx
input_finshed = False
prompt = f"""
bot is an emotion support voice assistant who wants to help the user feel better.
Usr: 
Bot:"""
mic = sr.Microphone(device_index=2) # index 2 because for me thats macbook mic (might differ for you)
examples = [
    cohere.classify.Example("I am very depressed today", "negative"),
    cohere.classify.Example("I am not happy", "negative"),
    cohere.classify.Example("I am anxious", "negative"),
    cohere.classify.Example("I am feeling fine today", "neutral"),
    cohere.classify.Example("I am feeling good", "positive"),
    cohere.classify.Example("I could be doing better", "neutral"),
    cohere.classify.Example("I am doing fine", "neutral"),
    cohere.classify.Example("I am lonely", "negative"),
    cohere.classify.Example("I am amazing", "positive"),
    cohere.classify.Example("Thank you", "positive"),
    cohere.classify.Example("I need help", "neutral"),
    cohere.classify.Example("I can do better", "neutral"),
    cohere.classify.Example("I am motivated to do better", "positive"), 
    cohere.classify.Example("I don't know what I am doing wrong", "negative"),

]
def generate(inp="hello"):
    # content = chat_output
    # co.classify(
    #     model='medium',
    #     inputs = inp,
    # )
    feelings = co.classify(
        model = 'medium',
        inputs = [inp],
        examples = examples
    )[0].prediction
    # c = f"Usr: {inp}" + "\nBot: "
    prompt = f"""
    bot is an emotion support voice assistant who wants to help the user feel better because user is {feelings},
    Usr: {inp}
    Bot:"""
    # chat_output = ""
    # chat_output = str(chat_output) + str(c)
    # print(chat)
    gen = co.generate(
        model='medium',  
        prompt = prompt,  
        max_tokens=30,  
        temperature=0.6,  
        stop_sequences=["Usr"]
    )
    text = gen[0].text.split("Usr",1)
    # prompt += f" {text[0]}"
    return text[0]


while not input_finshed: 
    # try catch statement to handle audio that cannot be transcribed
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)
            speech = r.recognize_google(audio)
            print(speech)
            if "exit" in speech:
                input_finshed = True
                continue
            if "meditate" in speech:
                playsound('music.mp3')
                continue
            resp = generate(speech) 
            # print(resp)
            os.system(f"say '{resp}'")
            # os.system(f"say '{resp}'")
            # testing to make it so that the system speaks something (won't be in this format)
            # look for alternatives to this it sounds too robot(y)
            # os.system(f"say '{speech}'") # speaks out loud on the computer
    except Exception as e:
        print(e)
        pass

def sentiment(input):
    pass
