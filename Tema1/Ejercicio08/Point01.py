try:
    # get keyboard input (string)
    rawInput = input('Enter number:')
    # convert string to integer
    x = int(rawInput)
    # calculate number squared
    print(x*x)
except ValueError:
    print("Invalid input. Please enter a number.")
