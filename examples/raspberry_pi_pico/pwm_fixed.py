from machine import Pin, PWM

relayA = PWM(Pin(17))
relayA.freq(100)

relayA.duty_u16(15000)

    

