def LCS_LENGTH(X, Y):
    m = len(X)
    n = len(Y)
    b = [[' ' for i in range(n + 1)] for i in range(m + 1)]
    c = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'LEFT-UP'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                c[i][j] = c[i][j - 1]
                b[i][j] = 'UP'
            else:
                b[i][j] = 'LEFT'
    return c, b


def PRINT_LCS(b, X, i, j):
    # 对它的起始调用为PRINT_LCS(b, X, X.length, Y.length)
    if i == 0 or j == 0:
        return
    if b[i][j] == 'LEFT-UP':
        PRINT_LCS(b, X, i - 1, j - 1)
        print(X[i - 1], end='')
    elif b[i][j] == 'UP':
        PRINT_LCS(b, X, i - 1, j)
    else:
        PRINT_LCS(b, X, i, j - 1)


def main():
    with open('test.txt', 'r'
              ) as file:
        test = file.read()
        print(test)
    Data = test.split()
    X = list(Data[0])
    Y = list(Data[1])
    m = len(X)
    n = len(Y)
    c, b = LCS_LENGTH(X, Y)
    print("LCS:", end=' ')
    PRINT_LCS(b, X, m, n)


if __name__ == '__main__':
    main()
