a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
res = 1
while b > 0:
	if b & 1 == 1:
		res = res * a % c
	b = b >> 1
	a = a * a % c
print(res)
