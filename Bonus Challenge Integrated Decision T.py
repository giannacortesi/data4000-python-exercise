# Bonus Challenge: Integrated Decision Tool
# Concepts: functions, bool returns, conditionals, match-case

def is_profitable(revenue, cost):
    """Return True if revenue exceeds cost."""
    return revenue > cost

def get_category(product):
    """Categorize a product using matchcase."""
    match product:
        case "electronics" | "gadget":
            return "High Margin"
        case p if p.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _:
            return "Uncategorized - Review Needed"

def get_suggestion(category):
    """Investment suggestion based on category."""
    match category:
        case "High Margin":
            return "Reinvest"
        case "Medium Margin":
            return "Maintain and monitor"
        case "Low Margin":
            return "Hold; look for cost savings"
        case _:
            return "Review before investing"

def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost?"))
    product = input("What's the product name? ").strip().lower()
    category = get_category(product)

    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profit: ${profit:,.2f}")
        print(f"Category: {category}")
        print(f"Suggestion: {get_suggestion(category)}")
    else:
        print("Not profitable. Review costs before investing.")

main()