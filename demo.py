from graphics import *
from pid import PID 
import time
import math

win = GraphWin("Window", 500, 500)

pt = Point(100, 220)
cir = Circle(pt, 25)
line = Line(Point(0, 250), Point(500, 250))
line.draw(win)
cir.draw(win)
dt = 0.01
yzad = 250
vel = 0
pid = PID(0.25, 0.01, 0.015, 5, -5)

while True:
    mousePos = win.checkMouse()
    yzad = (mousePos.getY() if mousePos else yzad)
    line.move(0, yzad - line.getP1().getY())
    y = cir.getCenter().getY()
    u = pid.out(yzad, y, dt)
    vel += u
    cir.move(0, vel)
    time.sleep(dt)
