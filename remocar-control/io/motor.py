'''
 Copyright (C) 2018 Robert Hansel
 All rights reserved.
 
 This software may be modified and distributed under the terms
 of the BSD license.  See the LICENSE file for details.
'''
import RPi.GPIO as GPIO
from time import sleep

in1 = 8
in2 = 7
in3 = 24
in4 = 23
enA = 12
enB = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
engine=GPIO.PWM(enB,10000)
engine.start(100)
steering=GPIO.PWM(enA,10000)
steering.start(100)
print("\n")
print("The default speed & direction of motor is Top & Forward.....")
print("d-drive h-halt f-forward b-backward s-slow m-medium t-top l-left r-right a-ahead e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='d':
        print("drive")
        if(temp1==1):
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'

    elif x=='l':
        print("left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='r':
        print("right")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        x='z'

    elif x=='a':
        print("ahead")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='h':
        print("halt")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='s':
        print("slow")
        engine.ChangeDutyCycle(80)
        x='z'

    elif x=='m':
        print("medium")
        engine.ChangeDutyCycle(90)
        x='z'

    elif x=='t':
        print("top")
        engine.ChangeDutyCycle(100)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        