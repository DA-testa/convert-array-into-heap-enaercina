def heapify(a):
    n = len(a)
    swaps = []

    for i in range(n // 2, -1, -1):
        j = i
        while j < n:
            min_idx = j
            if 2*j+1 < n and a[2*j+1] < a[min_idx]:
                min_idx = 2*j+1
            if 2*j+2 < n and a[2*j+2] < a[min_idx]:
                min_idx = 2*j+2
            if j != min_idx:
                swaps.append((j, min_idx))
                a[j], a[min_idx] = a[min_idx], a[j]
                j = min_idx
            else:
                break

    num_swaps = len(swaps)
    return num_swaps, swaps
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    num_swaps, swaps = heapify(a)

    #print(num_swaps)
    #for i, j in swaps:
       # print(i, j)
    result = str(num_swaps)+" "
    for sublist in swaps:
        for element in sublist:
            result = result + str(element) + " "
    print(result)
