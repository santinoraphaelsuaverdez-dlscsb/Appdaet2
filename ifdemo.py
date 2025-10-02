#if Demo sample code
# Author: Raphael Suaverdez
#Version 1.9
#Date 2-October-2025

name = input( "What is your name? ")
age = int(input("How old are you? "))

print (f"Welcome {name}!")
if age >= 18:
    print("You are of legal age.")
else:
    print("You are still a minor.")