n = int(input())
score = [int(input()) for _ in range(n)]
score.insert(0, 0)
d = [([0]*(3)) for _ in range(n+1)]

# d[i]에 해당 계단에 도착했을 때 얻을 수 있는 최대 점수를 추가한다
# 첫 번째 연속으로 밟을 때 / 두 번 째 연속으로 밟을 때르 를 고려해 [1][2]를 저장

if n>=1:
    d[1][1] = score[1]
    d[1][2] = score[1]
if n>=2:
    d[2][1] = score[2]
    d[2][2] = score[1]+score[2]

for i in range(3, n+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + score[i]
    d[i][2] = d[i-1][1] + score[i]

print(max(d[n][1], d[n][2]))