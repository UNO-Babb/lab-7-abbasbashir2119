# Problem2.py
from NumberTests import isEven, fibonacciSequence

def main():
    total = sum(fib for fib in fibonacciSequence(4000000) if isEven(fib))
    print(total)  # Expected: 4613732

if __name__ == '__main__':
    main()
