def counter(n):

	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		print(n)
		return counter(n-1)

print(counter(6))
