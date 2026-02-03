password = input("Please enter a password: ")


def strength(password_local):
    length = len(password_local)
    upper = "no"
    numeric = "no"
    for i in password_local:
        print(i)
        if i.isupper():
            upper = "yes"
    for i in password_local:
        if i.isnumeric():
            numeric = "yes"
    if length >= 8 and upper == "yes" and numeric == "yes":
        return "Strong Password"
    else:
        return "Weak Password"

print(strength(password))