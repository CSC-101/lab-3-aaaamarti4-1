def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total                        #4, 13, 15, 16

result = tally([4, 9, 2, 1])

#adds all values together, one by one