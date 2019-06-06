def main():
    #n = int(input())
    arr = list(map(int, input().split()))
    n = len(arr)

    hts = []
    totalArea = 0
    
    for i in range(n):
        if arr[i] > 0:
            cur = arr[i]
            if len(hts) > 0:
                c = len(hts) - 1
                prev = 0
                while c >= 0 and arr[hts[c]] < cur:
                    if arr[hts[c]] >= prev:
                        width = (i - hts[c] - 1)
                        totalArea += ((min(arr[hts[c]], cur) - prev) * width)
                    prev = arr[hts[c]]
                    c -= 1
                if c >= 0 and arr[hts[c]] >= prev:
                    width = (i - hts[c] - 1)
                    totalArea +=(min(arr[hts[c]], cur) - prev) * width
            hts.append(i)

    print("Total Area: {0}".format(totalArea))
                

if __name__ == '__main__':
    main()
