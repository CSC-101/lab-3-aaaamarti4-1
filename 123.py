def categorize(pos:list[int], neg:list[int], n:int) -> None:
    if n < 0:
        neg.append(n)
    else:
        pos.append(n)

positives = [4, 1]
negatives = [-2]
categorize(positives, negatives, -21)
print(positives)
print(negatives)
print()