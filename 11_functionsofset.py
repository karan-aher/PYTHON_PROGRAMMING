# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union: Elements that are in set1 or set2 or both
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")

# Intersection: Elements that are in both set1 and set2
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

# Difference: Elements that are in set1 but not in set2
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2 (set1 - set2): {difference_set}")

# Symmetric Difference: Elements that are in either set1 or set2 but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print(f"Symmetric Difference of set1 and set2: {symmetric_difference_set}")



