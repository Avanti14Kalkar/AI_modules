import os
import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3
engine= pyttsx3.init()

load_dotenv()
genai.configure(api_key= os.getenv('Gemini_api_key'))
model= genai.GenerativeModel('gemini-2.5-flash')
response=model.generate_content(input('Enter the content:'))

#rate
rate=engine.getProperty('rate')
print(rate)
engine.setProperty('rate',125)

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)

print(response.text)                               #print(response.text) -if want in text on terminal
engine.say(response.text)       #pyttsx3.speak(response.text)--applicable but not every library
engine.runAndWait()
