def problem_solver(input_data):
    # 1. VALIDATION: Check if the input is usable
    if not input_data:
        return "No data provided"

    # 2. PROCESSING: The logic/algorithm
    # This is where you transform the 'mess' into a 'solution'
    result = perform_calculation(input_data)

    # 3. OUTPUT: Return the answer
    return result

def perform_calculation(data):
    # Placeholder for your specific logic
    return sorted(data)
import sympy as sp

def solve_for_x(equation_str):
    # Define the variable
    x = sp.symbols('x')
    
    # Parse the string into a mathematical equation
    # Example input: "2*x - 10" (assumes = 0)
    equation = sp.sympify(equation_str)
    
    # Solve the equation
    solution = sp.solve(equation, x)
    
    return f"The value of x is: {solution}"

# Usage
print(solve_for_x("x**2 - 4")) # Solves x^2 - 4 = 0
