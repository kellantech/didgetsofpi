import math, decimal
decimal.getcontext().prec = 400

def cal_b(n):
	i1 = math.factorial(3*n)
	i2 = math.factorial(n)**3
	i3 = -262537412640768000**n
	return i1*i2*i3
def cal_top(n):
	i1 = math.factorial(6*n)
	i2 = (545140134*n)+13591409
	return i1*i2 

const = decimal.Decimal(426880 * math.sqrt(10005))
s = decimal.Decimal(0.0)
mx = int(input("iterations: "))
for i in range(0, mx):
	s+=decimal.Decimal(cal_top(i)/cal_b(i))
	if i % 1000 ==0: print("{0:.125} after {1}".format(decimal.Decimal(const/(s)),i))
	if i % 100000 ==0: print("{0:.400} after {1}".format(decimal.Decimal(const/(s)),i))


#decimal.Decimal(const/(s))
print(decimal.Decimal(const/(s)))
