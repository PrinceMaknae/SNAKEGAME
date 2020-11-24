import turtle
import random
import time

delay= 0.1
#set up for screen
wn=turtle.Screen()
wn.title("Snake Game by Keithzxc")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
head=turtle.Turtle()
head.speed(0)
head.color("pink")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0)
food.color("yellow")
food.shape("circle")
food.penup()
food.goto(0,100)

segments=[]

#functions
def go_up():
    head.direction="up"

def go_down():
    head.direction="down"
    
def go_left():
    head.direction="left"

def go_right():
    head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#Keyboard Press
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main Game Loop
while True:
    wn.update()
    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    for segment in segments:
            segment.goto(1000, 1000)
            segments.clear()

    segments.clear()

    #Snake food collision
    if head.distance(food) < 20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

  
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    time.sleep(delay)

wn.mainloop()