import pyttsx3


engine=pyttsx3.init('sapi5')
voices=engine.getproperty('voices')
print(voices[0].id)
engine.setproperty('voices',voices[0].id)
