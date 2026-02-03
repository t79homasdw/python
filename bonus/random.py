import random

while True:
    try:
        lower = int(input("Enter lower bound: "))
        upper = int(input("Enter upper bound: "))
        if lower == upper:
            print("Lower bound must be less than upper bound.")
        elif lower > upper:
            print("Lower bound must be less than upper bound.")
        else:
            print(f"Random number between {lower} and {upper} is {random.randint(lower, upper)}")
    except ValueError:
        print("Invalid input. Please enter valid integers.\nNote: that the lower bound must be less than the upper bound.")
