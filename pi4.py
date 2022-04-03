import math
import decimal
import time
inp = int(input("number: "))
print ("starting...")
decimal.getcontext().prec = 200

s = decimal.Decimal(0.0)
for n in range(1,inp+1):
	s += decimal.Decimal(1/(n**2))
	if n % 10000 == 0:	print("pi: {0:.125f} after {1}".format(decimal.Decimal((decimal.Decimal(s*6)).sqrt()),n))
	if n % 1000000 == 0: print("pi: {0:.200f} after {1}".format(decimal.Decimal((decimal.Decimal(s*6)).sqrt()),n))
	

print(s)

r = decimal.Decimal((decimal.Decimal(s*6)).sqrt())

print(r)
print('result: {0:.200f}'.format(r))
