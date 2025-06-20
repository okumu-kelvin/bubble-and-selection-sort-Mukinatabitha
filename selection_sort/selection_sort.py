def selection_sort(unsorted_list):
    # Make a copy so the original list is not modified
    arr = unsorted_list[:]
    n = len(arr)

    # Traverse through all list elements
    for i in range(n):
        # Assume the current index is the smallest
        min_index = i

        # Find the index of the minimum element in the remaining list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

