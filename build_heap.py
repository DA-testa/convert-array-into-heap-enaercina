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
def main():
    ievade = input("Input I or F:  ")
    if "I" in ievade:
        n = int(input())
        a = list(map(int, input().split()))
        assert len(a) == n
        num_swaps, swaps = heapify(a)
    elif "F" in ievade:
        fails = "./tests/" + input("Input filename(04): ")
        if "a" in fails:
            print("wrong file name")
            return
        with open(fails) as f:
            n = int(f.readline())
            a = list(map(int, f.readline().split()))
            assert len(a) == n
            num_swaps, swaps = heapify(a)
    else:
        print("wrong input")
        return
    swaps_l = len(swaps)
    assert swaps_l < 4 * len(a)
    print(num_swaps)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
