# Teinstein Education Private Limited
# Python Interview Questions

# Python program to sort given numbers using Insertion Sort


def insertion_sort(arr):

    for i in range(1, len(arr)):
        current_value = arr[i]
        current_position = i

        while current_position > 0 and arr[current_position - 1] > current_value:
            arr[current_position] = arr[current_position -1]
            current_position = current_position - 1

        arr[current_position] = current_value


arra = [68, 35, 27, 16, 23, 13, 89]

insertion_sort(arra)

print("Array in a sorted manner : ")
for i in range(len(arra)):
    print("%d" % arra[i])