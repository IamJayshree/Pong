import turtle
import os

con = turtle.Screen()
con.title("Pong By @iamcodegirl")
con.bgcolor("black")
con.setup(width=800, height=600)
#con.tracer(0) #speed up our game

#Score
score_a = 0
score_b = 0

#Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)  #co-ordinates of paddle A


#Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)  #co-ordinates of paddle A


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B:0",align="center",font=("Courier",24,"normal"))

#defining Functions for the game
def pad_a_up():
	y = pad_a.ycor()  #ycor fu in turtle module
	y += 20
	pad_a.sety(y)    #sety sets y coord

def pad_a_down():
	y = pad_a.ycor()  #ycor fu in turtle module
	y -= 20
	pad_a.sety(y)    #sety sets y coord

def pad_b_up():
	y = pad_b.ycor()  #ycor fu in turtle module
	y += 20
	pad_b.sety(y)    #sety sets y coord

def pad_b_down():
	y = pad_b.ycor()  #ycor fu in turtle module
	y -= 20
	pad_b.sety(y)    #sety sets y coord

#keyboard Controls
con.listen()
con.onkeypress(pad_a_up,"w")
con.onkeypress(pad_a_down,"s")
con.onkeypress(pad_b_up,"Up")
con.onkeypress(pad_b_down,"Down")  #paddle B moves with arroy keys
 
#Main game loop
while True:
	con.update()

	#Move the Ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border Constraints
	#Since height is 600, so up coord is 300 down is -300 and ball size is 20 px
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1 #reversing ball direction
		os.system("aplay bounce.mp3")

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1 #reversing ball direction

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1 #reversing ball direction
		score_a += 1
		pen.clear()
		pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1 #reversing ball direction
		score_b += 1
		pen.clear()
		pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

	#Collision
	if ball.xcor() > 340 and ball.xcor() < 350 and (ball.xcor() < pad_b.xcor() + 40 and ball.ycor() > pad_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1

	if ball.xcor() < -340 and ball.xcor() > -350 and (ball.xcor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1






turtle.done()

