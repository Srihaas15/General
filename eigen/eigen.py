import math

def findpq(n, a):
    p, q = -1, -1
    maxvalue = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(a[i][j]) > maxvalue:
                maxvalue = abs(a[i][j])
                p, q = i, j
    return p, q

def jacobi(n, a, P, p, q):
    t = 0.5 * math.atan((2 * a[p][q]) / (a[p][p] - a[q][q]))
    c = math.cos(t)
    s = math.sin(t)

    for i in range(n):
        for j in range(n):
            if i == j:
                P[i][j] = 1.0
            else:
                P[i][j] = 0.0
    
    P[p][p] = c
    P[q][q] = c
    P[p][q] = -s
    P[q][p] = s
    
    temp1 = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp1[i][j] += P[k][i] * a[k][j]
   
    temp2 = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp2[i][j] += temp1[i][k] * P[k][j]

    for i in range(n):
        for j in range(n):
            a[i][j] = temp2[i][j]

def main():
    n = int(input("Enter the order of the matrix:\n"))
    a = []
    print("Enter the elements of the symmetric matrix:")
    for i in range(n):
        row = list(map(float, input().split()))
        a.append(row)

    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                print("Enter a proper symmetric matrix")
                return

    tolerance = 0.00001
    maxpass = 100

    for pass_num in range(maxpass):
        p, q = findpq(n, a)
        if abs(a[p][q]) < tolerance:
            break
        P = [[0.0] * n for _ in range(n)]
        jacobi(n, a, P, p, q)

    print("Eigenvalues of the matrix are:")
    for i in range(n):
        print(f"{a[i][i]:.5f}")

if __name__ == "__main__":
    main()

