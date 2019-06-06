from math import floor
import sys

def isPossible(arr, n, m, value):
    studentCount = 1
    tempSum = value
    
    for i in range(n):
        if (tempSum - arr[i]) < 0:
            studentCount += 1
            tempSum = value
        else:
            tempSum -= arr[i]
            i += 1        
        
        if studentCount > m:
            return False
    
    return True

def main():
    '''
    n: number of books
    books: list of books(no. of pages)
    M: number of pages
    '''
    n = int(input())
    books = list(map(int, input().split()))
    M = int(input())

    if n < M:
        print("Not possible")
    elif n == 0:
        print("0 pages?")
    elif M == 0:
        print("0 students?")
    else:
        start = 0
        end = sum(books)
        minPages = 0

        while start <= end:
            mid = floor((start + end) /2)

            if isPossible(books, n, M, mid):
                minPages = mid
                end = mid - 1
            else:
                start = mid + 1

        print("Minimum number of pages alloted: {0}".format(minPages))
    
if __name__ == "__main__":
    main()