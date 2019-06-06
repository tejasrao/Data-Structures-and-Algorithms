def main():
    m = int(input())
    s = list(map(int, input().split()))
    n = int(input())

    table = [0 for _ in range(n + 1)]
    table[0] = 1
    for i in range(m):
        for j in range(s[i], n + 1):
            table[j] += table[j - s[i]]

    print(table)
    print(table[n])

if __name__ == '__main__':
    main()
