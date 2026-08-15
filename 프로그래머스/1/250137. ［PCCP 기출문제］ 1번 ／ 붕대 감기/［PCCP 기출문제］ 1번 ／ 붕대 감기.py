def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    attack = dict(attacks)
    cur_health = health
    combo = 0

    for time in range(1, attacks[-1][0] + 1):
        if time in attack:
            cur_health -= attack[time]
            combo = 0

            if cur_health <= 0:
                return -1
            
        else:
            cur_health = min(max_health, cur_health + x)
            combo += 1

            if combo == t:
                cur_health = min(max_health, cur_health + y)
                combo = 0

    return cur_health