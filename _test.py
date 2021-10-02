import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import sys
import ex_hx711
import ir_test
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
#GPIO.setup(15,GPIO.IN)

def find_tag():
    reader=SimpleMFRC522()
    tag, text = reader.read_no_block()
    if tag is None:
        #print("No tag found")
        return 1
    else:
        #print("Tag Found")
        #print(tag)
        return 0
        
        
def reed_status():
    GPIO.setup(15,GPIO.IN)
    if GPIO.input(15) is 0:
        #GPIO.cleanup()
        return 1
    else:
        return 0



while True:#use ex_hx711.getWeight() 
    try:
    #reed_status()
        
        if reed_status() is 1:
            if find_tag() is 1:
                if ir_test.ir() is 0:
                    print("You may start the engine")
                    GPIO.output(21,GPIO.HIGH)
                    time.sleep(5)
                    GPIO.output(21,GPIO.LOW)
            
            else:
                print("Put belt properly from the front")
                time.sleep(3)
        
        else:
            print("Put on the belt")
            time.sleep(3)
            
    except (KeyboardInterrupt, SystemExit):
        print("Bye")
        sys.exit()