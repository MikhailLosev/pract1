def main():
    def spiral():
        print("Введите n,m через пробел.")
        n, m = map(int, input().split())

        print("Введите матрицу, " + str(n) + " строк. Каждая строка " + str(m) + " символов через пробел!")
        a_ = []
        for i in range(1, n + 1):
            g = input().split()
            g = [int(x) for x in g]
            if len(g) != m:
                return 0
            else:
                a_.append(g)
        a = [[0] * m for _ in range(n)]
        results = []

        i, j, d = 0, 0, 0
        moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
        for k in range(1, n * m + 1):
            a[i][j] = k
            results.append(a_[i][j])
            for l in range(4):
                newD = (d + l) % 4
                di, dj = moves[newD]
                newI, newJ = i + di, j + dj
                if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
                    i, j, d = newI, newJ, newD
                    break
        print('\n')


        print('\n')
        print(results)

    spiral()
if __name__ == "__main__":
    main()

