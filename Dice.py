import time
import random
from gpiozero import LED, Button

# Define GPIO pins
led0 = LED(23)
led1 = LED(4)
led2 = LED(25)
led3 = LED(10)
led4 = LED(17)
led5 = LED(8)
led6 = LED(22)  # Adjust pin numbers if needed
pushButton = Button(7)  # Adjust pin number if needed

def main():
    try:
        while True: #Always run the underlying code...
            number = generateNumber() #generate a random number
            displayNumber(number) #display that number
    except KeyboardInterrupt: #... unless you exit with CTRL+C
        print("\nExiting program.")

def generateNumber():  # Wait for a push, return random die value
    throw = random.randint(1, 6)
    print("Press the button to roll the dice.")
    
    pushButton.wait_for_press()  # Wait for button press
    time.sleep(0.030)  # Debounce delay
    
    while pushButton.is_pressed: #Cycles through 1-6
        throw += 1
        if throw > 6:  # Wrap round the number
            throw = 1
    
    print(f"Dice rolled: {throw}")
    return throw

def displayNumber(number):

    ledsOff()
    
    #This is an example of how to turn on LEDs for a specific number
    if number == 1:
        led0.off()
        led1.off()
        led2.off()
        led3.on()
        led4.off()
        led5.off()
        led6.off()
    
    
    
    if number == 2:
        led0.off()
        led1.on()
        led2.off()
        led3.off()
        led4.off()
        led5.on()
        led6.off()
        
    
    
    
    if number == 3: 
        led0.off()
        led1.on()
        led2.off()
        led3.on()
        led4.off()
        led5.on()
        led6.off()
        
    
   
    
    
    if number == 4:
        led0.on()
        led1.on()
        led2.off()
        led3.off()
        led4.off()
        led5.on()
        led6.on()
        
    
    
    
    
    if number == 5:
        led0.on()
        led1.on()
        led2.off()
        led3.on()
        led4.off()
        led5.on()
        led6.on()
        
    
   
    
    
    if number == 6:
        led0.on()
        led1.on()
        led2.on()
        led3.off()
        led4.on()
        led5.on()
        led6.on()
        
    time.sleep(1)
    
    ledsOff()

def ledsOff():
    #Turn off all LEDs.
    led0.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    

if __name__ == "__main__":
    main()
