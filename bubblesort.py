import random, math
import datetime

def bubbleSort(arr):
    t1 = datetime.datetime.now()
    tmp = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # simultaneous assignment in Python: a,b = b,a
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
                swapped = True
    t2 = datetime.datetime.now()
    runtime = t2 - t1
    return (arr, runtime)

def makeRandomArr():
    arr = []
    for i in range(1, 101):
        arr.append(int(math.floor(random.random()*10000)))
    print "Original array: %s" % arr
    return arr

if __name__ == '__main__':
    print bubbleSort(makeRandomArr())