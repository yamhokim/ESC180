# Problem 1
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

# Problem 2
def interLeave(L1, L2):
    if len(L1) == 0:
        return []
    else:
        return [L1[0], L2[0]] + interLeave(L1[1:], L2[1:])

# Problem 3
def reverse_rec(L): # Fix asap
    if len(L) == 0:
        return []
    return [L[-1]] + reverse_rec(L[:-1])

# Problem 4
def zigzag(L):
    if len(L) == 0:
        return []
    elif len(L) == 1:
        return [L[0]]
    else:
        return

# Problem 5
def is_balanced(s, count=0):
    # find inner most bracket
    # START WITH THE FIRST character and move alogn the string in orde
    # everytime you encounter an open bracket, increase the counte by 1, if you encounter a closed bracker, decrement the counter by 1. If you ever have a negative value, not balanced, if you end up with a value of naythign but zero, not balanced
    # base case: if string is empty, return is count == 0
    # if counter is ever negative, return False
    pass

# Problem 6
def thank_you():
    print("Thank you Gil")

if __name__ == "__main__":
    print(power(3,3))
    print(interLeave([1,2,3,4], ["a","b","c","d"]))
    print(reverse_rec([1, 2, 3, 4, 5]))
    thank_you()