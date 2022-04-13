import math, decimal
decimal.getcontext().prec = 200

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
mx = int(input(""))
for i in range(0, mx):
	s+=decimal.Decimal(cal_top(i)/cal_b(i))


print(decimal.Decimal(const/(s)))