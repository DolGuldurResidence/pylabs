def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0  and j != i:
                row[j] = triangle[i - 1][j -1] + triangle[i-1][j]
        triangle.append(row)

    for k in triangle:
        print(" ".join(map(str, k)))


def serpinsky_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = triangle[i - 1][j - 1] + triangle[i-1][j]

        triangle.append(row)

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if triangle[i][j] % 2 == 0:
                triangle[i][j] = " "
            else:
                triangle[i][j] = "*"
    for s in triangle:
        print(" ".join(map(str, s)))


pas_number = int(input("Введите кол-во строк для треугольника Паскаля"))

pascal_triangle(pas_number)

serp_number = int(input("Введите кол-во строк для треугольника Серпинского"))

serpinsky_triangle(serp_number)
