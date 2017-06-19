import random

a = random.sample(range(30), random.randrange(15))
b = random.sample(range(30), random.randrange(15))


def listoverlap(list1, list2):
    c = [item for item in list1 if item in list2]
    print(set(c))
    return list(set(c))



def main():
    listoverlap(a, b)



if __name__ == '__main__':
    main()
