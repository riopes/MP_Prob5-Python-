import numpy as np
import matplotlib.pylab as plt
import math

n=np.arange(0,199) #array of 0 to 199 numbers
x1=(input("Input Equation to evaluate n with: "))   #X(n) input to be evaluated:
 
def x(n):       #Function to evaluate x1 with variable n
    f=eval(x1)  
    return f

for i in n:     #Piecewise function evaluating y(n) with x(n)
    if i == 0:
        y=-1.5*x(n) + 2*x(n+1) - 0.5*x(n+2)
    elif i > 0 and i <= 198:
        y= 0.5*x(n+1) - 0.5*x(n-1)
    else:
        y=1.5*x(n) - 2*x(n-1) + 0.5*x(n-2)

plt.plot(x(n),color="r", label = "Function of x(n)")    #Plots the functions x 
plt.plot(y,color="g", label = "Function of y(n)")       #and y wrt to n
plt.legend()
plt.grid()
plt.xlabel('Range of n numbers to 200')
plt.ylabel('Value of x(n) and y(n)')
plt.show()