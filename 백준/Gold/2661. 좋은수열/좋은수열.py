n = int(input())

def is_good(num):
    length = len(num)
    for i in range(1, length // 2 + 1):
        # 뒤에서 i개 vs. 그 앞 i개 비교
        if num[-i:] == num[-2 * i:-i]:
            return False

    return True


def recursive(num):
    if len(num) == n:
        print(num)
        exit()

    for next_num in ['1', '2', '3']:
        seq = num + next_num

        if is_good(seq):
            recursive(seq)


for i in ['1', '2', '3']:
    recursive(i)