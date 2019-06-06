import sys

def main():
    '''
    N: number of integers
    A: list of integers
    S: sum
    '''
    N = int(input())
    A = list(map(int, input().split()))
    S = int(input())

    A.sort()
    
    res = 0
    tmp = sys.maxsize

    for i in range(N - 2):
        j = i + 1
        k = N - 1
        while(j < k):
            currSum = A[i] + A[j] + A[k]
            if abs(S - currSum) < tmp:
                res = currSum
                tmp = abs(S - currSum)
            if res > S:
                k -= 1
            else:
                j += 1
    
    print("Closest sum(three integers): {0}".format(res))

if __name__ == "__main__":
    main()