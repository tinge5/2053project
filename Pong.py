import turtle
import time
t = turtle.Screen()
t.title("Turner's Game")
t.setup(width=1000, height=500)
t.bgcolor("black")

p2 = 0
p1 = 0
title = turtle.Turtle()
title.shape("circle")
title.shapesize(stretch_wid=.5, stretch_len=.5)
title.speed(2)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0,200)
title.write("PONG", align="center", font=("arial", 20, "normal"))

score1 = turtle.Turtle()
score1.speed(0)
score1.penup()
score1.color("white")
score1.hideturtle()
score1.goto(-450,200)
score1.write("Player2: {}" .format(p2), align="left", font=("arial", 20, "italic"))

score2 = turtle.Turtle()
score2.speed(0)
score2.color("white")
score2.penup()
score2.hideturtle()
score2.goto(450,200)
score2.write("Player1: {}" .format(p1), align="right", font=("arial", 20, "italic"))

intro = turtle.Turtle()
intro.speed(0)
intro.color("gray")
intro.goto(0,0)
intro.hideturtle()
intro.write("Welcome to Turner's Pong\n     Press space to start", align="Center", font=("arial", 50, "bold"))


goal = turtle.Turtle()
goal.speed(10)
goal.color("turquoise")
goal.goto(0,0)
goal.hideturtle()
goal.penup()
goal.write("GOALLLLLL!!!!", align="Center", font=("Times New Roman", 40, "bold"))
goal.clear()
    
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("gray")
instructions.penup()
instructions.hideturtle()
instructions.goto(170, 200)
instructions.write("Use 'up' and 'down' to move \n press 'p' to pause 'r' to resume", align="center", font=("arial", 10, "bold"))

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=6, stretch_len=2)
paddle.color("blue")
paddle.penup()
paddle.goto(485, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=6, stretch_len=2)
paddle2.color("orange")
paddle2.penup()
paddle2.goto(-485, 0)
paddle2.dy = 25
paddle2.dx = 0

ball = turtle.Turtle()

ball.shape("circle")
ball.color("yellow")
ball.shapesize(stretch_wid=1.5)
ball.goto(0,0)
ball.dx = 15
ball.dy = -15

waiting = True
pause = False
play = True

over = turtle.Turtle()
over.speed(0)
over.color("gray")
over.penup()
over.hideturtle()
over.goto(-170, 200)
over.write("First to 3 wins", align="center", font=("arial", 20, "bold"))

winner = turtle.Turtle()
winner.color("magenta")
winner.goto(0,0)
winner.hideturtle()

loser = turtle.Turtle()
loser.color("red")
loser.goto(0,0)
loser.hideturtle()

replay = turtle.Turtle()
replay.color("white")
replay.hideturtle()
replay.penup()
replay.goto(0, -50)

p = turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.hideturtle()
p.shapesize(stretch_wid=8, stretch_len=1.5)
p.penup()
p.goto(-25, 0)


j = turtle.Turtle()
j.speed(0)
j.shape("square")
j.color("white")
j.hideturtle()
j.shapesize(stretch_wid=8, stretch_len=1.5)
j.penup()
j.goto(25, 0)

def play():
    global pause
    pause = False
def paus():
    global pause
    pause = True

def ready(): 
    global waiting 
    waiting = False
    intro.clear()
    instructions.clear()
    over.clear()
    
def rep():
    global con
    con = False
    
def paddleup():
    paddle.dy = 10
    if not paddle.ycor() > 180:
        paddle.sety(paddle.ycor() + paddle.dy)
def paddledown():
    paddle.dy = -10
    if not paddle.ycor() < -180:
        paddle.sety(paddle.ycor() + paddle.dy)

x = 500
def goal2():
    goal.goto(x, 0)
    goal.write("GOALLLLLL!!!!", align="Center", font=("Times New Roman", 40, "bold"))
    goal.clear()
    
t.listen()
t.onkeypress(ready, "space")
t.onkeypress(paddleup, "Up")
t.onkeypress(paddledown, "Down")
t.onkeypress(rep, "x")
t.onkeypress(paus, "p")
t.onkeypress(play, "r")
while waiting:
    t.update()
    time.sleep(.8)
    intro.clear()
    over.clear()
    time.sleep(.8)
    intro.write("Welcome to Turner's Pong\n     Press space to start", align="Center", font=("arial", 50, "bold"))
    over.write("First to 3 wins", align="center", font=("arial", 20, "bold"))

con = True
intro.clear()
over.clear()
test = True
while test:
        loser.clear()
        winner.clear()
        replay.clear()
        con = True
        t.update()
        if pause:
            while pause:
                p.showturtle()
                j.showturtle()
                t.update()
        p.hideturtle()
        j.hideturtle()
        time.sleep(0.01)
        if paddle2.ycor() > 180:
            paddle2.sety(180)
            paddle2.dy *=-1
        if paddle2.ycor() < -180:
            paddle2.sety(-180)
            paddle2.dy *=-1
        paddle2.sety(paddle2.ycor() + paddle2.dy)
        ball.penup()
        if ball.xcor() > 495:
            p2+=1
            ball.goto(0,0)
            x = 500
            while x > -499:
                goal2()
                t.update()
                x-=50
            
            ball.dy *=-1
            ball.dx *=1
            score1.clear()
            paddle2.sety(0)
            score1.write("Player2: {}" .format(p2), align="left", font=("arial", 20, "italic"))
            if p2 == 3:
                ball.color("black")
                score1.clear()
                score2.clear()
                title.clear()
                over.clear()
                
                while con:
                    t.update()
                    time.sleep(.6)
                    loser.clear()
                    time.sleep(.6)
                    loser.write("Loser", align="center", font=("Arial", 50, "bold"))
                    replay.write("Press x to restart", align="center", font=("arial", 30, "bold"))
                p1 = 0
                p2 = 0
                score2.write("Player1: {}" .format(p1), align="right", font=("arial", 20, "italic"))
                score1.write("Player2: {}" .format(p2), align="left", font=("arial", 20, "italic"))
                ball.color("yellow")
                title.write("PONG", align="center", font=("arial", 20, "normal"))
            continue
        if ball.xcor() < -495:
            p1+=1
            ball.goto(0,0)
            x = -500
            while x < 499:
                goal2()
                t.update()
                x+=50
            ball.dy *=-1
            ball.dx *=-1
            score2.clear()
            paddle2.sety(0)
            score2.write("Player1: {}" .format(p1), align="right", font=("arial", 20, "italic"))
            if p1 == 3:
                ball.clear()
                ball.color("black")
                score1.clear()
                score2.clear()
                title.clear()
                over.clear()
                
                while con:
                    t.update()
                    time.sleep(.6)
                    winner.clear()
                    time.sleep(.6)
                    winner.write("Winner", align="center", font=("Arial", 50, "bold"))
                    replay.write("Press x to restart", align="center", font=("arial", 30, "bold"))
                p1 = 0
                p2 = 0
                score2.write("Player1: {}" .format(p1), align="right", font=("arial", 20, "italic"))
                score1.write("Player2: {}" .format(p2), align="left", font=("arial", 20, "italic"))
                ball.color("yellow")
                title.write("PONG", align="center", font=("arial", 20, "normal"))
                
            continue     
                    
        if ball.xcor() > 445:
            if ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50:
                ball.setx(445)
                ball.dx *=-1
        if ball.xcor() < -445:
            if ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
                ball.setx(-445)
                ball.dx *=-1
        if ball.ycor() > 225:
            ball.dy = -5
        if ball.ycor() < -225:
            ball.dy = 5
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
turtle.done()