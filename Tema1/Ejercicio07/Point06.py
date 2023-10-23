set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

# Check if set1 is a superset of itself
if set1.issuperset(set1):
    print("Set1 is a superset of itself")
else:
    print("Set1 is not a superset of itself")

# Check if set1 is a superset of set2
if set1.issuperset(set2):
    print("Set1 is a superset of set2")
else:
    print("Set1 is not a superset of set2")
