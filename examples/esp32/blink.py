from machine import Pin
from time import sleep

relayA = Pin(14, Pin.OUT)
relayB = Pin(12, Pin.OUT)

while True:
    relayA.on()
    relayB.off()
    sleep(0.5) # pause
    relayA.off()
    relayB.on()
    sleep(0.5)
