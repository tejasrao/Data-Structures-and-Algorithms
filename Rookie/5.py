def main():
    '''
    n: size of array
    a: list of integers
    '''
    n = int(input())
    a = list(map(int, input().split()))

    maxJump = a[0]
    for i in range(n):
        if maxJump <= i and a[i] == 0:
            print("Not Possible")
            return
        maxJump = max(maxJump, i + a[i])
        if maxJump >= (n - 1):
            print("Possible")
            return
    print("Not Possible")
        

if __name__ == '__main__':
    main()
