def solution(array):
	count = [0] * (max(array)+1)
	for i in array:
		count[i] += 1
	k = 0
	for x in count:
		if x == max(count):
			k += 1
	if k > 1:
		return -1
	else: 
		return count.index(max(count))