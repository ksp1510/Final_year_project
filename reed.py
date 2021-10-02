import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def reed_status():
    GPIO.setup(15,GPIO.IN)
    if GPIO.input(15) is 0:
        #GPIO.cleanup()
        return 1
    else:
        return 0
    
#while True:
    #print(reed_status())