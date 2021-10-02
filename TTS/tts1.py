from gtts import gTTS
import time
#import os
import pygame
stime=time.time()
tts=gTTS('how are you',lang='en')
#tts.write_to_fp(mp3_fp)
t="t.mp3"
tts.save(t)
#os.system("mpg123 t.mp3")
#os.system("clear")

pygame.mixer.init()
pygame.mixer.music.load(t)
pygame.mixer.music.play()
print("time of execution: ", time.time()-stime)