import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


GRAV = 1

class Projectile:
    # class variables for simulation time and number of time slices
    sim_time, time_slices = None, None #cambie de Nonetype a int
	
	
    def __init__(self, x0, y0, v0, alpha0):
        # projectile initial position and velocity
        self.x, self.y = x0, y0
        self.vx = v0 * np.cos(np.radians(alpha0))
        self.vy = v0 * np.sin(np.radians(alpha0))
        
        # time interval to be simulated
        self.t = np.linspace(0., self.sim_time, self.time_slices) 

    def kinematics(self, ax, ay):
        # kinematic equations: position and velocity
        self.x += self.vx * self.t + .5 * ax * self.t ** 2
        self.y += self.vy * self.t + .5 * ay * self.t ** 2

        
        self.vx += ax * self.t
        self.vy += ay * self.t
    
    def get_trajectory(self):
        # returns values of x(t) and y(t)
        return self.x, self.y
        
    
    def get_maxes(self):
    	#maximun points
    	t_max = 2. * v0 * np.sin(np.radians(alpha0)) / GRAV
    	x_max = v0 ** 2 * np.sin(2. * np.radians(alpha0)) / GRAV
    	y_max = (v0 * np.sin(np.radians(alpha0))) ** 2 / ((2.) * GRAV)
    	
    	return "t_max", t_max, "x_max", x_max,"y_max", y_max
    
		
		
class Animator:
    # choose your favorite colors!
    cls = ['green', 'red', 'blue', 'cyan', 'magenta', 'black']
    
    def __init__(self, objs):
        # objects to be animated and its total number
        self.artists = objs
        self.number = len(self.artists)
		
        # instance variables to None; properly set in set_animation
        self.fig = self.ax = self.line = self.point = None
        #self.time_template = self.time_text = None
        self.xdata = self.ydata = None
    
    
    def set_animation(self):
    	# plot setup: axis, labels, title, grid, etc.
    	self.fig = plt.figure()
    	self.ax = plt.axes(autoscale_on=False, xlim=(0, 25), ylim=(0,13))
    	self.ax.set(xlabel='X', ylabel='Y', title='Projectiles motion')
    	# ax.set_aspect('equal')
    	self.ax.grid()
    	# line points setup, time template, points on top of axes
    	
    	#self.time_template = 'time = %.1f a.u.'
    	#self.time_text = self.ax.text(0.4, 0.1, '', transform=self.ax.transAxes)
    	self.xdata, self.ydata = [], []
    	
    	

    def init(self):
        # function used to draw a clear frame
        self.point = [self.ax.plot([], [], 'o-', c= self.cls[i], lw=0) for i in range(self.number)]
        self.line = [self.ax.plot([], [], ls = '--', c = self.cls[i])for i in range(self.number)]
        #self.line.set_data(self.xdata, self.ydata)
        #self.time_text.set_text('')
        return self.line, self.point
        
#hay que anadir algo para hacer con ese index y lograr llenar la lista        
    def animate(self, idx):
    	"""if idx < self.number:
    		for q in range(idx):
    			for i in self.artists[q].y:
    				if i >= 0.:
    					self.xdata.append(self.artists[q].x)
    					self.ydata.append(self.artists[q].y)
    	#function to call at each frame
    			self.line[q][0].set_data(self.xdata, self.ydata)"""
    	for i in range(self.number):
            a = self.artists[i]
            self.xdata, self.ydata = a.get_trajectory()
            self.line[i][0].set_data([self.xdata[i]], [self.ydata[i]])
            if self.ydata[idx] >= 0.:
                self.point[i][0].set_data([self.xdata[idx]], [self.ydata[idx]])
    	return self.line, self.point
    
    def run_animation(self, inval=10, rep=True):
        # set up to perform animation
        ani = animation.FuncAnimation(self.fig, self.animate,
                                      range(len(self.artists[0].y)),
                                      repeat=rep, interval=inval,
                                      init_func=self.init)
        plt.show()



# physical constants (in arbitrary units)
grav_ = GRAV
drag_ = .0 * grav_
params = [val for val in range(15, 91, 15)]

# initial position and velocity; acceleration
x0, y0 = 0., 0.
v0, alpha0 = 5, params
ax, ay = -drag_, -drag_ - grav_
print("parameters =", params)


# calculate simulation time and set time slices
sim_times = max(2. * np.array(v0) * np.sin(np.radians(alpha0)) / grav_)
print("sim times =", sim_times)

Projectile.sim_time = 2. * np.array(v0) * np.sin(np.radians(90)) / grav_
Projectile.time_slices = 160
print("time slices =", Projectile.time_slices)


# create all projectiles to animate
balls = [Projectile(x0, y0, v0, val) for val in alpha0]

# generate their respective trajectories
[ball.kinematics(ax, ay) for ball in balls]

# print some relevant values to check correctenessanimate
#[print(ball.get_maxes()) for ball in balls]
#[print(ball.get_trajectory()) for ball in balls]


# create animator handle object for animation
framer = Animator(balls)

# set up animation
framer.set_animation()

# carry out animation (default parameters)
framer.run_animation(inval=1000*Projectile.sim_time/Projectile.time_slices)



