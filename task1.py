def bisection_method(a, b, epsilon, func):
    """
    Perform the bisection method to find the root of a function.

    Parameters:
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    epsilon (float): The tolerance level for the approximation.
    func (function): The function for which the root is to be found.

    Returns:
    float: The approximate root of the function.
    """
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2 # Calculate the midpoint

        # Check if the function changes sign between a and c
        if func(c) * func(a) < 0:
            b = c # If true, update the upper bound
        else:
            a = c # Otherwise, update the lower bound
    
    # Return the approximate root
    return c

# Initial function
func = lambda x : x**3 - 6*x**2 + 11*x - 6

# Input values
a, b = 1, 2 # Initial interval [a, b]
epsilon = 1e-6 # Tolerance

# Run the method
root = bisection_method(a, b, epsilon, func)

# Print results
print(f"Approximate root of the function: {root}")