n = input()
part = n.split("-")

answer = 0

first_part = part[0].split('+')
for num in first_part:
    answer += int(num)

for i in part[1:]:
    nums = i.split("+")
    sum = 0
    for num in nums:
        sum += int(num)

    answer -= sum

print(answer)