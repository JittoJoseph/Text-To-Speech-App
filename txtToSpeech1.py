from gtts import gTTS
import os
from playsound import playsound

# Delete the existing voice.mp3 file if it exists
if os.path.exists("voice.mp3"):
    os.remove("voice.mp3")

# Read the text from the file

file = open("abc.txt", "r").read()

# Generate speech
speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")

# Play the generated speech using playsound
playsound("voice.mp3")
