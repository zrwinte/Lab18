#Useful Links!
#https://pinout.xyz
#https://gpiozero.readthedocs.io/en/stable/recipes.html#button

#Created by Zach Winters, TEC 284 Quiz 2
#Importing the required libraries
#from gpiozero import Button, LED
from gpiozero import Button, RGBLED
from time import sleep

# Setting up the GPIO pins
red_button = Button(17)
green_button = Button(27)
blue_button = Button(22)

rgb_led = RGBLED(red=23, green=24, blue=25)

# Creating my function to check button states to ensure colors display/mix accordingly!
def check_buttons():
    red = red_button.is_pressed
    green = green_button.is_pressed
    blue = blue_button.is_pressed
    
    if red and not green and not blue:
        print("The Red Button has been pressed!")
        rgb_led.color = (1, 0, 0)  
    elif green and not red and not blue:
        print("The Green Button has been pressed!")
        rgb_led.color = (0, 1, 0)  
    elif blue and not red and not green:
        print("The Blue Button has been pressed!")
        rgb_led.color = (0, 0, 1)  
    elif red and green and not blue:
        print("Red and Green Make Yellow!")
        rgb_led.color = (1, 1, 0)  
    elif red and blue and not green:
        print("Red and Blue Make Magenta!")
        rgb_led.color = (1, 0, 1)  # 
    elif green and blue and not red:
        print("Green and Blue Make Cyan")
        rgb_led.color = (0, 1, 1)  
    elif red and green and blue:
        print("All Colors Combined Make White!")
        rgb_led.color = (1, 1, 1)  
    else:
        # No buttons pressed
        rgb_led.color = (0, 0, 0)

#Main loop, ensuring button states are continously checked rather than once!

while True:
        check_buttons()
        sleep(0.1)  


