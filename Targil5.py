
def map(func, arr):
    for x in range(len(arr)):
        arr[x]=func(arr[x])
    return arr

def func(num):
    return num*3

if __name__ == '__main__':
    listNum = [1,2,3]
    print( map(func, listNum))