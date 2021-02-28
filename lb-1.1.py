a = int(input())
b = int(input())
d = 1
nod = 0

while d <= min(a, b):
	if a % d == 0 and b % d == 0 and d > nod:
		nod = d
		d += 1
	else:
		d += 1

k = a * b
nok = a * b

while k >= max(a, b):
	if k % a == 0 and k % b == 0 and k < nok:
		nok = k
		k -= 1
	else:
		k -= 1

print("НОД =", nod, "НОК =", nok)