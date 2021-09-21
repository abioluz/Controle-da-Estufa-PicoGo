from machine import Pin
import time

led = Pin(25,Pin.OUT)

# led.value(1)

while True:
    for i in range(12):
        led.toggle()
        time.sleep(0.5)
    for i in range(6):
        led.toggle()
        time.sleep(3)
    