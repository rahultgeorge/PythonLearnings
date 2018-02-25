if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    l=list(arr)
    l.sort()
    print (l[len(l)-2])