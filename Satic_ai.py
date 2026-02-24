
import pyttsx3
engine = pyttsx3.init()       # or engine= pyttsx3.init('sapi5') - defines default speach engine of windows OS
engine.setProperty('rate',160)
engine.setProperty('volume',1)

while True:
    ask=input('Ask the question: ').strip().lower()
    if ask in ['hello','hi']:
        response='Hello Avanti, How can I help you today?'

    elif 'tell about doxpro robotics' in ask:
        response=('DoxPro Robotics Pvt. Ltd. is a technical training and project-solution organization that works with engineering students and professionals.')

    elif 'tell about internship' in ask:
        response=('They offer internship programs in areas like Artificial Intelligence (AI), Embedded Systems, and Robotics — subjects that are useful for engineering students and tech learners.')
        link='https://www.doxprorobotics.in/'

        engine.stop()
        engine.say('Here is the link')
        print("Apply here: ")
        print(link)
        engine.runAndWait()

    elif 'thank you' in ask:
        response=('Your Welcome! If you need some help, Just ask!')

    elif 'exit' in ask:
        response=('Okay.. \nGood Bye. See you again')
        print(response)
        engine.stop()
        engine.say(response)
        engine.runAndWait()
        break

    else:
        response="Sorry! I don't understand that"
        print(response)
        engine.stop()
        engine.say(response)
        engine.runAndWait()
        continue
    
    print(response)

    engine.stop()
    engine.say(response)
    engine.runAndWait()