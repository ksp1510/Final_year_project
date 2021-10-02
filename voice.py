from gtts import gTTS
import os

'''s0="Hello everyone, I am Kishan Patel and these are my team-mates Nitya Patel, Nishil Patel and Rutvik Patel, and our guide is Dr. Harshal Shah. We are here to present our project, that is Ignition Interlocking Seat Belt. This system makes sure that the seat belt is properly worn before driver can start the engine. It compiles the user to wear seat belt regularly and also properly."
s1="Welcome Sir"
s2="Before starting the engine please wear the seat belt for your safety."
s3="Please wear seat belt properly over your body and not behind your back, it is for your own safety."
s4="Please put seat belt from the front, this will ensure your safety."
s5="Now you can start the engine and have a safe journey."
s6="Do not remove your seat belt please keep the belt buckled for your safety."
tts=gTTS(s0,lang='en', slow=False)
tts.save("t0.mp3")
tts=gTTS(s1,lang='en', slow=True)
tts.save("t1.mp3")
tts=gTTS(s2,lang='en', slow=False)
tts.save("t2.mp3")
tts=gTTS(s3,lang='en', slow=False)
tts.save("t3.mp3")
tts=gTTS(s4,lang='en', slow=False)
tts.save("t4.mp3")
tts=gTTS(s5,lang='en', slow=False)
tts.save("t5.mp3")
tts=gTTS(s6,lang='en', slow=False)
tts.save("t6.mp3")'''

def play(choice):
    if choice is 0:
        os.system("mpg123 t0.mp3")
        os.system("clear")
    elif choice is 1:
        os.system("mpg123 t1.mp3")
        os.system("clear")
    elif choice is 2:
        os.system("mpg123 t2.mp3")
        os.system("clear")
    elif choice is 3:
        os.system("mpg123 t3.mp3")
        os.system("clear")
    elif choice is 4:
        os.system("mpg123 t4.mp3")
        os.system("clear")
    elif choice is 5:
        os.system("mpg123 t5.mp3")
        os.system("clear")
    elif choice is 6:
        os.system("mpg123 t6.mp3")
        os.system("clear")
    return 0

#play(1)
