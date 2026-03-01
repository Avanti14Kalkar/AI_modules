import pyttsx3
engine = pyttsx3.init() # object creation

a=input('Enter a text to speak: ')
pyttsx3.speak(a)

engine.save_to_file(a, 'test.mp3')
engine.runAndWait()