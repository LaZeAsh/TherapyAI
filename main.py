import cohere
import speech_recognition as sr
import os
co = cohere.Client('KcujpY0yBg7MG7MJUXf99foQFb3IBbjAZ7NQpxYX')

r = sr.Recognizer()
# # use recognize_google() for google web speech api (no install req)
# chat = f"""  
#     Bot is an emotion support chat bot who wants to help the user feel better.
# """
# limited to 50 requests per day so we might need to use recognize_sphinx
input_finshed = False
global chat_output
# chat_output = ""
mic = sr.Microphone(device_index=2) # index 2 because for me thats macbook mic (might differ for you)

def generate(inp):
    content = chat_output
    c = f"Usr: {inp}" + "\nBot: "
    # chat_output = ""
    chat_output = str(chat_output) + str(c)
    # print(chat)
    gen = co.generate(  model='medium',  prompt = chat_output,  max_tokens=30,  temperature=0.6,  stop_sequences=["Usr"])
    text = gen[0].text.split("Usr",1)
    return text[0]
    # return chat_output


while not input_finshed: 
    # try catch statement to handle audio that cannot be transcribed
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)
            speech = r.recognize_google(audio)
            print(speech)
            resp = generate("Hello") 
            print(resp)
            os.system(f"say '{resp}'")
            if "exit" in speech:
                input_finshed = True
            # os.system(f"say '{resp}'")
            # testing to make it so that the system speaks something (won't be in this format)
            # look for alternatives to this it sounds too robot(y)
            # os.system(f"say '{speech}'") # speaks out loud on the computer
    except Exception as e:
        print(e)
        pass

def sentiment(input):
    pass
# def generate(inp):
#     c = f"""  
#         Usr: {inp}
#         Bot:
#     """
#     chat = str(chat) + str(c)
#     print(chat)
#     # gen = co.generate(  model='medium',  prompt = chat,  max_tokens=30,  temperature=0.6,  stop_sequences=["Usr"])
#     # text = gen[0].text.split("Usr",1)
#     # return text[0]
#     return "Hello"