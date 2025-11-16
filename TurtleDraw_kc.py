import turtle
import math

screen = turtle.Screen()
screen.setup(width=450, height=450)
screen.title("TurtleDraw")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

filename = input("Enter the name of the input file: ")

try:
    with open(filename, 'r') as file:
        total_distance = 0
        prev_point = None
        
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.lower() == "stop":
                t.penup()
                prev_point = None
                continue

            parts = line.split()
            if len(parts) < 3:
                continue

            color = parts[0]
            try:
                x = float(parts[1])
                y = float(parts[2])
            except ValueError:
                continue

            t.color(color)
            
            if prev_point is None:
                t.goto(x, y)
                t.pendown()
            else:
                t.goto(x, y)
                distance = math.sqrt((x - prev_point[0])**2 + (y - prev_point[1])**2)
                total_distance += distance
            
            t.dot(6, color)
            prev_point = (x, y)
        
        t.penup()
        t.goto(200, -200)
        t.write(f"Total Distance: {total_distance:.2f}", align="right", font=("Arial", 12, "normal"))

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print("An error occurred:", e)

input("Press Enter to close the window...")
turtle.bye()

