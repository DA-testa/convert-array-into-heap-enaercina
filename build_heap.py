def build_heap(data):
    swaps = []
    n = len(data)

    # iterates from the middle of the array to the beginning
    for i in range(n // 2, -1, -1):
        shift_down(i, data, swaps)

    return swaps

def shift_down(i, data, swaps):
    n = len(data)
    min_index = i

    left_child = 2 * i + 1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child

    right_child = 2 * i + 2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        shift_down(min_index, data, swaps)

def main():
    # input from keyboard
    try:
        n = int(input())
    except ValueError:
        print("Invalid input: please enter a valid integer.")
        return
    data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4 * n
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
