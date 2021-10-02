import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN)

def ir():
    v=GPIO.input(18)
    time.sleep(3)
    return v
