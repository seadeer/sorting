import datetime, random, math
def selectionSort(arr):
    t1 = datetime.datetime.now()
    start = 0
    temp = 0
    while start < len(arr)-1:
        #pick the minimum
        currentMin = arr[start]
        currentMinPos = start
        currentMax = arr[start]
        currentMaxPos = arr[start]
        for i in range(start,len(arr)):
            if arr[i] < currentMin:
                currentMin = arr[i]
                currentMinPos = i 
            if arr[i] > currentMax:
                currentMax = arr[i]
                currentMaxPos = i

        '''after running through the entire array,
        swap the minimum with the first element'''
        temp = currentMin
        temp2 = currentMax
        arr[currentMinPos] = arr[start]
        arr[start] = temp
        arr[currentMaxPos] = arr[len(arr)-1]
        arr[len(arr)-1] = temp2
        start += 1
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
    print selectionSort(makeRandomArr())