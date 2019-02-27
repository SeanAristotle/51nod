T = int(input())
for i in range(0, T):
	a, b = input().split(' ')
	a = int(a)
	b = int(b)
	if a % (b + 1) == 0:
		print("B")
	else:
		print("A")
		