matrix = []
j = 0
while j == 0:
    row_input = [int(i) for i in input().split() if i != 'end']
    if not row_input:
        j += 1
        break
    matrix.append(row_input)

m = matrix
m2 = [[0 for j in range(len(m[0]))] for i in range(len(m))]
for i in range(len(m)):
    for j in range(len(m[0])):
        if i == 0 and len(m) == 1:
            if len(m[0]) == 1:
                m2[i][j] = m[i][j] * 4
            elif j == 0:
                m2[i][j] = m[i][-1] + m[-1][j] + m[i][j + 1] + m[i][j]
            elif j == len(m[0]) - 1:
                m2[i][j] = m[i][j - 1] + m[-1][j] + m[i][0] + m[i][j]
            else:
                m2[i][j] = m[i][j - 1] + m[-1][j] + m[i][j + 1] + m[i][j]
        elif len(m[0]) == 1 and len(m) > 1:
            if i == 0 and j == 0:
                m2[i][j] = m[i][j] + m[-1][j] + m[i][j] + m[i+1][j]
            elif i == len(m)-1:
                m2[i][j] = m[i][j] + m[i-1][j] + m[i][j] + m[0][j]
            else:
                m2[i][j] = m[i][j] + m[i-1][j] + m[i][j] + m[i+1][j]
        elif i == 0 and j == 0:
            m2[i][j] = m[i][-1] + m[-1][j] + m[i][j + 1] + m[i + 1][j]
        elif i == len(m) - 1 and j == len(m[0]) - 1:
            m2[i][j] = m[i][j - 1] + m[i - 1][j] + m[i][0] + m[0][j]
        elif i == 0:
            if j == len(m[0]) - 1:
                m2[i][j] = m[i][j - 1] + m[i - 1][j] + m[i][0] + m[i + 1][j]
            else:
                m2[i][j] = m[i][j - 1] + m[-1][j] + m[i][j + 1] + m[i + 1][j]
        elif j == 0:
            if i == len(m) - 1:
                m2[i][j] = m[i][-1] + m[i - 1][j] + m[i][j + 1] + m[0][j]
            else:
                m2[i][j] = m[i][-1] + m[i - 1][j] + m[i][j + 1] + m[i + 1][j]
        elif i != 0:
            if j == len(m[0]) - 1:
                m2[i][j] = m[i][j - 1] + m[i - 1][j] + m[i][0] + m[i + 1][j]
            elif i == len(m) - 1:
                m2[i][j] = m[i][j - 1] + m[i - 1][j] + m[i][j + 1] + m[0][j]
            else:
                m2[i][j] = m[i][j - 1] + m[i - 1][j] + m[i][j + 1] + m[i + 1][j]
for i in range(len(m2)):
    for j in range(len(m2[0])):
        print(m2[i][j], end=' ')
        if j == len(m2[0]) - 1:
            print()
