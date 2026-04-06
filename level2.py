def generate_fibonacci(terms: int) -> list[int]:
    """
    Generate a Fibonacci sequence containing the specified number of terms.
    
    Args:
        terms: The number of Fibonacci terms to generate. Must be non-negative.
        
    Returns:
        A list of integers representing the Fibonacci sequence.
    """
    if terms < 0:
        raise ValueError("Number of terms must be non-negative.")
    if terms == 0:
        return []
    if terms == 1:
        return [0]
        
    sequence = [0, 1]
    while len(sequence) < terms:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if name == "main":
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        result = generate_fibonacci(num_terms)
        print(f"Fibonacci sequence ({num_terms} terms): {result}")
    except ValueError as e:
        print(f"Error: {e}")
