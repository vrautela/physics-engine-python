from bodies import *
import math
# import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

G = 6.67408e-11

# Create some bodies
rb1 = RoundBody(1e16, (0, 0), (0, 10), 5)
rb2 = RoundBody(1e18, (30, 40), (-1000, 0), 10)

bodies = [rb1, rb2]

# Create figure and axis
fig, ax = plt.subplots()

ax = plt.axis([-100, 100, -100, 100])

p1, = plt.plot(rb1.position[0], rb1.position[1], color='green', marker='o', markersize=2*rb1.radius)
p2, = plt.plot(rb2.position[0], rb2.position[1], color='red', marker='o', markersize=2*rb2.radius)

def animate(i):
    """
    THIS IS A TERRIBLE HACK, need to figure out why I can't do what I want
    """
    global p1
    global p2
    if not rb1.overlaps_with(rb2):
        pass
        f_g = (G * rb1.mass * rb2.mass) / (rb1.distance_between(rb2) ** 2)
        f_1 = tuple(f_g * num for num in rb1.unit_vec_between(rb2))
        f_2 = tuple(-num for num in f_1)

        a_1 = (f_1[0] / rb1.mass, f_1[1] / rb1.mass)
        a_2 = (f_2[0] / rb2.mass, f_2[1] / rb2.mass)

        # Each "tick" of the clock is 1 millisecond
        rb1.move()
        rb1.accelerate(a_1)

        rb2.move()
        rb2.accelerate(a_2)

        # print("First body velocity: (%d, %d)" % rb1.velocity)
        # print("Second body velocity: (%d, %d)" % rb2.velocity)

        p1.set_data(rb1.position[0], rb1.position[1])
        p2.set_data(rb2.position[0], rb2.position[1])

        # p1, = plt.plot(rb1.position[0], rb1.position[1], color='green', marker='o', markersize=5)
        # p2, = plt.plot(rb2.position[0], rb2.position[1], color='red', marker='o', markersize=10)

        xmin = -100
        xmax = 100
        ymin = -100
        ymax = 100

        for body in bodies:
            x = body.position[0]
            y = body.position[1]

            if x < xmin:
                xmin = x
            elif x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            elif y > ymax:
                ymax = y

        ax = plt.axis([xmin, xmax, ymin, ymax])
    else:
        midpoint = rb1.midpoint_between(rb2)
        print(rb1.position)
        print(rb2.position)
        print(midpoint)
        p1.set_data(rb1.position[0], rb1.position[1])
        p2.set_data(rb2.position[0], rb2.position[1])
        pboom, = plt.plot(midpoint[0], midpoint[1], color='blue', marker='x', markersize=20)


anim = FuncAnimation(fig, animate, interval=10)

plt.show()
