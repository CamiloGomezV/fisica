import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
print(xdata)
print(ydata)
plt.show()

"""
def set_animation(self):
        # plot setup: axis, labels, title, grid, etc.
        self.fig = plt.figure()
        self.ax = plt.axes(autoscale_on = False, xlim = (0, 26), ylim = (0, 15))
        self.ax.set(xlabel = 'x', ylabel = 'y', title = 'Simulation')
        self.ax.grid()
        # line points setup, time template, points on top of axes
        self.point = [self.ax.plot([], [], 'o-', c = self.cls[i], lw = 0)for i in range(self.number)]
        self.line = [self.ax.plot([], [], ls = "--", lw = 2, c = self.cls[i]) for i in range(self.number)]
        return

    def init(self):
        # function used to draw a clear frame
        return

    def animate(self, idx):
        # function to call at each frame
        for i in range(self.number):
            a = self.artists[i]
            self.xdata, self.ydata = a.get_trajectory()
            self.line[i][0].set_data([self.xdata[i]], [self.ydata[i]])
            if self.ydata[idx] >= 0.:
                self.point[i][0].set_data([self.xdata[idx]], [self.ydata[idx]])

"""
