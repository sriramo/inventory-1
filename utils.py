def is_prime(number):
    for index in range(2, number//2):
        if number%index == 0:
            return False
    return True

def sum_of_prime_numbers(max):
    numbers=list(range(2,max+1))
    return sum(numbers)
    numbers = list(range(2, max+1))
    prime_numbers = list(filter(is_prime, numbers))
    return sum(prime_numbers)
    return sum(numbers)

def fibbonaci(max):
    fibbonaci = [1,1]
    return fibbonaci

