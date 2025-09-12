import sys
m = int(input())
a = list(map(int,sys.stdin.readline().split()))

a.sort()
atm = []
for i in range(m):
    if i == 0:
        atm.append(a[i])
    else:
        atm.append(atm[i-1] + a[i])
print(sum(atm))