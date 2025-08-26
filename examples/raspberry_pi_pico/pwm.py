from machine import Pin, PWM

relayA = PWM(Pin(17))
relayA.freq(200)

while True:
    brightness_str = input("brightness (0-100):")
    brightness = int(int(brightness_str) * 655.36)
    relayA.duty_u16(brightness)
    
