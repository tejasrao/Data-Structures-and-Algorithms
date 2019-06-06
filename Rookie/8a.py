def main():
    s = input().strip()
    n = len(s)
    stack = [-1]
    result = 0
    
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) > 0:
                result = max(result, i - stack[-1])
            else:
                stack.append(i)
    print("Longest valid sub string: {0}".format(result))

if __name__ == '__main__':
    main()
