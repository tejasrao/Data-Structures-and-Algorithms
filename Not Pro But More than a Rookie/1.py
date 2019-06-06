def main():
    #n = int(input())
    hist = list(map(int, input().split()))
    n = len(hist)

    arr = [] # contains previous bar lenghts(minimum/sorted?)
    maxArea = -1
    i = 0

    while i < n:
        if len(arr) == 0 or hist[i] >= hist[arr[-1]]:
            arr.append(i)
            i += 1
        else:
            prev = hist[arr.pop()] # height
            if len(arr) == 0:
                width = i
            else:
                width = (i - arr[-1] - 1)
            maxArea = max(maxArea, prev * width)

    while len(arr) != 0:
        prev = hist[arr.pop()] # height
        if len(arr) == 0:
            width = i
        else:
            width = (i - arr[-1] - 1)
        maxArea = max(maxArea, prev * width)

    print("Max Area: {0}".format(maxArea))

if __name__ == '__main__':
    main()
