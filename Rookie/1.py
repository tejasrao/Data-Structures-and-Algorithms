def main():
    """
    n: total number of arrivals/departures
    arrivals: array of time of arrivals
    departures: array of time of departures
    k: total number of rooms available
    """
    n = int(input())
    arrivals = list(map(int, input().split()))
    departures = list(map(int, input().split()))
    k = int(input())

    res = []
    for i in range(n):
        res.append((arrivals[i], 1))
        res.append((departures[i], 0))
    
    res.sort()

    currActive = 0
    maxActive = 0

    for i in range(len(res)):
        if res[i][1] == 1:
            currActive += 1
            maxActive = max(maxActive, currActive)
        else:
            currActive -= 1

    if k >= maxActive:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
