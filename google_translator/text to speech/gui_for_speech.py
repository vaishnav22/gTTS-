from tkinter import *
#import text_to_speech
from gtts import gTTS
import os

def voice():
    userInput = textEntry.get()
    language = 'en'
    myobj = gTTS(text=userInput, lang=language, slow=False)
    myobj.save("/home/vaishnav/Desktop/pycharm/google_translator/welcome.mp3")
    os.system("mpg321 welcome.mp3")

########################################################################################


win = Tk()
win.title('WeSay')
win.geometry("300x200")


text = Label(win, text = 'Enter the text')
text.grid(row=0)

textEntry =  Entry(win)
textEntry.grid(row=0,column=1)

button_1 = Button(win,text = 'Submit',command=voice)
button_1.grid(columnspan=2)

win.mainloop()