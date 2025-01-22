from turtle import *




#we want to paint house

#step 1:  draw a square
speed(4)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#drawing door

forward(70)
color("yellow") 
begin_fill()
left(90) 
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


# Window 1


penup()
goto(68, 190)
pendown()
begin_fill()
color("blue")
begin_fill()
left(30)
forward(58)
right(90)
forward(55)
right(90)
forward(58)
right(90)
forward(56)

penup()
goto(129, 190)
pendown()
right(90)
forward(58)
left(90)
forward(58)
left(90)
forward(58)
left(90)
forward(58)
end_fill()


penup()
goto(500, -500)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(1200)
    right(90)
    forward(493)
    right(90)
end_fill()







    
    

    



exitonclick()
