from machine import Pin, PWM

relayA = PWM(Pin(14))
relayA.freq(200)

while True:
    brightness_str = input("brightness (0-100):")
    brightness = int(brightness_str)
    if brightness < 0 or brightness > 100:
        print("Brightness between 0 and 100")
    else:
        duty = int(brightness * 655.35)
        relayA.duty_u16(duty)
    

