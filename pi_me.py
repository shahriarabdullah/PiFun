import random
import time

# n is the number of total points taken inside the circular area ADCB
# The more points taken, the higher the accuracy of pi
n=10000
i=0
square_points=0 

start=time.time()

while i<n:
	# These two lines are used to generate random pairs (x,y) within 
	# horizontal range A(-3,0) to C(3,0) and vertical range D(0,-3)
	# to B(0,3)
	x=random.uniform(-3.0,3.0)
	y=random.uniform(-3.0,3.0)


	# The randomly generated pair (x,y) can be outside the circle due
	# to the range we used. So we have to make sure we are only counting
	# the pairs which lie inside the circle
	# For example- (-3,3) is such a randomly generated pair
	if x**2 + y**2 -9<=0:
		i=i+1

		# |x|+|y|=3 is the equation of our square
		# Checking if the point lies inside the square
		if abs(x)+abs(y)-3<=0:
			square_points=square_points+1


print("Total points:         ",n,"\nPoints inside square: ",square_points)

# Calculating the probability of the points lying inside the square
probability=square_points/n

pi=2/probability

# Calculating devation of our result from actual value of pi.
# 16 digits after radix point is considered.
deviation=(pi-3.1415926535897932)*100
end=time.time()

print("\nPI:                   ",pi)
print("\nDeviation:            ",deviation,"%")
print("Elapsed time:         ",end-start)