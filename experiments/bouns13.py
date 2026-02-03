feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    """Parses a string of feet and inches into separate float values."""
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    """Converts feet and inches to meters."""
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
print("fi",f, i)
result = convert(f, i)

if result < 1:
    print("You are too short to ride.")
else:
    print("You are tall enough to ride.")
