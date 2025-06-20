def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    def bubble_sort(unsorted_list):
       n = len(unsorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break
my_list = [54, 39, 85, 12, 27, 10, 93]
bubble_sort(my_list)
print("Sorted list:", my_list)
Sorted list: [11, 12, 22, 25, 34, 64, 90]
pass
