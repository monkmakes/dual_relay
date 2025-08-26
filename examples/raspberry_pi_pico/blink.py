from machine import Pin
from time import sleep

relayA = Pin(17, Pin.OUT)
relayB = Pin(16, Pin.OUT)

while True:
    relayA.on()
    relayB.off()
    sleep(0.5) # pause
    relayA.off()
    relayB.on()
    sleep(0.5)
    
