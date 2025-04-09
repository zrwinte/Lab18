#Useful Links!
#https://pinout.xyz
#https://gpiozero.readthedocs.io/en/stable/recipes.html#button

#Created by Zach Winters, TEC 284 Quiz 2
#Importing the required libraries
from gpiozero import Button, LED
from time import sleep

# Setting up the GPIO pins
red_button = Button(17)
green_button = Button(27)
blue_button = Button(22)

red_led = LED(23)
green_led = LED(24)
blue_led = LED(25)

# Creating my function to check button states to ensure colors display/mix accordingly!
def check_buttons():
    red = red_button.is_pressed
    green = green_button.is_pressed
    blue = blue_button.is_pressed

    if red and not green and not blue:
        print("The Red Button has been pressed!")
        red_led.on()
        green_led.off()
        blue_led.off()

    if green and not red and not blue:
        print("The Green Button has been pressed!")
        green_led.on()
        red_led.off()
        blue_led.off()

    if blue and not red and not green:
        print("The Blue Button has been pressed!")
        blue_led.on()
        red_led.off()
        green_led.off()

    if red and green and not blue:
        print("Red and Green Make Yellow!")
        red_led.on()
        green_led.on()
        blue_led.off()

    if red and blue and not green:
        print("Red and Blue Make Magenta!")
        red_led.on()
        blue_led.on()
        green_led.off()

    if green and blue and not red:
        print("Green and Blue Make Cyan")
        green_led.on()
        blue_led.on()
        red_led.off()

    if red and green and blue:
        print("All Colors Combined Make White!")
        red_led.on()
        green_led.on()
        blue_led.on()

    if not red and not green and not blue:
        red_led.off()
        green_led.off()
        blue_led.off()

# Main loop, ensuring button states are continously checked rather than once!
while True:
    check_buttons()
    sleep(0.1)
