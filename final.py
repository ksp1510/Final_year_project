import ir
import reed
import rfid
import unotopi
import ex_hx711
import voice
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
#voice.play(0)
flag=0
print("Human presence detected and confirmed")
voice.play(1)
voice.play(2)

'''and (30<unotopi.getTemp()<39)'''
i=0
while (2<ex_hx711.getWeight()<5) and flag==0:
    i+=1
    
    if reed.reed_status() == 0:
        print("Seat Belt not buckled")
        voice.play(2)
        

    else:
        if ir.ir() == 1:
            print("Seat Belt buckled but from behind the seat")
            voice.play(4)
            

        else:
            if i!= 8:
                print("Seat Belt buckled but from between driver's back and seat")
                voice.play(3)
                

            else:
                print("Seat Belt buckled properly so can start the engine")
                voice.play(5)
                flag=1
                GPIO.output(20,GPIO.LOW)
                
                
while (2<ex_hx711.getWeight()<5) and flag==1:
    
    
    if reed.reed_status() == 0:
        print("Seat Belt removed in mid journey")
        voice.play(6)
        

    