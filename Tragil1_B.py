if __name__ == '__main__':
    count = 0
    listNum = input()
    for ch in listNum:
        if ch.isdigit():
            count = count + int(ch)
    print(count)
