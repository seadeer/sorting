def selectionSort(arr):
    start = 0
    temp = 0
    while start < len(arr)-1:
        #pick the minimum
        currentMin = arr[start]
        currentMinPos = start
        for i in range(start,len(arr)):
            if arr[i] < currentMin:
                currentMin = arr[i]
                currentMinPos = i

        '''after running through the entire array,
        swap the minimum with the first element'''
        temp = currentMin
        arr[currentMinPos] = arr[start]
        arr[start] = temp
        print arr
        start += 1











if __name__ == '__main__':
    selectionSort([2, 7, 9, 10, 2, 3, 7, 1])