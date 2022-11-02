import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 20
ECHO = 21

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


try:
    while True:

        GPIO.output(TRIG, False)
        time.sleep(0.05)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = (pulse_duration / 2) * 34300
        distance = round(distance)

        print ("Distance: ",distance,"cm")

        if distance < 7:
            print ("STOP")



except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
    print("Cleaning up!")

