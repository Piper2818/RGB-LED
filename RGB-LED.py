#Assignment 3 - Python Template
#Student Name: Piper Morris
#Hint: Read the function __main__ before implementation
# 2/25/23

"""Write a single python statement to import
the appropriate library to control the GPIO Pins"""

import RPi.GPIO as GPIO

"""Write a single python statement to import
the sleep function from the time module"""

from time import sleep

"""Complete the function body to setup
three GPIO pins as Output pins.The parameter pins is a
list containing the pin numbers"""

def setup_pins(pins):
    #Write a single Python statement to setup the pins as output pins
    GPIO.setup(pins,GPIO.OUT)
   
   
"""Complete the function body to set the
three GPIO pins to LOW state, and cleanup
the GPIO"""
def reset_GPIO(pins):
    #Write a single Python statement to set the three GPIO Pins to LOW State
    GPIO.output(pins,GPIO.LOW)
   
    #Write a single Python statement to clean up the GPIO Pins
    GPIO.cleanup()
     
"""Complete the function body to generate eight different colors"""
#parameter state_time is the time for which a color is displayed
#parameter truth_table is a dictionary containing 3-bit Truth Table
def generate_colors(pins,truth_table,state_time):
    """ we want to iterate through the dictionary but we can't use .values() because then we are setting i equal to the values being stored in
        the dictionary and we can use a list as an index to get when we set the color in line 45"""
    for i in truth_table:
       
        """Write a single python statement to set the color of the
        RGB LED according to the value or state of the truth table """
        GPIO.output(pins, truth_table[i])
       
        """ in line 45 we are useing the list of pins and the list of values to set the color. Each pin in the list corresponds to a color RGB
        and each value in the list being pulled from the dictionary is either a 1 or a 0 for true to false. So we are setting each color equal
        to either true or false (on or off) for a total of 8 combinations"""
       
        #Write a single python statement to sleep for the desired color time
        # we want to take in the amount of time to sleep for because we are going to pass this function a user input later when we call it
        sleep(state_time)

#Implementation
if __name__ == '__main__':
    #Write a single python statement to set the pin access mode, broadcome mode
    GPIO.setmode(GPIO.BCM)
     
    #Write a single python statement to create a list of the GPIO pins
    # This will be the arguement that gets plugged in for the parameter pins, when invoking the functions above
    Pin_nums = [17,18,27]
   
    #Write a single python statement to call or invoke the function setup_pins
    setup_pins(Pin_nums)
   
    #Write python statements to create a dictionary to create a 3-bit truth table
    """ This will be the arguement that gets plugged in for the parameter truth_table, when invoking generate_colors. Each value being stored
    in this dictionary is a binary number corresponding to the row it's in starting with 0 in row 1. For binary numbers less then 3 digits,
    0's serve as place holders to the left of it. So 1 is 001"""
    Table = {'1': [0,0,0],
            '2': [0,0,1],
            '3': [0,1,0],
            '4': [0,1,1],
            '5': [1,0,0],
            '6': [1,0,1],
            '7': [1,1,0],
            '8': [1,1,1]}
   
    try:
        """Write a python statement to obtain the desired time
        for which a color has to be displayed from the user.
        Store the desired time in an variable named color_time of
        appropriate data type"""
        # this is the agruement corresponding to the parameter state_time
        color_time = float(input('Please input how long your want the colors to display for: ' ))
       
        """Write a single python statement to call/invoke the
        function generate_colors"""
        generate_colors(Pin_nums,Table,color_time)
       
        #Write a single python statement to call the function reset_GPIO
        reset_GPIO(Pin_nums)
       
    except KeyboardInterrupt:
        #Write a single python statement to call the function reset_GPIO
        reset_GPIO(Pin_nums)
