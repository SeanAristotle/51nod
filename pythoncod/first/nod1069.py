n = int(input())
res = 0 
for i in range(0,n):
	temp = int(input())
	res = res ^ temp
if res == 0:
	print('B')
else:
	print('A')