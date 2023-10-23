import sys
import timeit

mylist = [1, 2, 3, 4, "hello", True]
mytuple = (1, 2, 3, 4, "hello", True)
myset = {1, 2, 3, 4, "hello", True}

if sys.getsizeof(mylist) > sys.getsizeof(mytuple):
    if sys.getsizeof(mylist) > sys.getsizeof(myset):
        print(f"Mi lista es mayor")
        if sys.getsizeof(mytuple) > sys.getsizeof(myset):
            print(f"Mi set es el menor")
        else:
            print(f"Mi tupla es la menor")
    else:
        print(f"Mi set es mayor")
        print("Mi tupla es la menor")
elif sys.getsizeof(mytuple) > sys.getsizeof(myset):
    print(f"Mi tupla es la mayor")
    if sys.getsizeof(mylist) > sys.getsizeof(myset):
        print(f"Mi set es el menor")
    else:
        print(f"Mi lista es la menor")
else:
    print(f"Mi set es el mayor")
    print(f"Mi lista es la menor")


def join_lists(list1, list2):
    """Returns a new list containing all the elements of the two given lists."""
    return list1 + list2


def join_tuples(tuple1, tuple2):
    """Returns a new tuple containing all the elements of the two given tuples."""
    return tuple1 + tuple2


def join_sets(set1, set2):
    """Returns a new set containing all the elements of the two given sets."""
    return set1 | set2


# Join two lists and print the time used.
joined_list = timeit.timeit('join_lists(mylist, mylist)', globals=globals(), number=100000)
print(f'Time to join lists: {joined_list:.10f}')

# Join two tuples and print the time used.
joined_tuple = timeit.timeit('join_tuples(mytuple, mytuple)', globals=globals(), number=100000)
print(f'Time to join tupla: {joined_tuple:.10f}')

# Join two sets and print the time used.
joined_set = timeit.timeit('join_sets(myset, myset)', globals=globals(), number=100000)
print(f'Time to join set: {joined_set:.10f}')