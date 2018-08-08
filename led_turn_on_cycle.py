# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:12:29 2018

@author: USER
"""

import RPi.GPIO as GPIO
import time
  

channel = 16;
  
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel,GPIO.OUT)
    pass

def on(): #turn on led
    GPIO.output(channel,GPIO.HIGH)
 
def off(): #turn off led
    GPIO.output(channel, GPIO.LOW)
    
def test():
    on()
    off()
    time.sleep(1) # how long take a pic (secs)
 
def clean():
    GPIO.cleanup()
    
test()

