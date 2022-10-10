import random
import time


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            #time.sleep(1)

        return array


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            #time.sleep(1)

            return array
    return array


def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []

    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1

        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    #print(result)
    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    print(f"Left: {left}\t Right: {right}")

    return merge(merge_sort(left), merge_sort(right))


def quick_sort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]
    print(pivot)
    for item in array:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        elif item == pivot:
            same.append(item)
    print(low + same + high)

    return quick_sort(low) + same + quick_sort(high)


# test_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# print(quick_sort(test_array))




