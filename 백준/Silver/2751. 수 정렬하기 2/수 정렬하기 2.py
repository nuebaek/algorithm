import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
print('\n'.join(map(str, a)))