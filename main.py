from wsgiref.util import request_uri
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import SQLScript as SQL

db = SQL.Database("ahmetnicanci.ddns.net", "iot", "admin", "Studentje1")

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
            id= reader.read() #Leest de NFC kaart uit
            lezer = str(id) #verandert de output naar een string
            aanpassing = lezer.split(",")[0] #Stript de overbodige data
            aanpassing = aanpassing.strip("(")
            aanpassing = int(aanpassing)
    finally:
            GPIO.cleanup() #sluit de GPIO pins
    return aanpassing #Geeft resulaat terug

#NFC_lezen()

def slagboom_open():
    GPIO.setmode(GPIO.BCM) #GPIO Mode
    GPIO.setwarnings(False) 
    GPIO.setup(17, GPIO.OUT) #selecteerd pin 17 als een out pin
    p = GPIO.PWM(17, 50) 
    p.start(6)
    p.ChangeDutyCycle(11) #zet de slagboom 90 graden omhoog
    sleep(5) # wacht voor 5 seconden
    p.ChangeDutyCycle(6) #Slagboom word weer naar beneden gezet
    sleep(1)
    GPIO.cleanup() #GPIO pin word weer opgeschoond

def beweging():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    PIR_PIN = 21
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    if GPIO.input(PIR_PIN):
        main()
    else:
        print("Geen beweging")
    GPIO.cleanup()


def main():
    lezer = NFC_lezen()
    f = open("key.txt","r")
    ids = db.select("rfid.rfidid", "RFID")
    lijst1=[]
    for l1 in ids:
        lijst1.append(l1[0])

    for i in lijst1:
        if lezer == i:
           slagboom_open()
           print("open")
    f.close

while True:
    beweging()
    sleep(0.5)

