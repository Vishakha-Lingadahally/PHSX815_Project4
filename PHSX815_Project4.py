# import necessary libraries
import matplotlib.pyplot as plt
from scipy import sqrt

# define system in terms of separated differential equations
def f(x,y): # Essentially our dx/dt
    return 2*y-y**2-x*y
def g(x,y): # dy/dt
    return -x+x*y

# initialize lists containing values
x = []
y = []

#iv1, iv2 = initial values, dt = timestep, time = range
def sys(iv1, iv2, dt, time):
    # initial values:
    x.append(iv1)
    y.append(iv2)
    # compute and fill lists
    for i in range(time):
        x.append(x[i] + (f(x[i],y[i])) * dt)
        y.append(y[i] + (g(x[i],y[i])) * dt)
    return x, y

sys(5, 5, 0.01, 1000)

#plot the equations:
    
fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace = 0.5, hspace = 0.3)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x, 'r-', label='x(t)')
ax1.plot(y, 'b-', label='y(t)')
#ax1.plot(z, 'g-', label='prey')
ax1.set_title("Evolution with time")
ax1.set_xlabel("time")
ax1.grid()
ax1.legend(loc='best')

ax2.plot(x, y, color="blue")
ax2.set_xlabel("x")
ax2.set_ylabel("y")  
ax2.set_title("Phase space")
ax2.grid()

fixed_points = []
# Define fixed points
def fixedpoints(r):
    for x in range(r):
        for y in range(r):
            if ((f(x,y) == 0) and (g(x,y) == 0)):
                fixed_points.append((x,y))
                print('The system has a fixed point at (%s,%s).' %(x,y))
    return fixed_points

fixedpoints(100)

# Compute the eigenvalues of the Jacobian
def eigenvalues(x,y):
    a11 = 2 - 2*y -x       
    a12 = -y
    # - y + x*y
    a21 =   x
    a22 = - 1 + y               

    tr = a11 + a22
    det = a11*a22 - a12*a21
    lambda1 = (tr - sqrt(tr**2 - 4*det))/2
    lambda2 = (tr + sqrt(tr**2 - 4*det))/2
       
    
    if (lambda1.real < 0 and lambda2.real < 0):
        print('The fixed point is stable at (%s,%s).' %(x,y))
    if (lambda1.real > 0 and lambda2.real > 0):
        print('The fixed point is unstable at (%s %s).' %(x,y))
    if (lambda1.real > 0 and lambda2.real < 0):
        print('The fixed point is unstable at (%s %s).' %(x,y))
    if (lambda1.real < 0 and lambda2.real > 0):
        print('The fixed point is unstable at (%s,%s).' %(x,y))
    return lambda1 , lambda2

# iterate through list of fixed points
for x,y in fixed_points:
    eigenvalues(x,y)       