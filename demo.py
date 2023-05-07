def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 选择第一个元素为基准值
        less = [x for x in arr[1:] if x <= pivot]  # 所有比基准值小的元素
        greater = [x for x in arr[1:] if x > pivot]  # 所有比基准值大的元素
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([3, 2, 5, 1]))
