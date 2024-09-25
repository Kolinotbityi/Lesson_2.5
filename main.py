
def get_matrix(n, m, valve):
    matrix = []

    for i in range(n) :
        list_ = []
        matrix.append(list_)
        for j in range(m) :
            if valve > 0 :
                list_.append(valve)
            else :
                list_ = []
    return matrix


result1 = get_matrix(2, 2, 0)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

