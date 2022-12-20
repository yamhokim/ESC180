import numpy as np

# Problem 1
def print_matrix(M_lol):
    matrix = np.array(M_lol)
    return matrix

# Problem 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

# Problem 3
def get_row_to_swap(M, start_i):
    empty_list = []
    for i in range(start_i, len(M)):
        for j in range(len(M[i])):
            if M[i][j] != 0:
                empty_list.append((i, j))
                break
    while len(empty_list) > 1:
        if empty_list[0][1] < empty_list[1][1]:
           del empty_list[1]
        elif empty_list[0][1] > empty_list[1][1]:
            del empty_list[0]
        elif empty_list[0][1] == empty_list[1][1]:
            del empty_list[1]

    return empty_list[0][0]


# Problem 4
def add_rows_coefs(r1, c1, r2, c2):
    L = []
    L1 = []
    L2 = []
    for element in r1:
        element *= c1
        L1.append(element)

    for element in r2:
        element *= c2
        L2.append(element)

    for i in range(len(r1)):
        sum = L1[i] + L2[i]
        L.append(sum)

    return L


# Problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    subtracting_row = [] # Create an empty list representing the row_to_sub multiplied by the coefficient
    for row in range(row_to_sub+1, len(M)):
        row_to_be_subtracted = M[row] # Create another list representing the row we will mutate
        # Create a variable which stores the factor we will multiply subtracting_row by to erase the index from row_to_be_subtracted
        if M[row_to_sub][best_lead_ind] == 0:
            factor = 1
        else:
            factor = M[row][best_lead_ind] / M[row_to_sub][best_lead_ind]
        for element in M[row_to_sub]:
            subtracting_row.append(element) # Fill the subtracting row with the elements of row_to_sub
        for elem in range(len(subtracting_row)):
            subtracting_row[elem] *= factor # Multiply the entire row by the factor
        for i in range(len(row_to_be_subtracted)):
            # mutate the row we are subtracting from by subtracting each element of row_to_be_subtracted by its corresponding element
            # in subtracting_row
            row_to_be_subtracted[i] = int(row_to_be_subtracted[i] - subtracting_row[i])

        M[row] = row_to_be_subtracted # set the corresponding row in M to be equal to the mutated row_to_be_subtracted
        subtracting_row = []
    return M # In the end, return the mutated M

# Problem 6
def forward_step(M): # Edit me
    for i in range(len(M)):
        if M[i][i] == 0:
            temp = i
            n = i
            while get_row_to_swap(M, n) == n:
                n += 1
            M[i] = M[get_row_to_swap(M, n)]
            M[get_row_to_swap(M, n)] = M[temp]
        print(M)
        eliminate(M, i, n)

# Problem 7
def backward_step(M):
    pass

# Problem 8
def solve():
    pass

# print(print_matrix([[1,-2,3],[3,10,1],[1,5,3]]))
# print(get_lead_ind([0, 0, 0, 0, 1]))

# M = [[5, 6, 7, 8],
# [0,0, 1, 1],
# [0, 1, 5, 2],
# [0, 0, 7, 0]]

L = [[ 0, 0, 1, 0, 2],[1, 0, 2, 3, 4],[3, 0, 4, 2, 1],[1, 0, 1, 1, 2]]
forward_step(L)

