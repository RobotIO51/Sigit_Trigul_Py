if __name__ == '__main__':
    count = 0
    temp = ''
    new = ""
    listNum = input()
    pre = listNum[0]
    for x in listNum:
        temp = x
        if temp == pre:
            count = count + 1
        else:
            new += pre
            new += str(count)
            pre = x
            count = 1
    new += pre
    new += str(count)
    print(new)