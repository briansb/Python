# Checks the algebra for Morley's Theorem Proof
import sys
import numpy as np
import matplotlib.pyplot as plt

# the three vertices are global...they are the only values that are not computed
#  (see page 1)
Ux = -30
Uy = 20
Vx = 20
Vy = 15
Wx = 0
Wy = 0

def main():
	# get slopes of three perimeter lines...1, 2, and 3 (see page 1)
	# I could have used an array, but when we get to checking the algebra,
	# 	  there will be less typing
	a1 = GetSlope(Wy,Uy,Wx,Ux)
	a2 = GetSlope(Uy,Vy,Ux,Vx)
	a3 = GetSlope(Vy,Wy,Vx,Wx)
	print ('Slope a1 = %s\nSlope a2 = %s\nSlope a3 = %s' % (a1, a2, a3))
	b1 = GetY_Intercept(Wy,a1,Wx)
	b2 = GetY_Intercept(Uy,a2,Ux)
	b3 = GetY_Intercept(Vy,a3,Vx)
	print ('Y-Intercept b1 = %s\nY-Intercept b2 = %s\nY-Intercept b3 = %s' % (b1, b2, b3))

# plotting
line1_x = (Ux,Wx)
line1_y = (Uy,Wy)
line3_x = (Wx, Vx)
line3_y = (Wy, Vy)
line2_x = (Vx, Ux)
line2_y = (Vy, Uy)
plt.plot(line1_x, line1_y)
plt.plot(line3_x, line3_y)
plt.plot(line2_x, line2_y)
plt.show()


def GetSlope(b2,b1,a2,a1):
	if ((a2-a1) == 0):
		print('ERROR: Division by zero in GetSlope')
		sys.exit()
	return (b2-b1)/(a2-a1)

def GetY_Intercept(y,a,x):
	return y-a*x


# If AlgebraChecker is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
