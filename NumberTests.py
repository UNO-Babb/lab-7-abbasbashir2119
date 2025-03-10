# NumberTests.py

def isThreeOrFive(n):
    """Returns boolean determination if number is multiple of 3 or 5"""
    return n % 3 == 0 or n % 5 == 0

def isPrime(p):
    """Returns boolean (True/False) if the value given is prime."""
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def isEven(n):
    """Returns boolean about given value being even."""
    return n % 2 == 0

def addElement(numList, num):
    """Adds the given number to the list. Does not add duplicate values."""
    if num not in numList:
        numList.append(num)

def fibonacciSequence(value):
    """Returns a list of numbers in the Fibonacci sequence up to the given value."""
    nums = [1, 2]
    while nums[-1] + nums[-2] < value:
        nums.append(nums[-1] + nums[-2])
    return nums

def primeFactors(n):
    """Returns a list of prime factors of n."""
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def isPalindrome(n):
    """Checks if a number is a palindrome."""
    return str(n) == str(n)[::-1]
