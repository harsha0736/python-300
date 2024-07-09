T = int(input().strip())
for _ in range(T):
    N, A, B, C = map(int, input().strip().split())
    dishes_type1 = min(A, B)
    dishes_type2 = min(B, C)
    total_dishes = dishes_type1 + dishes_type2
    if total_dishes >= N:
        print("YES")
    else:
        print("NO")