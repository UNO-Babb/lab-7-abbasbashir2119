# Problem1.py
import NumberTests

def main():
    total = sum(i for i in range(1000) if NumberTests.isThreeOrFive(i))
    print(total)

if __name__ == '__main__':
    main()
