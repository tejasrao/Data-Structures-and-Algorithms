def main():
    words = {w:0 for w in input().split()}
    s = input().strip()
    n = len(s)

    if n == 0:
        print("Not Possible")
        return

    # contains matching substring index(end) values
    matches = [-1]
    for i in range(n):
        m = len(matches) - 1
        flag = False
        for j in range(m, -1, -1):
            # no matches then pos = 0
            pos = matches[j] + 1
            sub = s[pos : pos + i - matches[j]]
            if sub in words:
                flag = True
                break
        if flag:
            matches.append(i)

    if matches[-1] == (n - 1):
        print("Possible")
    else:
        print("Not Possible")
    
if __name__ == '__main__':
    main()
