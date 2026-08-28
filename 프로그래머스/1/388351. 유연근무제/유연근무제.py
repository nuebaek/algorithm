def time_calculator(t):
    if t % 100 >= 50:
        return t + 50
    return t + 10


def check(schedule, timelog, startday):
    standard = time_calculator(schedule)

    for i, time in enumerate(timelog):
        day = (startday + i - 1) % 7 + 1

        if day in (6, 7):
            continue

        if time > standard:
            return 0

    return 1


def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        answer += check(schedules[i], timelogs[i], startday)

    return answer
