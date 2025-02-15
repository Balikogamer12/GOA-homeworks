from turtle import *

def draw_rectangle(x, y, width, height, fill_color="lightgray"):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor(fill_color)  # Use fillcolor() to set the color
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw_tower(x, y, width, height):
    draw_rectangle(x, y, width, height)
    for i in range(3):
        draw_rectangle(x + i * (width / 3), y + height, width / 3, width / 3)

def draw_wall():
    draw_rectangle(-250, -100, 500, 200)  # მთავარი სასახლის კედელი

def draw_arch(x, y, width, height):
    # დავხაზოთ კარის მართკუთხა სხეული
    draw_rectangle(x, y, width, height, "gray")
    
    # ახლა დავხაზოთ თაღი
    penup()
    goto(x + width / 2, y + height)  #  კარის ზედა ცენტრიდან დაწყება
    setheading(90)  # დააყენეთ სათაური ზევით
    pendown()
    
    # Draw the top half of the arch (curved top)
    penup()
    circle(width / 2, 180)  # Semi-circle for the arch at the top

def draw_gate():
    # Draw the gate (arch-shaped door) with width 120 and height 90
    draw_arch(-60, -100, 120, 90)
    
    # Draw the door handle centered on the door
    penup()
    goto(-10, -55)  # Center the handle horizontally
    pendown()
    begin_fill()
    color("gold")
    circle(7)  # Small circle for the door handle
    end_fill()

def draw_window(x, y, width, height):
    # Draw the window frame with a decorative color (black)
    draw_rectangle(x, y, width, height, "black")

    # Draw window panes (cross bars)
    penup()
    goto(x + width / 2, y)  # Middle of the window, bottom side
    setheading(90)
    pendown()
    forward(height)  # Vertical line of the window

    penup()
    goto(x, y + height / 2)  # Middle of the window, left side
    setheading(0)
    pendown()
    forward(width)  # Horizontal line of the window

def draw_flag(x, y):
    penup()
    goto(x, y)
    pendown()
    forward(20)
    right(90)
    forward(30)
    right(90)
    forward(20)
    right(90)
    forward(30)
    right(90)

def draw_roof(x, y, width):
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    forward(width / 2)
    left(120)
    forward(width)
    left(120)
    forward(width)
    left(120)
    forward(width / 2)
    end_fill()

def draw_castle():
    speed(12)
    width(7)
    bgcolor("lightblue")
    
    # დავხაზოთ მარცხენა კოშკი
    draw_tower(-250, -100, 80, 200)
    draw_roof(-210, 134, 100)
    
    # დავხაზოთ მარჯვენა კოშკი
    draw_tower(170, -100, 80, 200)
    draw_roof(210, 134, 100)
    
    # დავხაზოთ მთავარი კედელი
    draw_wall()
    
    # დავხაზოთ მარცხენა სახურავი
    draw_roof(-5, 100, 160)

    # ციხის კარიბჭის (კარის) დახატვა თაღით
    draw_gate()
  
    # ფანჯრების დახატვა (ჯვარედინი ზოლებით)
    draw_window(-210, -30, 40, 60)  # Left window
    draw_window(190, -30, 40, 60)   # Right window
    draw_window(-60, 30, 40, 60)    # Top-left window
    draw_window(20, 30, 40, 60)     # Top-right window
    
    hideturtle()
    done()

# გაშვების ბრძანება რომ სასახლე დაიხაზოს
<<<<<<< HEAD
draw_castle()
=======
draw_castle()
>>>>>>> 07ccc6af43e8bc38e849c95ef299cb32896120f3
