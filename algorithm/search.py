
def sequential_search(arr,target):
    """
    顺序查找函数
    """
    for i in range(len(arr)):
        if target == arr[i]:
            return 0
    return -1

def binary_search(nums, target: int) -> int:
    """
    二分查找，必须有序数组
    """
    low = 0
    high =len(nums)-1

    while(low <= high):
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low =mid + 1
        else:
            high = mid - 1

    return -1

def test_sequential_search_search():
    arr = [1,3,4,5,7,8]
    assert sequential_search(arr,5) == 0


def test_binary_search():
    arr = [1,3,4,5,7,8]
    print(binary_search(arr, 4))