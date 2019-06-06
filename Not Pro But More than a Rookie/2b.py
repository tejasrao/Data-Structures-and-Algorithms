def main():
    #n = int(input())
    arr = list(map(int, input().split()))
    n = len(arr)
    #2D
    maxLeft = 0
    maxRight = 0
    totalArea = 0
    start = 0
    end = n - 1

    while start <= end:
        if arr[start] < arr[end]:
            maxLeft = max(maxLeft, arr[start])
            totalArea += (maxLeft - arr[start])
            start += 1
        else:
            maxRight = max(maxRight, arr[end])
            totalArea += (maxRight - arr[end])
            end -= 1
    print("Total Area: {0}".format(totalArea))

if __name__ == '__main__':
    main()
