import math
inp2 = int(input("num: "))
print ("starting...")

s2 = 0
def pi2(m):
	ods = []
	for i in range(1,m):
		if i%2==0:continue
		else: ods.append(i)

	global s2;
	
	for n in range(0, len(ods)-1):
		if n % 2 != 0 : continue
		else : 	s2 += 1/(ods[n]); s2 -= 1/(ods[n+1])
		print(s2*4)


pi2(inp2)
print(s2*4)		
r2 = s2*4

print(f"final result:{r2}")