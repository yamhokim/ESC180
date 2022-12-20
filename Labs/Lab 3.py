import Lab02
# Problem 1 - Testing Functions in Different Files

# Problem 2 - Sum of Cubes
def sum_cubes(n):
    # initializes the value of sum, starting at 0
    sum = 0
    # runs a for index loop which starts at 1 and goes up to and including n
    # each iteration of the loop adds the cube of i to the overall sum
    for i in range(1, n+1):
        sum += i**3
    # returns sum when loop is finished
    return sum

def sum_cubes2(n):
    # initializes the sum value
    sum = 0
    # runs a for index loop which starts at 1 and goes up to and includes n
    for i in range(1, n+1):
        # each iteration adds i to the sum
        sum += i
    # once all i's have been added to the sum, the sum gets squared
    sum = sum ** 2
    return sum

def check_sum(n):
    '''Return True if the two formulas return the same value for the indicated n,
    False otherwise
    '''
    if sum_cubes(n) == sum_cubes2(n):
        return True
    else:
        return False

def check_sums_up_to_n(N):
    '''Return True if the two functions return the same value for all values of
    N up to and including N
    '''
    for i in range(N+1):
        if sum_cubes(i) != sum_cubes2(i):
            return False
    return True

# Problem 3 - Pi
def leibniz_for(n):
    '''Returns the value of the leibniz formula for the indicated value of n'''
    sum = 0
    for i in range(0, n+1):
        sum += ((-1)**i)/(2*i + 1)
    return sum

def leibniz_while(n):
    sum = 0
    i = 0
    while i <= n:
        sum += ((-1)**i)/(2*i + 1)
        i += 1
    return sum

if __name__ == "__main__":
    Lab02.initialize()
    Lab02.add(42)
    if Lab02.get_current_value() == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")
    Lab02.initialize()
    Lab02.add(64)
    if Lab02.get_current_value() == 65:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    print(sum_cubes(3))
    print(sum_cubes2(3))
    print(leibniz_for(1000))
    print(leibniz_while(1000))
    pi = leibniz_for(1000) * 4
    print(pi)