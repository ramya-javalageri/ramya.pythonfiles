# .....................bubble sort.................
# l=[5,1,4,3,2]
# def bubble_sort(l):
#     n=len(l)
#     for i in range(n):
#         for j in range(n-i-1):
#             if l[j]>l[j+1]:                      #for desending order l[j]<l[j+1]
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
# print(f'Unsorted array:{l}')
# print(f'sorted array:{bubble_sort(l)}')


# ..............selection sort..........
# l=[5,1,4,3,2]
# def selection_sort(l):
#     n=len(l)
#     for i in range(n-1):
#         min=i
#         for j in range(i+1,n):
#             if l[min]>l[j]:
#                 min=j
#         l[i],l[min]=l[min],l[i]
#     return l
# print(f'Unsorted array:{l}')
# print(f'sorted array:{selection_sort(l)}')

# .............insertion sort..............
# l=[5,1,4,3,2]
# def i_s(l):
#     n=len(l)
#     for i in range(1,n):
#         key=l[i]
#         j=i-1
#         while j>=0 and l[j]>key:
#             l[j],l[j+1]=l[j+1],l[j]
#             j-=1
#         l[j+1]=key
#     return l
# print(f'Unsorted array:{l}')
# print(f'sorted array:{i_s(l)}')
# ....................merge sort.............
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsortedArr = [4,3,1,2]
print("original array:", unsortedArr)
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)


# ..........................
####################################################

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot_index = len(arr) // 2
#     pivot = arr[pivot_index]
#
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     # print(left, middle, right)
#     return quick_sort(left) + middle + quick_sort(right)
#
# arr = [10, 7, 8, 9, 1, 5]
# print("Original array:", arr)
# sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)

############################################################################


