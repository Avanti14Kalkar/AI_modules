import os
import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3
engine= pyttsx3.init()

load_dotenv()
genai.configure(api_key= os.getenv("Gemini_api_key"))
model= genai.GenerativeModel('gemini-2.5-flash')
ask=input('Ask about Plant: ')
response=model.generate_content(ask)

while True:
    
    if 'plant' not in ask:
        engine.stop()
        engine.say("Sorry! I have not information of that.")
        engine.runAndWait()
        continue

    engine.stop()
    print(response.text)
    engine.say(response.text)
    engine.runAndWait()