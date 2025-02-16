from turtle import *

speed(12)
bgcolor("lightblue")
width(7)

# Draw left tower
penup()
goto(-250, -100)
color("black")
pendown()
for _ in range(2):
    forward(80)
    left(90)
    forward(200)
    left(90)
for i in range(3):
    penup()
    goto(-250 + i * (80 / 3), 100)
    pendown()
    for _ in range(2):
        forward(80 / 3)
        left(90)
        forward(80 / 3)
        left(90)

# Draw left roof
penup()
goto(-210, 134)
pendown()
forward(50)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(50)

# Draw right tower
penup()
goto(170, -100)
pendown()
for _ in range(2):
    forward(80)
    left(90)
    forward(200)
    left(90)
for i in range(3):
    penup()
    goto(170 + i * (80 / 3), 100)
    pendown()
    for _ in range(2):
        forward(80 / 3)
        left(90)
        forward(80 / 3)
        left(90)

# Draw right roof
penup()
goto(210, 134)
pendown()
forward(50)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(50)

# Draw main wall
penup()
goto(-250, -100)
pendown()
for _ in range(2):
    forward(500)
    left(90)
    forward(200)
    left(90)

# Draw main roof
penup()
goto(-5, 100)
color("black")
pendown()
forward(80)
left(120)
forward(160)
left(120)
forward(160)
left(120)
forward(80)

# Draw gate
penup()
goto(-60, -100)
pendown()
for _ in range(2):
    forward(120)
    left(90)
    forward(90)
    left(90)

# Draw windows
for x, y in [(-230, -30), (190, -30), (-60, 30), (20, 30)]:
    penup()
    goto(x, y)
    color("black")
    pendown()
    for _ in range(2):
        forward(40)
        left(90)
        forward(60)
        left(90)
    penup()
    goto(x + 20, y)
    pendown()
    left(90)
    forward(60)
    penup()
    goto(x, y + 30)
    pendown()
    right(90)
    forward(40)

    # draw door handle
    penup()
    goto(-3, -55)  # Center the handle horizontally
    pendown()
    begin_fill()
    color("gold")
    circle(7)  # Small circle for the door handle
    end_fill()

hideturtle()
done()