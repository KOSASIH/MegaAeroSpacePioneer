def calculate_cost(material_costs, labor_costs, other_expenses):
    total_cost = material_costs + labor_costs + other_expenses
    return total_cost

# Example usage
material_costs = 1000000  # Cost of materials in dollars
labor_costs = 500000  # Cost of labor in dollars
other_expenses = 200000  # Other expenses in dollars

estimated_cost = calculate_cost(material_costs, labor_costs, other_expenses)

# Output markdown code
print(f"The estimated cost for the megastructure project is ${estimated_cost}.")
