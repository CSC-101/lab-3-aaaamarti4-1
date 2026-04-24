def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    return new_list                    # How does this loop differ from that above?

result = copy([4, 9, 2, 1])

#new list values: [], [4], [4, 9], [4, 9, 2], [4, 9, 2, 1]
#idx at end: 4
#creates a new list, then adds 1 by 1 each value of inputted list as list entry. it makes use of append by idx which
#makes it different from the last