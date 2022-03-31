import time
import RPi.GPIO as GPIO


def task2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)
