import sys

mylist=[1, 2, 3, 4, "hello", True]
mytuple=(1, 2, 3, 4, "hello", True)
myset={1, 2, 3, 4, "hello", True}

if sys.getsizeof(mylist) > sys.getsizeof(mytuple):
    if sys.getsizeof(mylist) > sys.getsizeof(myset):
        print(f'Mi lista es mayor')
        if sys.getsizeof(mytuple) > sys.getsizeof(myset):
            print(f'Mi set es el menor')
        else:
            print(f'Mi tupla es la menor')
    else:
        print(f'Mi set es mayor')
        print('Mi tupla es la menor')
elif sys.getsizeof(mytuple) > sys.getsizeof(myset):
    print(f'Mi tupla es la mayor')
    if sys.getsizeof(mylist) > sys.getsizeof(myset):
        print(f'Mi set es el menor')
    else:
        print(f'Mi lista es la menor')
else:
    print(f'Mi set es el mayor')
    print(f'Mi lista es la menor')


mylist.extend(mytuple)
mylist.extend(myset)

print(*mylist, sep="\n")