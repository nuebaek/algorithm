def to_sec(time):
    mm, ss = map(int, time.split(':'))
    return mm * 60 + ss

def to_time(sec):
    return f'{sec // 60:02}:{sec % 60:02}'
    
def solution(video_len, pos, op_start, op_end, commands):
    video_time = to_sec(video_len)
    pos_time = to_sec(pos)
    op_start_time = to_sec(op_start)
    op_end_time = to_sec(op_end)

    if op_start_time <= pos_time <= op_end_time:
        pos_time = op_end_time

    for command in commands:
        if command == 'next':
            pos_time = min(pos_time + 10, video_time)

        elif command == 'prev':
            pos_time = max(pos_time - 10, 0)

        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time

    return to_time(pos_time)
