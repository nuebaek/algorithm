from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True


def solution(numbers):
    digits = list(numbers)
    candidates = set()
    
    for length in range(1, len(digits) + 1):
        for p in permutations(digits, length):
            candidates.add(int(''.join(p)))
            
    return sum(is_prime(c) for c in candidates)
