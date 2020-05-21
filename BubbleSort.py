# Teinstein Education Private Limited
# Python Interview Questions

# Python program to sort given numbers using Bubble Sort


def bubble_sort(arr):
    n = len(arr)

    # The loop should run for n-1 times
    for i in range(n - 1):
        # Last i elements are already in place

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arra = [68, 35, 27, 16, 23, 13, 89]

bubble_sort(arra)

print("Array in a sorted manner:")
for i in range(len(arra)):
    print("%d" % arra[i])
