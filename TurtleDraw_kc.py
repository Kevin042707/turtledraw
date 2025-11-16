import turtle
import math

screen = turtle.Screen()
screen.setup(width=450, height=450)
screen.title("TurtleDraw")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

filename = input("Enter the input filename: ")

try:
    with open(filename) as file:
        total_dist = 0
        pen_down = False
        prev_x, prev_y = None, None
        
        for line in file:
            line = line.strip()
            if line.lower() == "stop":
                t.penup()
                pen_down = False
                continue
            
            parts = line.split()
            if len(parts) != 3:
                continue
            
            color, x, y = parts[0], float(parts[1]), float(parts[2])
            t.color(color)
            
            if not pen_down:
                t.penup()
                t.goto(x, y)
                t.pendown()
                pen_down = True
            else:
                t.goto(x, y)
                dist = math.dist((prev_x, prev_y), (x, y))
                total_dist += dist
            
            prev_x, prev_y = x, y
    
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(180, -200)
    writer.write(f"Total distance: {total_dist:.2f}", align="right")
    
    input("Press Enter to close...")
    
except FileNotFoundError:
    print(f"Input file {filename} not found.")
    
turtle.done()
