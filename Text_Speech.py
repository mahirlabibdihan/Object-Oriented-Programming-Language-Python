from win32com.client import Dispatch

def speak(text):
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(text)


while 1:
	Text=input(" : ")
	speak(Text)