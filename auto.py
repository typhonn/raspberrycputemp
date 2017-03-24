import RPi.GPIO as GPIO
import os

def on():
    GPIO.output(17, True)

def off():
    GPIO.output(17, False)

def getCpuT():
 tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
 cpu_temp = tempFile.read()
 tempFile.close()
 return int(cpu_temp)/1000


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    if getCpuT() >= 37:
        on()
        exit()
    elif getCpuT() < 37:
        off()
    else:
        exit()
