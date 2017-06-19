import random
import string

def passwordgen():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()?"
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


def main():
    while True:
        inp = input("Would you like to set a new pw? (y or n)")
        if inp == "y":
            print(passwordgen())

        elif inp == "n":
            break
        else:
            print("not a valid option")
    return


if __name__ == '__main__':
    main()
