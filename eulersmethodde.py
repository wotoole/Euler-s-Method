'''
eulersmethodde.py
solving ordinary differen
radioactive decay
solve dy/dt y**2 + 1 using the euler method
analytical solution is y(t) = tan(t)
'''

from math import tan
import matplotlib
import matplotlib.pyplot as plt


#define slope at any point
def f(y):
    return y**2 + 1

#specify initial values
y = 0
t = 0
h = input("Enter the value of the time step, h = ")

plt.title("Euler Method of Solution")
plt.xlabel("Time (t)")
plt.ylabel("y(t)")

while t < 1.0:
    plt.plot(t, y, "bo")
    plt.plot(t, tan(t), "ro")
#calculate the next value of y
    y = y + f(y)*h
    t = t + h
    print t, "\t", "%-10.4g"%y, "\t", "%-10.4g"%tan(t)

plt.show()
