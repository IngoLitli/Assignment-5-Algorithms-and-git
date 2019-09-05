
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
old_int = 0
max_int = -1
while num_int > -1:
    if num_int > old_int:
        max_int = num_int
    old_int = num_int

    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line
