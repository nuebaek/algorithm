s = input()
count_z = 0
count_o = 0

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    if s[i] == '0':
      count_o += 1
    else:
      count_z += 1
    
if s[len(s)-1]=='0':
  count_o += 1

else:
  count_z += 1

print(min(count_z,count_o))
