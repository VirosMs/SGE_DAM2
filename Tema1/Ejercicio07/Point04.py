# Define a input variable
input_value = input("Enter a value: ")

# Define a set
my_set = {'1', '2', '3',' 4',' 5'}

# Check if a value is present in the set
if input_value in my_set:
    print(f'{input_value} is present in the set')
else:
    print(f'"{input_value}" is not present in the set')
