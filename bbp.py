import decimal
decimal.getcontext().prec = 200
mx = int(input("iterations: "))


s = decimal.Decimal(0.0)


def compute(k):
	i1 = decimal.Decimal(1/(16**k))

	i2=decimal.Decimal(4/((8*k)+1))
	i3 = decimal.Decimal(2/((8*k)+4))
	i4= decimal.Decimal(1/((8*k)+5))
	i5 = decimal.Decimal(1/((8*k)+6))

	i = decimal.Decimal(i2 - i3)
	i -= decimal.Decimal(i4)
	i -= decimal.Decimal(i5)

	i = decimal.Decimal(i*i1)
	return i


for it in range(0,mx+1):
	s+=decimal.Decimal(compute(it))
	if it % 1000 == 0: print("{0:.125f} after {1}".format(s, it))
	if it % 10000000 == 0: print("{0:.400f} after {1}".format(s, it))


print(s)	