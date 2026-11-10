def safe_ratio(numerator, denominator):
    """Return numerator / denominator as float, or None if denominator is 0.
    
    Both arguments must be exact builtin ints in range [-1000000000, 1000000000].
    Rejects bools and subclasses with TypeError. Bounds checked after type validation.
    """
    # Type checks first: exact builtin int, not bool or subclass
    if type(numerator) is not int or type(denominator) is not int:
        raise TypeError("arguments must be exact builtin ints")
    
    # Bounds
    if not (-1000000000 <= numerator <= 1000000000) or not (-1000000000 <= denominator <= 1000000000):
        raise ValueError("arguments out of bounds")
    
    if denominator == 0:
        return None
    return numerator / denominator
