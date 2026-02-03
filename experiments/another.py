def strength(password):
    length = len(password)
    for i in password:
        if isupper(i):
            upper = "yes"
    for i in password:
        if isnumeric(i):
            numeric = "yes"
    if length >= 8 and upper == "yes" and numeric == "yes":
        return "Strong"
    else:
        return "Weak"

password = input("Please enter a password: ")