# https://www.acmicpc.net/problem/2628

def largest_area (row, column, matrix):
    row_cut = [0, row]
    column_cut = [0, column]

    for cut in matrix:
        if cut[0] == 0:
            row_cut.append(cut[1])
        else:
            column_cut.append(cut[1])

    row_cut.sort()
    column_cut.sort()
    max_area = 0

    for i in range(len(row_cut)-1):
        for j in range(len(column_cut)-1):
            area = (row_cut[i+1] - row_cut[i])*(column_cut[j+1]-column_cut[j])

            if max_area < area:
                max_area = area

    return max_area


N, M = map(int, input().split())
T = int(input())
input_matrix = []
for t in range(T):
    input_list = list(map(int, input().split()))
    input_matrix.append(input_list)
print(largest_area(M, N, input_matrix))
