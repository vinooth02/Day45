def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second


arr = [10, 25, 5, 40, 15]

print("Second largest:", second_largest(arr))