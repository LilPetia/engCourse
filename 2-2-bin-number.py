import time
import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
#number = [i % 2 for i in dac] 
number = [0,0,0,0,0,0,0,1]

number = [1,1,1,0,1,1,1,1]
GPIO.setmode(GPIO.BCM)
def bin2dec(): 
    sum = 0
    for i in range(len(number)) : sum += 2**(7-i) * number[i]
    return sum 
def  task2():
    print(bin2dec() * 1.3)
    for pin in dac: GPIO.setup(pin, GPIO.OUT)
    for pin, mode in zip(dac, number): GPIO.output(pin, mode)
    time.sleep(10)
    for pin in dac: GPIO.output(pin, 0)
    GPIO.cleanup()
    pass
task2()