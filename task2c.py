def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
    return new_list #new_list & value : [] 4, [5] 9, [5, 10] 2, [5, 10, 3] 1, [5, 10, 3, 2] 1

result = increment_all([4, 9, 2, 1])
#increment_all takes each entry of the list and adds 1 to it
