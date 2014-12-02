import numpy as np
import RPi.GPIO as GPIO
import time
ADDR_0 = 25
ADDR_1 = 24
ADDR_2 = 23
ADDR_3 = 18
D_G = 17
D_R = 22
CLK = 10
WE = 9
ALE = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(ADDR_0,GPIO.OUT)
GPIO.setup(ADDR_1,GPIO.OUT)
GPIO.setup(ADDR_2,GPIO.OUT)
GPIO.setup(ADDR_3,GPIO.OUT)
GPIO.setup(D_G,GPIO.OUT)
GPIO.setup(D_R,GPIO.OUT)
GPIO.setup(CLK,GPIO.OUT)
GPIO.setup(WE,GPIO.OUT)
GPIO.setup(ALE,GPIO.OUT)
data_r = 0b1010101010101010101010101010101010101010101010101010101010101010
data_rrr = 0b01010101010101010101010101010101
data_rr = 0b11111111111111111111111111111111
#data_g = 0b0000000000000000000000000000000010000000000000000000000000000000
data_g = 0b0101010101010101010101010101010101010101010101010101010101010101

arr_g = np.array([[data_g],[data_r],[data_g],[data_r],
                 [data_g],[data_r],[data_g],[data_r],
                 [data_g],[data_r],[data_g],[data_r],
                 [data_g],[data_r],[data_g],[data_r]])

arr_r = np.array([[data_r],[data_r],[data_r],[data_r],
                 [data_r],[data_r],[data_r],[data_r],
                 [data_r],[data_r],[data_r],[data_r],
                 [data_r],[data_r],[data_r],[data_r]])
               

GPIO.output(CLK,False)
GPIO.output(WE,False)
GPIO.output(ALE,False)
GPIO.output(ADDR_0,False)
GPIO.output(ADDR_1,False)
GPIO.output(ADDR_2,False)
GPIO.output(ADDR_3,False)

def setram(arr_g, arr_r):
    GPIO.output(CLK,False)
    for j in range(16):
        data_r = arr_r[j]
        data_g = arr_g[j]
        for i in range(64):
            if data_r >> i & 1:
                GPIO.output(D_R,True)
            else:
                GPIO.output(D_R,False)
            if data_g >> i & 1:
                GPIO.output(D_G,True)
            else:
                GPIO.output(D_G,False)
            GPIO.output(CLK,True)
            GPIO.output(CLK,False)
        chk0 = j & 1
        chk1 = (j >> 1) & 1
        chk2 = (j >> 2) & 1
        chk3 = (j >> 3) & 1
        GPIO.output(ALE,True)
        if chk0 ==1:
            GPIO.output(ADDR_0,True)
        else:
            GPIO.output(ADDR_0,False)
        if chk1 ==1:
            GPIO.output(ADDR_1,True)
        else:
            GPIO.output(ADDR_1,False)
        if chk2 ==1:
            GPIO.output(ADDR_2,True)
        else:
            GPIO.output(ADDR_2,False)
        if chk3 ==1:
            GPIO.output(ADDR_3,True)
        else:
            GPIO.output(ADDR_3,False)
        GPIO.output(WE,True)
        GPIO.output(WE,False)
        GPIO.output(ALE,False)
#    time.sleep(0.01)

for x in range(100):
    setram(arr_g, arr_r)

GPIO.cleanup()
