"""
___2026/07/18___

___CHALLENGE___
Temperature Converter: Create a function to convert Celsius to Fahrenheit and vice versa

___TAKEAWAY_AFTER_COMPLETION___
Honestly... I'm very tired today, and intentonally picked an easy challenge;
even so I still miss scoped me variables initally, and had to take a step back.
We got there in the end! I'll do something more challenging tommorow.
"""


def fahrenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


print(fahrenheit_to_celsius(32))
print(celsius_to_fahrenheit(32))