def fizzbuzz(number):
    for num in range(number):
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 15 == 0:
            print("FizzBuzz")
        else:
            print(num)
    return num


def main():
    fizzbuzz(100)
    return

if __name__ == '__main__':
    main()
