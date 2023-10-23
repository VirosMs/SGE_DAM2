# define the first set
first_set = {1, 2, 3, 4, 5, 6}

# define the second set
second_set = {5, 6, 7, 8}

# remove the intersection of the second set with the first set
first_set -= second_set.intersection(first_set)

# print the updated first set
print(first_set)
