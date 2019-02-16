import math
n = int(input())
res = 0
for i in range(1,n+1):
	#print(math.log(i,10))
	res = res + math.log(i,10)
	#print(res)
print(int(res)+1)
