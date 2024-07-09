T=int(input().strip())
for _ in range(T):
    A,B= map(int, input().strip().split())
    max_burgers = min(A, B)
    print(max_burgers)
