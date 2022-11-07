from apa102_pi.driver import apa102
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

strip = apa102.APA102(num_led=8, order='rgb')
strip.clear_strip()

TRIG=4
ECHO=17
BUZZER=40

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER, GPIO.OUT)

def sr04(trig_pin, echo_pin):
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
    output = sr04(TRIG, ECHO)
    formatted_output = '{:.2f}'.format(output)
    print(formatted_output)
    # print(int(output))
    time.sleep(1)

    if distance<30:
        strip.set_pixel_rgb(1, 0x00FF00)  # Green
        strip.set_pixel_rgb(2, 0x00FF00)  # Green
        strip.set_pixel_rgb(3, 0x00FF00)  # Green
        strip.set_pixel_rgb(4, 0x00FF00)  # Green
        strip.set_pixel_rgb(5, 0x00FF00)  # Green
        strip.set_pixel_rgb(6, 0x00FF00)  # Green
        strip.set_pixel_rgb(7, 0x00FF00)  # Green
        strip.set_pixel_rgb(8, 0x00FF00)  # Green

        strip.show()
        strip.cleanup()
        GPIO.output(BUZZER,GPIO.HIGH)
    else:
        strip.set_pixel_rgb(1, 0xFF0000)  # Red
        strip.set_pixel_rgb(2, 0xFF0000)  # Red
        strip.set_pixel_rgb(3, 0xFF0000)  # Red
        strip.set_pixel_rgb(4, 0xFF0000)  # Red
        strip.set_pixel_rgb(5, 0xFF0000)  # Red
        strip.set_pixel_rgb(6, 0xFF0000)  # Red
        strip.set_pixel_rgb(7, 0xFF0000)  # Red
        strip.set_pixel_rgb(8, 0xFF0000)  # Red

        strip.show()
        strip.cleanup()
        GPIO.output(BUZZER,GPIO.LOW)