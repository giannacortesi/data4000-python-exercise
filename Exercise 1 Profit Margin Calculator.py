# Exercise 1: Profit Margin Calculator
# Concepts: input, float variables, arithmetic, f-string formatting

revenue = float(input("What's the revenue?"))
cost = float(input("What's the cost?"))

# Profit is simply revenue minus cost
profit = revenue - cost

# Only calculate margin if revenue is positive (avoids division by zero)
if revenue > 0:
    margin = (profit / revenue) * 100
    # :, adds thousands separators; .2f keeps 2 decimal places
    print(f"Profit: ${profit:,.2f} | Nargin: {margin:.2f}%")
else:
    print("Invalid revenue.")