def main():
    '''
    n: number of integers
    a: list of non-negative integers
    # lines are at: (i, A[i]) and (i, 0)
    '''
    n = int(input())
    a = list(map(int, input().split()))
    
    res = -1
    start = 0
    end = n - 1

    while start <= end:
        res = max(res, min(a[start], a[end]) * (end - start))

        if a[start] < a[end]:
            start += 1
        else:
            end -= 1
    
    print("Max area: {0}".format(res))
    
if __name__ == "__main__":
    main()