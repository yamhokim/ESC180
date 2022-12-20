import math
# Question 1
def count_evens(L):
    '''Counts the number of evens in a given list and returns the number.
    '''
    count = 0 # Counter starts off as zero
    for number in L:
        if number % 2 == 0:
        # Every time an even number is encountered, count goes up by one
            count += 1
    return count # Returns count at the end

# Question 2
def list_to_strs(lis):
    '''Returns the string representation of a list without the use of the str() method.
    '''
    string = "[" # String starts off with the opening square bracket
    i = 0 # i starts off as zero
    while i != (len(lis) - 1):
    # Runs a whiel loop where each iteration adds the element at index i followed by ","
        string += str(lis[i]) + ", "
        i += 1
    # Once all elements have been added, the last element followed by a closing bracket is added
    string += str(lis[-1]) + "]"
    return string # the string is returned

# Question 3
def lists_are_the_same(list1, list2):
    '''Return True if list1 and list2 contain the same elements in the same order,
    return False otherwise.
    '''
    if len(list1) != len(list2): # If list 1 and 2 are of differing lengths, return False
        return False

    for i in range(len(list1)):
    # Runs a for loop checking if each element at index
    # i in list 1 is equal to the same index in list2
        if list1[i] != list2[i]:
            return False
    return True

# Question 4
def simplify_fraction(n, m):
    '''Takes two parameters, n, which is the numerator, and m, which is the denominator, and returns
    the simplified fraction.
    '''
    print("bruh") # This was added to actually check if the code was running
    divisor = n
    while divisor != 0:
    # Runs a while loop where we check if both numbers are divisible by the divisor
        if (n % divisor == 0) and (m % divisor == 0):
            n //= divisor
            m //= divisor
        divisor -= 1 # each iteration decreases the value of the divisor by 1
    return str(n) + "/" + str(m)

# Question 5 - Sum more Pi
def approx_pi(n):
    power = 10**(n-1)
    pi = int(math.pi*(power)) # We get the int of pi, to n sig digs
    sum = 0
    counter = 0
    while int(4*sum*(power)) != pi:
        sum += ((-1)**counter)/(2*counter + 1)
        counter += 1
    return counter

# Question 6 - Euclid's Algorithm
def gcd(a, b):
    '''Returns the greatest common factor of two numbers using Euclid's algorithm.
    '''
    remainder = None
    num1 = a
    num2 = b
    while remainder != 0:
        remainder = num1 % num2 # Find the remainder of num1 divided by num2
        num1 = num2 # num2 becomes the dividend
        num2 = remainder # # the remainder becomes the divisor
    return num1 # when the remainder is zero, num1 is returned

if __name__ == "__main__":
    print(approx_pi(5))
    print(approx_pi(3))
    print(count_evens([1, 2, 4, 6, 8, 11]))
    print(lists_are_the_same([1, 2, 4, 5], [1, 2, 4, 5]))
    print(lists_are_the_same([1, 2, 3, 5, 4, 6], [1, 2, 3, 4, 4, 6]))
    print(simplify_fraction(126, 3))
    print(count_evens([1, 2, 3]))
    print(gcd(106, 16))
    print(list_to_strs([1, 2, 3, 4, 5, 7]))
    print(simplify_fraction(4, 12))