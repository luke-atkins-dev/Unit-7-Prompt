"""
In programming to short circuit an and/or condition refers to the fact that if statements
will stop evaluating an and/or condition if a satisfying condition has been met and will not
evaluate all of the conditions.

For and statements this means that if the if statement encounters a condition that has a
"false" value, then it will not evaluate the second condition. This is the same for or conditions
the difference is that if it encounters a "true" value then it will stop evaluation.

This is useful if you want to prevent the program from throwing errors by verifying
certain conditions before running code that might possibly error. This applies to if statements,
variable assignments and anytime you put an and/or condition inside the code.
"""

x = ["value1", "value2", "value3"]

# I know that this code will not error because I check if value3 is present within the list first
# if value3 is not present within the list it will not print anything instead of throwing a ValueError
'value3' in x and print(f'value3 is in the list at position {x.index("value3")}')

arr: list | None = None

def safe_pop(l: list=None):
    # this function will not error no matter what you throw at it
    # order of the conditions matter here
    # we check if the list is not none first becasue if we try to get the length of None or .pop None then we will get an error
    # checking if is not None is a little redundant because of the type check but it helps to read
    return l is not None and type(l) == list and len(l) > 1 and l.pop() or None

print(
    safe_pop(arr)
)
arr=[1,2,3]
print(
    safe_pop(arr)
)