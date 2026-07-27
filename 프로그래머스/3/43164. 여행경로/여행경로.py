def dfs(start, tickets, used, path):
    if len(path) == len(tickets) + 1:
        return path[:]

    for i, (a, b) in enumerate(tickets):
        if a == start and not used[i]:
            used[i] = True
            path.append(b)
            result = dfs(b, tickets, used, path)

            if result:
                return result

            used[i] = False
            path.pop()

    return None


def solution(tickets):
    tickets.sort()              
    used = [False] * len(tickets)
    path = ["ICN"]

    return dfs("ICN", tickets, used, path)