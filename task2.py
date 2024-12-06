import math

def golden_section_minimization_method(a, b, epsilon, func):
    """
    Perform the golden section search method to find the minimum of a function.

    Parameters:
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    epsilon (float): The tolerance level for the approximation.
    func (function): The function for which the minimum is to be found.

    Returns:
    tuple: The approximate minimum point and the function value at that point.
    """
    phi = (1 + math.sqrt(5)) / 2 # Golden ratio
    reversed_phi = 1 / phi # Inverse golden ratio

    # Initial interior points
    c = b - reversed_phi * (b - a)
    d = a + reversed_phi * (b - a)
    func_c, func_d = func(c), func(d)

    while abs(b - a) > epsilon:
        if func_c < func_d:
            # Update the interval to [a, d]
            b, d = d, c
            func_d = func_c
            
            # Calculate new point c
            c = b - reversed_phi * (b - a)
            func_c = func(c)
        else:
            # Update the interval to [c, b]
            a, c = c, d
            func_c = func_d

            # Calculate new point d
            d = a + reversed_phi * (b - a)
            func_d = func(d)

    # Calculate the approximate minimum point
    x_min = (a + b) / 2
    return x_min, func(x_min)

# Initial function
func = lambda x : (x - 2)**2 + 3

# Input values
a, b = 0, 5 # Initial interval [a, b]
epsilon = 1e-4  # Tolerance

# Run the method
x_min, func_x_min = golden_section_minimization_method(a, b, epsilon, func)

# Print results
print(f"Approximate x_min: {x_min}\nf(x_min): {func_x_min}")