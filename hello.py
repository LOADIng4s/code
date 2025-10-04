def quick_sort(arr):
    """
    快速排序函数
    参数：arr - 待排序的列表
    返回：排序后的列表
    """
    # 基线条件：如果列表长度小于等于1，直接返回（已排序）
    if len(arr) <= 1:
        return arr
    
    # 选择基准值（这里选列表的第一个元素，也可以选中间或最后一个）
    pivot = arr[0]
    
    # 分区：将列表分为三部分
    less = [x for x in arr[1:] if x <= pivot]   # 所有小于等于基准值的元素
    greater = [x for x in arr[1:] if x > pivot] # 所有大于基准值的元素
    
    # 递归排序左右两部分，并与基准值合并
    return quick_sort(less) + [pivot] + quick_sort(greater)


# 测试示例
if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print("原始列表：", test_arr)
    sorted_arr = quick_sort(test_arr)
    print("排序后：", sorted_arr)  # 输出：[1, 1, 2, 3, 6, 8, 10]