
def build_triangle():
    for i in range(int(n)):
        rows = [1] * (i + 1) 
        for j in range(i + 1):
            if (j != 0) and (j != i):
                rows[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(rows)

def print_triangle():
    for row in triangle:
        print(row)

triangle = []

n = input("Введите целое число: ")
print(f"Введенное число: {n}")

if not n.isdigit():
    print("Введите положительное целое число!")

build_triangle()
print_triangle()
