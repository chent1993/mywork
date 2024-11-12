


def bubble_sort(arr):
    """
    冒泡排序：比较相邻的两个元素。如果第一个比第二个大，就交换它们的位置
    """
    n = len(arr)
    for i in range(n-1):
        print(f"第{i}次排序：")
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
        print(arr)
    return arr


def selection_sort(arr):
    """
    选择排序：在未排序的序列中选择最小（大）的元素，把它放在序列的起始位置上
    """

    for i in range(len(arr)):
        min_index = i
        for j in range (i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


arr = [7, 6, 5, 4, 3, 2, 1]
# print(selection_sort(arr))
print(selection_sort(arr))