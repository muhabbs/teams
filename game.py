import turtle
kys = turtle.Screen()
kys.title("Pong game (shoutout:playboycarti)")
kys.bgcolor("green")
kys.setup(width=800, height=600)
kys.tracer(0)
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("black")
p1.shapesize(stretch_wid=6, stretch_len=2)
p1.penup()
p1.goto(-350, 0)

p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("black")
p2.shapesize(stretch_wid=6, stretch_len=2)
p2.penup()
p2.goto(350, 0)

# Ball
RIP= turtle.Turtle()
RIP.speed(0)
RIP.shape("circle")
RIP.color("blue")
RIP.penup()
RIP.goto(0, 0)
RIP.dx = 0.3
RIP.dy = -0.3
leftp = 0
rightp = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Leftp: 0  Rightp: 0", align="center", font=("Courier", 24, "normal"))
def paddleaup():
    y = p1.ycor()
    y =y+20
    p1.sety(y)
def paddleadown():
    y = p1.ycor()
    y =y-20
    p1.sety(y)
def paddlebup():
    y = p2.ycor()
    y =y+20
    p2.sety(y)
def paddlebdown():
    y = p2.ycor()
    y -= 20
    p2.sety(y)
kys.listen()
kys.onkeypress(paddleaup, "w")
kys.onkeypress(paddleadown, "s")
kys.onkeypress(paddlebup, "Up")
kys.onkeypress(paddlebdown, "Down")
while True:
    kys.update()
    RIP.setx(RIP.xcor() + RIP.dx)
    RIP.sety(RIP.ycor() + RIP.dy)
    if RIP.ycor() > 280:
        RIP.sety(280)
        RIP.dy *= -1
    if RIP.ycor() < -280:
        RIP.sety(-280)
        RIP.dy *= -1
    if (RIP.xcor() > 340 and RIP.xcor() < 350) and (RIP.ycor() < p2.ycor() + 50 and RIP.ycor() > p2.ycor() - 50):
        RIP.setx(340)
        RIP.dx *= -1
    if (RIP.xcor() < -340 and RIP.xcor() > -350) and (RIP.ycor() < p1.ycor() + 50 and RIP.ycor() > p1.ycor() - 50):
        RIP.setx(-340)
        RIP.dx *= -1
    if RIP.xcor() > 390:
        RIP.goto(0, 0)
        leftp =leftp+1
        sketch.clear()
        sketch.write("Leftp: {}  Right_player: {}".format(leftp, rightp), align="center", font=("Courier", 24, "normal"))
    if RIP.xcor() < -390:
        RIP.goto(0, 0)
        rightp= 1
        sketch.clear()
        sketch.write("Left_player: {}  Right_player: {}".format(leftp, rightp), align="center", font=("Courier", 24, "normal"))
