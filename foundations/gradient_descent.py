class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        
        # Initialize x
        x = init

        # Go through the iterations
        for i in range(iterations):
            der_func = 2*x # calculate the derivative each iteration
            x = x - learning_rate * der_func # process the step

        return round(x, 5) # round output to 5 decimals
