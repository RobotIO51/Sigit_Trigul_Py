if __name__ == '__main__':
    count = 0
    number = input()
    while number != "stop":
        count = count + int(number)
        number = input()
    print(count)
5