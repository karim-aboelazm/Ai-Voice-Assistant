import webbrowser as web
import time
import keyboard
def whatsapp(number,msg):
    open_chat = "https://web.whatsapp.com/send?photo="+number+"&text="+msg
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')

whatsapp("+20 121 039 3259","If You Need SomeThing Just Call Me .. My Name Is Omar Assistant ....")