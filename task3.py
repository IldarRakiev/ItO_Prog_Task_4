def gradient_ascent_method(x_0, alpha, iterations, func, derivative):
    """
    Perform gradient ascent to find the maximum of a function.

    Parameters:
    x_0 (float): The initial guess for the maximum.
    alpha (float): The learning rate.
    iterations (int): The number of iterations to perform.
    func (function): The function for which the maximum is to be found.
    derivative (function): The derivative of the function.

    Returns:
    tuple: The approximate maximum point and the function value at that point.
    """
    x_max = x_0 # Initialize the maximum point with the initial guess

    for _ in range(iterations):
        # Calculate the gradient (derivative) at the current point
        grad = derivative(x_max)

        # Update the maximum point using the gradient and learning rate
        x_max = x_max + alpha * grad
    
    # Calculate the function value at the approximate maximum point
    func_x_max = func(x_max)
    return x_max, func_x_max

# Initial function and derivative
func = lambda x : (x - 2)**2 + 3
deriv = lambda x : -2 * x + 4

# Input values
x_0 = 0 # Initial guess
alpha = 0.1 # Learning rate
N = 100 # Iterations

# Run the method
x_max, f_x_max = gradient_ascent_method(x_0, alpha, N, func, deriv)

# Print results
print(f"Approximate x_max: {x_max}\nf(x_max): {f_x_max}")