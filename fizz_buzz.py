# Get user input and type cast it to integer.
user_input = int(input())

# If the input divided by 3 and 5 has no remainder...
if (user_input % 3) == 0 and (user_input % 5) == 0:
    # ...print "Fizz Buzz"
    print("Fizz Buzz")
elif (user_input % 3) == 0:
    print("Fizz")
elif (user_input % 5) == 0:
    print("Buzz")
else:
    print(user_input)
