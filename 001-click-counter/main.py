import machine
import utime

button_1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_2 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0

while True:

    if button_1.value() == 1:
        count = count + 1
        utime.sleep(0.5)
        print("Counter: ", count)

    if button_2.value() == 1:
        count = 0
        utime.sleep(0.5)
        print("--Reset--\nCounter: ", count)
