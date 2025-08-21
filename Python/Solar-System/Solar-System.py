import turtle as tur
from math import *
import random

screen = tur.Screen()
screen.tracer(50)
screen.bgcolor("black")

sun = tur.Turtle()
screen.setup(width=1.0, height=1.0)
sun.shape('circle')
sun.color('yellow')
sun.shapesize(stretch_wid = 2.0, stretch_len = 2.0)  # Slightly bigger sun

starfield = tur.Turtle()
starfield.hideturtle()
starfield.speed(0)
starfield.color("white")
starfield.up()

for _ in range(600):
    angle = random.uniform(0, 2 * pi)
    r = random.uniform(580, 1200)
    x = r * cos(angle)
    y = r * sin(angle)
    starfield.goto(x, y)
    starfield.dot(2)


class Planet(tur.Turtle):
    def __init__(self, name, radius, color, size):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.col = color
        self.color(self.col)
        self.up()
        self.angle = random.uniform(0, 2*pi)  # Random starting positions
        self.shapesize(stretch_wid=size, stretch_len=size)  # Different sizes
        self.dot_counter = 0  # Counter for dot generation
        
        # Create label for planet name
        self.label = tur.Turtle()
        self.label.hideturtle()
        self.label.up()
        self.label.color("white")
        self.label.speed(0)

    def move(self):
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)

        self.goto(sun.xcor() + x, sun.ycor() + y)
        
        # Leave a dot trail every 5 moves to reduce lag
        self.dot_counter += 1
        if self.dot_counter >= 5:
            self.dot(2, self.col)
            self.dot_counter = 0
        
        # Update planet name label
        self.label.clear()
        self.label.goto(self.xcor(), self.ycor() + 15)
        self.label.write(self.name, align="center", font=("Arial", 8, "normal"))

# Planets with realistic sizes and better colors
mercury = Planet("Mercury", 80, '#8C7853', 0.4)    # Small, brownish-gray
venus = Planet("Venus", 160, '#FFC649', 0.7)       # Bright yellow-orange
earth = Planet("Earth", 200, '#6B93D6', 0.8)       # Blue
mars = Planet("Mars", 300, '#C1440E', 0.6)         # Red-orange
jupiter = Planet("Jupiter", 360, '#D8CA9D', 2.2)   # Large, tan/beige
saturn = Planet("Saturn", 460, '#FAD5A5', 1.8)     # Pale yellow
uranus = Planet("Uranus", 500, '#4FD0E7', 1.4)     # Light blue
neptune = Planet("Neptune", 560, '#4B70DD', 1.3)   # Deep blue

planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
# More realistic orbital speeds (closer planets orbit faster)
radius_list = [speed/2 for speed in [0.08, 0.06, 0.04, 0.03, 0.02, 0.015, 0.01, 0.008]]

# Draw orbit paths
orbit_turtle = tur.Turtle()
orbit_turtle.hideturtle()
orbit_turtle.speed(0)
orbit_turtle.up()

for planet in planet_list:
    orbit_turtle.color(planet.col)
    for angle in range(0, 360, 8):  # Draw orbit dots
        x = planet.radius * cos(radians(angle))
        y = planet.radius * sin(radians(angle))
        orbit_turtle.goto(sun.xcor() + x, sun.ycor() + y)
        orbit_turtle.dot(1)

while True:
    screen.update()

    for index, planet in enumerate(planet_list):
        planet.move()
        planet.angle += radius_list[index]