import RGB1602
import utime
from machine import Pin

button_1 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(10, Pin.IN, Pin.PULL_DOWN)

lcd = RGB1602.RGB1602(16, 2)
rgb = (0, 128, 60)
dangerRgb = (255, 0, 0)

count = 0

# Default screen color
lcd.setRGB(rgb[0], rgb[1], rgb[2])
lcd.setCursor(0, 0)
lcd.printout(count)

while True:

    # Add Button
    if button_1.value() == 1:
        count = count + 1
        utime.sleep(0.3)
        lcd.clear()
        lcd.printout(count)

    # Reset button
    if button_2.value() == 1:
        count = 0
        lcd.clear()

        # Momentary red screen color for visual feedback
        lcd.setRGB(dangerRgb[0], dangerRgb[1], dangerRgb[2])
        lcd.printout("Reset")

        # Wait 1 sec and clear screen
        utime.sleep(1)
        lcd.clear()

        # Default screen color
        lcd.setRGB(rgb[0], rgb[1], rgb[2])
        lcd.printout(count)
