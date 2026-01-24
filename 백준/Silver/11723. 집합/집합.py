import sys
input = sys.stdin.readline
s = set()

m = int(input())
for _ in range(m):
    a = input().strip()

    if a == "empty" or a == "all":
        if a == "empty":
            s.clear()
        elif a == "all":
            s.update(list(range(1, 21)))
 
    else:
        func, num = a.split()

        if func == "add":
            s.add(int(num))
        elif func == "remove":
            s.discard(int(num))
        elif func == "check":
            if int(num) in s:
                print(1)
            else:
                print(0)
        elif func == "toggle":
            if int(num) in s:
                s.remove(int(num))
            else:
                s.add(int(num))