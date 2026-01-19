n, k = map(int, input().split())
lst = list(map(int, input().split()))
plugs = []
ans = 0

for i in range(k):
    now = lst[i]
    # 이미 꽂혀있다면 넘어간다
    if now in plugs:
        continue
    # 비어있으면 일단 추가한다
    if len(plugs) < n:
        plugs.append(now)
    # 둘 다 해당하지 않으면 뽑아야하는 플러그를 찾는다
    else:
        target_item = 0
        max_idx = -1
        for p in plugs:
            if p not in lst[i+1:]:
                target_item = p
                break
            current_idx = lst[i+1:].index(p)
            if current_idx > max_idx:
                max_idx = current_idx
                target_item = p
        plugs.remove(target_item)
        plugs.append(now)
        ans += 1

print(ans)