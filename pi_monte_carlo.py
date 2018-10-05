import random

n=100000

square_point=n
circle_point=0

for x in range(n):
	x=random.uniform(-1.0,1.0)
	y=random.uniform(-1.0,1.0)

	if x**2 + y**2 -1 <=0:
		circle_point=circle_point+1


probability=circle_point/square_point

pi=4*probability
deviation=(pi-3.1415926535897932)*100

print(pi)
print("Deviation: ",deviation,"%")




