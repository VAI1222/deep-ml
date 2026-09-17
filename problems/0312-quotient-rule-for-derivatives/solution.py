import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    # Create polynomial objects
    g = np.poly1d(g_coeffs)
    h = np.poly1d(h_coeffs)
    
    # Get derivative polynomial objects
    g_prime = np.polyder(g)
    h_prime = np.polyder(h)
    
    # Compute values at point x
    g_x, h_x = g(x), h(x)
    gp_x, hp_x = g_prime(x), h_prime(x)
    
    # Quotient rule calculation
    return float((gp_x * h_x - g_x * hp_x) / (h_x ** 2))
    pass