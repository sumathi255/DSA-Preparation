def second_largest(arr):
    if len(arr) < 2:
        return None  # edge case: not enough elements

    max_val = second_max = float('-inf')
    
    for num in arr:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num != max_val and num > second_max:
            second_max = num

    if second_max == float('-inf'):
        return None  # all elements same
    return second_max
