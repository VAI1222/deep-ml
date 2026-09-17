import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    # 1. Convert gradient list to a NumPy array for easy calculation
    grad = np.array(gradient, dtype=float)
    
    # 2. Calculate magnitude (L2 norm)
    magnitude = float(np.linalg.norm(grad))
    
    # 3. Handle zero magnitude edge case
    if magnitude == 0:
        zero_vector = [0.0] * len(gradient)
        return {
            'magnitude': 0.0,
            'direction': zero_vector,
            'descent_direction': zero_vector
        }
    
    # 4. Calculate unit vector for steepest ascent (direction / magnitude)
    ascent = grad / magnitude
    
    # 5. Calculate unit vector for steepest descent (-ascent)
    descent = -ascent
    
    # 6. Return as dictionary with lists
    return {
        'magnitude': magnitude,
        'direction': ascent.tolist(),
        'descent_direction': descent.tolist()
    }