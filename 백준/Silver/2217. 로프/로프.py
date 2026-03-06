n = int(input())
weight = [int(input()) for _ in range(n)]
result = []
weight.sort(reverse=True)

for i in range(n):
    result.append(weight[i] * (i + 1))
    
print(max(result))