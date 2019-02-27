T = int(input())
for i in range(0, T):
	a, b = input().split(' ')
	a = int(a)
	b = int(b)
	if a > b:
		a, b = b, a
	c = b-a
	w = int((5 ** 0.5 + 1) / 2 * c)
	if w == a:
		print("B")
	else:
		print("A")
