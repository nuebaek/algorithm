def solution(dirs):
    x, y = 0, 0
    paths = []

    move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }

    for direction in dirs:
        dx, dy = move[direction]
        nx, ny = x + dx, y + dy

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        path = (x, y, nx, ny)
        reverse_path = (nx, ny, x, y)

        if path not in paths and reverse_path not in paths:
            paths.append(path)

        x, y = nx, ny

    return len(paths)


# 1. 캐릭터는 `(0, 0)`에서 시작한다.
# 2. 명령어를 하나씩 보며 한 칸 이동한다.
# 3. 범위를 벗어나는 이동은 무시한다.
# 4. 이동할 때마다 지나간 길을 저장한다.
# 5. 이미 지나간 길이면 다시 세지 않는다.
# 6. 처음 지나간 길의 개수를 구한다.
