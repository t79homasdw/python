import random

while True:
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    try:
        print(f"Random number between {lower} and {upper} is {random.randint(lower, upper)}")
    except ValueError:
        print("Invalid input. Please enter valid integers.\n  Note: that the lower bound must be less than the upper bound.")
