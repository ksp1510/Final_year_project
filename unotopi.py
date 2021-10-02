'''This module is created to get sensor data reading from Arduino Uno to Raspberry Pi through serial data transfer'''
import serial
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

def getTemp():

    read_ser=ser.readline()
    s=float(read_ser.decode('UTF-8','strict'))
    #print(s)
    return s
    
