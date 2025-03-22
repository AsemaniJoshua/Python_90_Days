from gtts import gTTS
from playsound import playsound

text = input("Enter the text: ")
tts = gTTS(text=text, lang="en")
tts.save("output.mp3")
playsound("output.mp3")
