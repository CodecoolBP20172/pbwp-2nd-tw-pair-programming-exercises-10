def palindrome(string):
    x = "".join(reversed(string))
    if x == string:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
    return x.lower()


def main():
    palindrome(input("please write a word: "))
    return


if __name__ == '__main__':
    main()
