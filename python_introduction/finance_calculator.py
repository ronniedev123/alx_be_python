Monthly_income = float(input("Enter your monthly income: "))
Monthly_expenses = floar(input("Enter your monthly expenses: "))

Monthly_savings = Monthly_income - Monthly_expenses

Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print(f"Your Monthly savings will be ${Monthly_savings:.2f}.")
print(f"Projected annual savings after interest will be {Projected_savings:.2f}")