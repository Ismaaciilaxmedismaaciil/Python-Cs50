import sys 


if len(sys.argv) < 2:
    sys.exit('Too few arguments')


# Using for loop and slicing
for arg in sys.argv[1:]:
    print('Hello, my name is ', arg)