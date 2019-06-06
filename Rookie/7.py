def main():
    '''
    n: lenght of input string
    s: input string - contains sequence of '(' or ')'
    '''
    #n = int(input())
    s = input().strip()
    n = len(s)
    currMax = 0
    if n > 1:
        subStrs = [0] * n
        for i in range(1, n):
            if s[i] == ')'and (i - subStrs[i - 1] - 1) >= 0 and s[i - subStrs[i - 1] - 1] == '(':
                subStrs[i] = subStrs[i - 1] + 2
                if (i - subStrs[i - 1] - 2) >= 0:
                    subStrs[i] += subStrs[i - subStrs[i - 1] - 2]
                currMax = max(currMax, subStrs[i])
    print("Longest Valid Substring: {0}".format(currMax))

if __name__ == '__main__':
    main()
