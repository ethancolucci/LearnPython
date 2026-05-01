# This program simulates and animate
# a falling ball with a constant acceleration (G)
# Then, generate a plot image with:
# speeds, acc. and heights function of time.

from sys import exit

import pygame as pg
import matplotlib.pyplot as plt

pg.init()

# Screen Height/Width
W, H = 800, 600

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Screen title
pg.display.set_caption("Falling Ball v1")

G = 9.81  # Gravity acc. (m/s^2)
PPM = 80  # pixels per meter (conv m -> pixels)

BALL_RADIUS = 25

BALL_X = W // 2  # Center the ball middle of the screen

START_HEIGHT_METERS = 0.5

# Stops the ball on the ground
GROUND_Y = H - BALL_RADIUS

# acceleration founction of time (for now constant)
a = lambda t: G

# speed function of time
s = lambda t: G * t

# height function of time
h = lambda t: START_HEIGHT_METERS + 0.5 * a(t) * t**2

# Keeping values for plot
times = []
speeds = []
accelerations = []
heights = []

start_time = pg.time.get_ticks()

running = True
while True:

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

    # current time since we start (s)
    t = (pg.time.get_ticks() - start_time) / 1000

    y = h(t)  # current height of current time
    y_px = int(y * PPM)  # current height in pixels

    # push plot values
    times.append(t)
    speeds.append(s(t))
    accelerations.append(a(t))
    heights.append(y)

    # stops the ball and sim if touch the ground
    if y_px >= GROUND_Y:
        y_px = GROUND_Y
        running = False
        break

    # paint background + draw circle + paint it
    screen.fill("black")
    pg.draw.circle(screen, "white", (BALL_X, y_px), BALL_RADIUS)
    pg.display.flip()

pg.quit()

# Create the plot
plt.plot(times, speeds, label="Speed (m/s)")
plt.plot(times, accelerations, label="Acc. (m/s^2)")
plt.plot(times, heights, label="Height (m)")

plt.xlabel("Time (s)")
plt.legend()
plt.grid(True)
plt.savefig("simulation/plot.png")
plt.close()

# EOP
exit()
