def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 1 false, 2 false, 3 true, 4 true


answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3, 4]
print() #checks if numbers 0, 1, 2, 3, 4 are greater than 2. then puts into a list if true