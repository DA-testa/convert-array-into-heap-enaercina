def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    swaps = []

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        swaps.append((i, largest))
        total_swaps = 1

        # Heapify the root.
        sub_swaps, sub_total_swaps = heapify(arr, N, largest)
        swaps.extend(sub_swaps)
        total_swaps += sub_total_swaps

    return swaps, total_swaps

def build_heap(data):
    swaps = []
    total_swaps = 0

    # Build a maxheap.
    for i in range(len(data) // 2 - 1, -1, -1):
        sub_swaps, sub_total_swaps = heapify(data, len(data), i)
        swaps.extend(sub_swaps)
        total_swaps += sub_total_swaps

    # One by one extract elements
    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # swap
        swaps.append((0, i))
        sub_swaps, sub_total_swaps = heapify(data, i, 0)
        swaps.extend(sub_swaps)
        total_swaps += sub_total_swaps

    return data, swaps, total_swaps


def main():
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    data, swaps, total_swaps = build_heap(data)

    # output how many swaps were made
    print("Number of swaps made: ", total_swaps)

    # output all swaps
    for i, j in swaps:
        print(i, j)
