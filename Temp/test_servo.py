#!/bin/python
 
# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
# Importeer de time biblotheek voor tijdfuncties.
from time import sleep
 
# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)
# Zet waarschuwingen uit.
GPIO.setwarnings(False)
 
# Zet de GPIO pin als uitgang.
GPIO.setup(17, GPIO.OUT)
# Configureer de pin voor PWM met een frequentie van 50Hz.
p = GPIO.PWM(17, 50)
# Start PWM op de GPIO pin met een duty-cycle van 6%
p.start(6)
   
def slagboom_open(p):
    p.ChangeDutyCycle(11)
    sleep(5)
    p.ChangeDutyCycle(6)
    
    
slagboom_open(p)