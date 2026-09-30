# Exercise 5: Product Category Matcher
# Concepts: match-case, guards, strip/lower

product = input("What's the product name? ").strip().lower()

match product:
    case "electronics" | "gadget":
        category = "High Margin"
    case p if p.startswith("tech"): #guard clause handles the prefix check
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _: #default case
        category = "Uncategorized - Review Needed"

print(f"Product: {product} | Category: {category}")