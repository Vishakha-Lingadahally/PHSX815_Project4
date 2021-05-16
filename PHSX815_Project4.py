# import necessary libraries
import matplotlib.pyplot as plt
# show plots in notebook

# define system in terms of separated differential equations
def f(x,y):
    return 2*y - y**2 - x*y
def g(x,y):
    return - x + x*y

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
        #z.append(z[i] + (h(x[i],y[i],z[i])) * dt)
    return x, y

sys(10, 2, 0.01, 1000)

#plot
fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace = 0.5, hspace = 0.3)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x, 'r-', label='f(x,y)')
ax1.plot(y, 'b-', label='g(x,y)')
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

def fixedpoints(r):
    for x in range(r):
        for y in range(r):
            if ((f(x,y) == 0) and (g(x,y) == 0)):
                fixed_points.append((x,y))
                print('The system has a fixed point at %s,%s' %(x,y))
    return fixed_points

fixedpoints(5)