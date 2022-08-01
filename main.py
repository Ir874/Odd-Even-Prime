#!/usr/local/bin/python3
# Importing the time module to allow slight delay
from time import sleep


# Have to put sorting function first to avoid referencing error

def sorter(userin):

    if (userin%2) == 0: # Returns remainder: if its 0, the number is even 
        sleep(0.5)
        print(f"{userin} is an even number")
        sleep(0.5)

    elif (userin%2) > 0: # Returns remainder: if its greater than 0, the number is odd
        sleep(0.5)
        print(f"{userin} is an odd number")
        sleep(0.5)

def primesorter(userin):
    isnotprime = 0
    
    defprime = f"A prime number is a number that can only be divided by 1 and itself. {userin} is not prime because it is divisible by more than 2 numbers. "
    divisible_numbers = []

    for x in range(1,userin):

        if (userin%x) == 0: # Returns remainder of the division. If it is one, then isnotprime is added to. 
            isnotprime += 1
            divisible_numbers.append(x)

    if isnotprime > 2: # If isnotprime reaches more than 1, then the number is not prime
        sleep(0.5)
        print(f"{userin} is not prime.")
        sleep(0.5)
        print(defprime)
        sleep(0.5)
        primeinp = input("Would you like to know these numbers(y/n)? ")
        if primeinp == "y":
            sleep(0.5)
            print(divisible_numbers)
            sleep(0.5)
            print("Goodbye!")
        else: 
            sleep(0.5) 
            print("Goodbye!")
    
    else: print(f"{userin} is prime.")





# Ask user for input
userin = int(input("Input a number to be categorized: "))


# Enter user input into the pre-defined function
sorter(userin)
primesorter(userin)
