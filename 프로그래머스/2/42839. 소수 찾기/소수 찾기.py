from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, (int(n**0.5)+1)):
        if n % i == 0:
            return False
        
    return True

def solution(numbers):
    numbers = list(numbers)
    all_nums = set()

    for r in range(1, len(numbers) + 1):
        for n in permutations(numbers, r):
            num = int(''.join(n))
            all_nums.add(num)

    count = 0
    for z in all_nums:
        if is_prime(z):
            count += 1

    return count