import speech_recognition as sr
import os
from voice_input import Listen
from Assistant import main_function
while True:
    wake_up = Listen()
    if 'wake up' in wake_up:
        os.startfile('E:\\OI_GP\\Project\\src\\Assistant.py')
    elif wake_up == None:
        os.startfile('E:\\OI_GP\\Project\\src\\Assistant.py')
    else:
        print("Nothing...")