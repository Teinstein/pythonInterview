# Teinstein Education Private Limited
# Python Interview Questions

# Python program to sort given numbers using Selection Sort


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest = i

        # Find the smallest number
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j

        # Swap the smallest with the current index
        arr[i], arr[smallest] = arr[smallest], arr[i]


arra = [68, 35, 27, 16, 23, 13, 89]

selection_sort(arra)
print('Array in a sorted manner : ')
for i in range(len(arra)):
    print("%d" % arra[i])