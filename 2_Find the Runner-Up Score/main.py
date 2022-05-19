if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maximum = max(arr)
    counting = arr.count(maximum)

    for i in range(counting):
        arr.remove(maximum)

    print(max(arr))
