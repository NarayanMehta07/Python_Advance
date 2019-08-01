import gtts
import os
import string

t=input('Hi friend how are you...Write something\n')
new_str = t.replace('Hi friend how are you...Write something', 'You Said')
print(new_str)

tts = gtts.tts.gTTS(text=new_str, lang='en')
tts.save("D:\\hello.mp3")
