try:
    sale_value = float(input("Enter a number: "))
    retail_price = float(input("Enter a number: "))

    savings = retail_price - sale_value
    percentage_savings = (savings / retail_price) * 100
    print(f"Savings Value: ${savings} Percentage Savings: {percentage_savings}%")

except (ValueError, ZeroDivisionError):
    print("The retain price cannot be zero. Please enter a valid number.")