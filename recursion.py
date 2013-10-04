# Multiply all the elements in a list
def multiply_list(l):
    if l == [1]:
        return 1
    return l[0] * multiply_list(l[1:]) 

print multiply_list([5,4,3,2,1])

# Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print factorial(4)

# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

print count_list([1,3,5,7])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

print sum_list([11, 13, 2])


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) <= 1:
        return l
    return [l[-1]] + reverse(l[:-1])

print reverse([1,2,3,4,5])

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2).
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(8)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return 0
    return 1 + find(l[1:], i)

print find(list("hello"), "l")

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) <= 1:
        return True
    else:
        if some_string[0] != some_string[-1]:
            return False
        else:
            return palindrome(some_string[1:-1])

print palindrome("helleh")

# Given the width and height of a sheet of paper, and the number of times to 
# fold it, return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    else:
        if width > height:
            return fold_paper(width/2, height, folds-1)
        else:
            return fold_paper(width, height/2, folds-1)

print fold_paper(20, 10, 3)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if target == 0:
        return n
    print n
    return count_up(target-1, n+1)

print count_up(10,0)

# Move n rings from Tower 1 to Tower 2 given a buffer tower

start = [2,1]
end = []
temp = []

def move_rings(n, start, end, temp):

    if n == 1:
        end.append(start.pop())
    else:
        move_rings(n-1, start, temp, end)
        move_rings(1, start, end, temp)   
        move_rings(n-1, temp, end, start)

print move_rings(len(start), start, end, temp)