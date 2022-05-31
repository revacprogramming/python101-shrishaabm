def add():
    a = int(input("enter "))
    b = int(input("enter "))
    sum=a+b
    return sum
def output(sum):
    print("the sum is",sum)


def main():
    z=add()
    output(z)


if __name__ == '__main__':
    main()
