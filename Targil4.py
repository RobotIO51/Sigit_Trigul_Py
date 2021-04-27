

if __name__ == '__main__':
    id_num = input()
    num = id_num[:8]
    count=0
    sum=0
    for x in num:
        if count%2 == 0:
            sum = sum+int(x)
        else:
            if int(x) * 2 > 9:
                sum = int((int(x)*2)%10) + int((int(x)*2)/10) + sum
            else:
                sum = sum+int(x)*2
        count=count+1

    if sum%10 != 0:
        count= (int(sum/10)+1)*10

    print(count)
    print(sum)
    if count-sum == int(id_num[8]):
        print("Good ID")
    else:
        print("Bad ID")