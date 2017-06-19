import datetime


def years(age):
    date = datetime.datetime.now()
    name = input("what is your name? ")
    #age = int(input("how old are you? "))
    when_is_hundred = date.year + (99 - age)
    print("Hello %s! You are going to be 100 years old in %d!" % (name, when_is_hundred))
    return when_is_hundred

def main():
    years(35)
    return years


if __name__ == '__main__':
    main()
