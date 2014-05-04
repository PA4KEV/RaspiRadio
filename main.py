'''
Created on May 4, 2014

@author: Kevin
'''
from time import sleep
from subprocess import call
from subprocess import check_output
import RPi.GPIO as GPIO 

LCD_RS = 7
LCD_E = 5
LCD_D4 = 25
LCD_D5 = 23
LCD_D6 = 24
LCD_D7 = 18
LED_GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

def setPins(d4 = False, d5 = False, d6 = False, d7 = False):
    GPIO.output(LCD_D4, d4)
    GPIO.output(LCD_D5, d5)
    GPIO.output(LCD_D6, d6)
    GPIO.output(LCD_D7, d7)
    
def lcd_write(byte, rs):    
    GPIO.output(LCD_RS, rs)
    
    # High Nibble
    setPins()    
    GPIO.output(LCD_D4, (byte & 0x80 == 0x80))
    GPIO.output(LCD_D5, (byte & 0x40 == 0x40))
    GPIO.output(LCD_D6, (byte & 0x20 == 0x20))
    GPIO.output(LCD_D7, (byte & 0x10 == 0x10))    
    sleep(0.1)
    GPIO.output(LCD_E, True)
    sleep(0.1)
    GPIO.output(LCD_E, False)
    sleep(0.1)
    
    # Low Nibble
    setPins()
    GPIO.output(LCD_D4, (byte & 0x08 == 0x08))
    GPIO.output(LCD_D5, (byte & 0x04 == 0x04))
    GPIO.output(LCD_D6, (byte & 0x02 == 0x02))
    GPIO.output(LCD_D7, (byte & 0x01 == 0x01))
    sleep(0.1)
    GPIO.output(LCD_E, True)
    sleep(0.1)
    GPIO.output(LCD_E, False)
    sleep(0.1)
    
    
if __name__ == '__main__':
    i = 0
    LedGreen = 0
    sleep(1)
    call(["mpc", "play"])
    lcd_write(0x0F, False)
    while (i < 20):        
        output = (check_output(["mpc"]))
        arr = (output[10:output.find("[Rainwave Game]")]).split(" - ")
        print(arr[1])
        sleep(1)
        i += 1
        LedGreen = LedGreen ^ 1
        GPIO.output(22, LedGreen)
    GPIO.output(22, 0)
    call(["mpc", "stop"])
    GPIO.cleanup()