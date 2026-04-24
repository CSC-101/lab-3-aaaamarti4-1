def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. m = 3 + 1 = 4


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0-false, 1-false, 2-false, 3-true


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4, 5]
print()

#checks if each number between 0 and 5 is greater than 2. if so, add 1 to it and compile into a list