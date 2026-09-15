def flyodTri(n):
        k = 1
        for i in range(1, n+1):
                for j in range(i):
                        print(k, end = " ")
                        k += 1
                print()
n = int(input())
flyodTri(n)