import time
import RPi.GPIO as GPIO

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
def task3(): 
    GPIO.setmode(GPIO.BCM)

    for led, pin in zip(leds, aux):
        GPIO.setup(led, GPIO.OUT)
        GPIO.setup(pin, GPIO.IN)
    try:
        while(True):
            for led, pin in zip(leds, aux):
                GPIO.output(led, GPIO.input(pin))
            time.sleep(0.1)
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()
task3()