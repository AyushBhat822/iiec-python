import subprocess as sp
import speech_recognition as sr
import webbrowser

print("Welcome to my tools\n\n")
print("Say ur requirements:",end='')

r = sr.Recognizer()

with sr.Microphone() as source:
	print('start saying...')
	audio = r.listen(source)
	print("we got it")

sending_api_google = r.recognize_google(audio)

text = sending_api_google

if ("open" in text) and ("notepad" in text):
	sp.getoutput("notepad")

print(text)





