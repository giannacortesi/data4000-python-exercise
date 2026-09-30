# DATA 4000: Python Exercise

Python 3.x, developed in VS Code.

| File | Description |
|------|-------------|
| `Exercise 1 Profit Margin Calculator.py` | Profit and margin from revenue/cost; guards against zero revenue. |
| `Exercise 2 Credit Score Evaluator.py` | Categorizes credit score and loan eligibility; validates 300-850 range. |
| `Exercise 3 Customer Greeting Formatter.py` | `format_greeting()` cleans a name and returns a first-name greeting. |
| `Exercise 4 Tax Bracket Determiner.py` | `get_tax_bracket()` and `get_tax_rate()` compute bracket and estimated tax. Includes bonus ternary deduction check. |
| `Exercise 5 Product Category Matcher.py` | Match-case product categorizer with a guard for "tech" prefixes. |
| `Bonus Challenge Integrated Decision T.py` | Combines functions and match-case to suggest an investment action. |

## Assumptions
- Inputs are valid numbers (no exception handling required).
- Tax bracket boundaries: below 50,000 is Low, 50,000 to 99,999.99 is Medium, 100,000+ is High.
- Exercise 5 prints the cleaned (stripped, lowercased) product name, matching the sample output.

## Sample runs
```
What's the revenue? 5000.0
What's the cost? 3500.0
Profit: $1,500.00 | Margin: 30.00%
```
```
What's your annual income? 75000.0
Your bracket: Medium (20%). Estimated tax: 15000.0
```
