import time
import RPi.GPIO as GPIO


def task2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)

    GPIO.output(22, 1)
    time.sleep(1)
    GPIO.output(22, 0)
    time.sleep(1)
    

    GPIO.output(22, 1)
    time.sleep(1)
    GPIO.output(22, 0)
    time.sleep(1)
    
    GPIO.output(22, 1)
    time.sleep(1)
    GPIO.output(22, 0)
    time.sleep(1)
    GPIO.cleanup()

def task3():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.IN)
    while(True):
        time.sleep(0.01)
        print(GPIO.input(23))
        if GPIO.input(23) == 1:
            GPIO.output(22, 1)
        if GPIO.input(23) == 0:
            GPIO.output(22, 0)
    GPIO.cleanup()


task3 ()
