# Exercise 4: Tax Bracket Determiner
# Concepts: functions returning values, if/elif/else, modulo, ternary expressions

def get_tax_bracket(income):
    """Return the tax bracket label for an income"""
    if income < 0:
        return "Invalid income."
    elif income < 50000:
        return "Low (10%)"
    elif income < 100000:
        return "Medium (20%)"
    else:
        return "High (30%)"

def get_tax_rate(income):
    """Return the tax rate as a decimal so we can calculate tax."""
    if income < 50000:
        return 0.10
    elif income < 100000:
        return 0.20
    else:
        return 0.30

def add_deduction_note(bracket, income):
    """Bonus: ternary + modulo. Even incomes are 'Deduction Eligible'."""
    return bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket

income = float(input("What's your annual income? "))
bracket = get_tax_bracket(income)

if bracket == "Invalid income.":
    print(bracket)
else:
    tax = income * get_tax_rate(income)
    print(f"Your bracket: {bracket}. Estimated tax: {tax}")

    