from experiments.converters14 import convert
from experiments.parsers14 import parse

feet_inches = input("Enter feet and inches: ")

f, i = parse(feet_inches)
print("fi",f, i)
result = convert(f, i)

if result < 1:
    print("You are too short to ride the roller coaster.")
else:
    print("You are tall enough to ride the roller coaster.")
