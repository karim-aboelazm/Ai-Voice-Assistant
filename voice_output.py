import pyttsx3 as pytts

def say(text):
    engine = pytts.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[4].id)
    engine.setProperty('rate',180)
    print(f'Omar : {text}\n')
    engine.say(text=text)
    engine.runAndWait()

