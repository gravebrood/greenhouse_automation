#!/usr/bin/env python


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print GPIO.input(3)
