def parse(feet_inches):
    """Parses a string of feet and inches into separate float values."""
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches
