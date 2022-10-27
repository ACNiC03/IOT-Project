from wsgiref.util import request_uri
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep




def NFC_aanmaken():
    reader = SimpleMFRC522()
    try:
            print("Now place your tag to write")
            lezer = reader.read()
            lezer = str(lezer)
            aanpassing = lezer.split(",")[0]
            aanpassing = aanpassing.strip("(")
            f = open("key.txt","a")
            f.write(f"{aanpassing}\n")
            print("Written")
            f.close
    finally:
            GPIO.cleanup()
            
#NFC_aanmaken()

def NFC_lezen():
    reader = SimpleMFRC522()
    try:
            print("Plaats de NFC-Kaart voor de lezer")
            id= reader.read()
            lezer = str(id)
            aanpassing = lezer.split(",")[0]
            aanpassing = aanpassing.strip("(")
    finally:
            GPIO.cleanup()
    return aanpassing
#NFC_lezen()

def slagboom_open():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    p = GPIO.PWM(17, 50)
    p.start(6)
    p.ChangeDutyCycle(11)
    sleep(5)
    p.ChangeDutyCycle(6)
    sleep(1)




def main():
    lezer = NFC_lezen()
    f = open("key.txt","r")
    for i in f:
        if lezer in i:
           slagboom_open()
    f.close
    
main()