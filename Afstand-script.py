import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("sr04 print")

sr04_trig = 20
sr04_echo = 21

GPIO.setup(sr04_trig, GPIO.OUT)
GPIO.setup(sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def sr04(trig_pin, echo_pin):
    """
    Return the distance in cm as measured by an SR04
    that is connected to the trig_pin and the echo_pin.
    These pins must have been configured as output and input.s
    """
    GPIO.output(trig_pin, True)
    time.sleep(0.1)
    GPIO.output(trig_pin, False)

    begintime = 0
    endingtime = 0

    while GPIO.input(echo_pin) == 0:
        begintime = time.time()

    while GPIO.input(echo_pin) == 1:
        endingtime = time.time()

    diff = endingtime - begintime
    dist = (diff * 34300) / 2

    return dist


while True:
    output = sr04(sr04_trig, sr04_echo)
    formatted_output = '{:.2f}'.format(output)
    print(formatted_output)
    # print(int(output))
    time.sleep(1)