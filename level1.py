def is_prime(number: int) -> bool:
    """
    Determine whether a given integer is a prime number.
    
    Args:
        number: The integer to evaluate.
        
    Returns:
        True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Check divisors of the form 6k ± 1 up to sqrt(number)
    limit = int(number**0.5)
    for i in range(5, limit + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True
if name == "main":
    try:
        user_input = int(input("Enter an integer to check for primality: "))
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
