from gpiozero import LED
from time import sleep

red = LED(4)
blue = LED(18)
green = LED(27)
red.on()
blue.on()
green.on()
sleep(1)
red.off()
green.off()
blue.off()
