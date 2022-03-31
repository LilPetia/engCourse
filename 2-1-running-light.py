import time
import RPi.GPIO as GPIO

leds = [21, 20, 16, 12, 7, 8, 25, 24]
def task1():
    GPIO.setmode(GPIO.BCM)

    for led in leds:
        GPIO.setup(led, GPIO.OUT)
    for cycle in range(3):
        for led in leds:
            GPIO.output(led, 1)
            time.sleep(0.3)
            GPIO.output(led, 0)
    for led in leds: GPIO.output(led, 0)
     
    GPIO.cleanup()

task1()