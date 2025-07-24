# import pyttsx3
# text="SITAMRHI INSTITUTE OF TECHNOLOGY"
# output_file="audio.mp3"
# engine=pyttsx3.init()
# voices =engine.getProperty("voices")
# #engine.setProperty("voice",voices[0].id)
# engine.setProperty("voice",voices[1].id)

# engine.setProperty("rate",150)
# engine.save_to_file(text=text,filename=output_file)
# engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if 'hindi' in voice.name.lower() or 'india' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
else:
    
    engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 145)

text = input("Enter the text you want to speak: ")

engine.say(text)
engine.runAndWait()