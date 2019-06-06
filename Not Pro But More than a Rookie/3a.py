def recurString(words, s):
    n = len(s)

    if n == 0:
        return True

    for i in range(1, n + 1):
        if s[:i] in words and recurString(words, s[i:]):
            return True

    return False

def main():
    words = {w:0 for w in input().split()}
    s = input().strip()
    n = len(s)

    if recurString(words, s):
        print("Possible")
    else:
        print("Not Possible")
    
if __name__ == '__main__':
    main()
