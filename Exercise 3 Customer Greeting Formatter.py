# Exercise 3: Customer Greeting Formatter
# Concepts: string methods, functions, default parameters, return values

def format_greeting(name, title="Customer"):
    """Return a personalized greeting using the customer's first name."""
    # strip() removes leading/trailing whitespace; title() capitlizes each word
    name = name.strip().title()

    # Empty name -> generic greeting
    if name == "":
        return "Hello, Valued Customer!"

    # split() breaks the name on spaces; [0] grabs the first piece
    first_name = name.split()[0]
    return f"Hello, {first_name} ({title})!"

full_name = input("What's your full name? ")
print(format_greeting(full_name))