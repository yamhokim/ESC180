# Problem 1
def list1_starts_with_list2(list1, list2):
    if len(list2) > len(list1):
        return False

    for i in range(len(list2)-1):
        if list1[i] != list2[i]:
            return False

    return True

# Problem 2
# edit this asap, only works when the correct sequence comes first
# check if the list matches, each time it doesnt't, get rid of the letter
def match_pattern(list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[0] and list1[i:i + len(list2)] == list2:
            return True

    return False



# Problem 3
def repeats(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False

# Problem 4
# 4a
def print_matrix_dim(M):
    return str(len(M)) + "x" + str(len(M[0]))

# 4b
def mult_M_v(M, v):
    empty_list = []
    sum = 0
    if len(M[0]) != len(v):
        print("The matrix and vector cannot be multiplied")
        return None
    else:
        for i in range(len(M)):
            for j in range(len(v)):
                sum += M[i][j] * v[j]
            empty_list.append(sum)
            sum = 0
    return empty_list

# 4c
def mult_matrix(M1, M2):
    res = []

    if len(M1[0]) != len(M2):
        return None

    for rowM1 in range(len(M1)):
        rowValue = []
        for columnM2 in range(len(M2[0])):
            individualValue = 0
            for columnM1 in range(len(M1[0])):
                individualValue += M1[rowM1][columnM1]*M2[columnM1][columnM2]
            rowValue.append(individualValue)
        res.append(rowValue)

    return res



if __name__ =="__main__":
    print(match_pattern([4, 4, 6, 4, 5, 6], [4, 5, 6]))
    print(print_matrix_dim([[1, 2, 3, 5], [4, 5, 6, 10], [7, 8, 9, 11]]))
    print(list1_starts_with_list2([1, 3, 3, 4, 5, 6], [1, 3, 3, 4]))
    print(repeats([1, 1, 2, 3, 44, 4, 5, 6]))
    print(mult_M_v([[3, 4], [4, 5], [5, 6]], [4, 5]))
    print(mult_M_v([[3, 4, 5], [6, 7, 8], [9, 10, 11]], [1, 2, 3]))
    print(mult_matrix([[1, 2], [3, 4], [5, 6]], [[3, 5, 7], [4, 6, 8]]))