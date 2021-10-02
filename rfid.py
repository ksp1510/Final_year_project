import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import time
reader=SimpleMFRC522()

def find_tag():
    time.sleep(1.5)
    tag, text = reader.read_no_block()
    if tag is None:
        #print("No tag detected")
        return 0
    else:
        #print("Tag detected")
        #print(tag)
        return 1
#while True:
#    print(find_tag())