# Exercise 2: Credit Score Evaluator
# Concepts: int conversion, if/elif/else, logical operators, chained comparisons

score = int(input("What's your credit score? "))

# Check validity first with a logical operator
if score < 300 or score > 850:
    print("Invalid score.")
else:
    if score >= 750:
        category = "Excellent - Loan Approved"
        approved = True
    elif 700 <= score < 750: # chained comparison
        category = "Good - Loan Approved with Review"
        approved = True
    elif 600 <= score < 700:
        category = "Fair - Loan Conditional"
        approved = False
    else:
        category = "Poor - Loan Denied"
        approved = False

    # Follow-up message depends on approval
    message = "Interest rate: Low" if approved else "Seek credit improvement."
    print(f"{category}. {message}")