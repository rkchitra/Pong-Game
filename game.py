import turtle
import winsound

#create a window for the game 
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
#In the game, (0,0) is in the center; x-coordinates go from -400 to 400; y-coordinates from -300 to 300
wn.tracer(0) #stops the window from updating; has to be done manually 

#Scores 
score_a = 0
score_b = 0

#Paddle A : Left Paddle
paddle_a = turtle.Turtle() #create a turtle object
paddle_a.speed(0) #speed of animation; this is set to max possible speed 
paddle_a.shape("square") #there's several such shapes available
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #default is 20px for both; making the width 5 times the default one 
paddle_a.penup() #prevents it from drawing lines by default
paddle_a.goto(-350,0)
#Paddle B : Right Paddle
paddle_b = turtle.Turtle() #create a turtle object
paddle_b.speed(0) #speed of animation; this is set to max possible speed 
paddle_b.shape("square") #there's several such shapes available
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #default is 20px for both; making the width 5 times the default one 
paddle_b.penup() #prevents it from drawing lines by default
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle() #create a turtle object
ball.speed(0) #speed of animation; this is set to max possible speed 
ball.shape("circle") #there's several such shapes available
ball.color("white")
ball.penup() #prevents it from drawing lines by default
ball.goto(0,0)

#move the ball by 2 px 
ball.dx = 0.2
ball.dy = -0.2

#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #We want to view just the text, not the turtle object
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

#Final score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-20,0)

#Functions

def paddle_a_up() :
    y = paddle_a.ycor() #current y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down() :
    y = paddle_a.ycor() #current y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up() :
    y = paddle_b.ycor() #current y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down() :
    y = paddle_b.ycor() #current y coordinate
    y -= 20
    paddle_b.sety(y)

def quit() :
    paddle_a.reset()
    paddle_b.reset()
    ball.reset()
    if score_a > score_b :
        score.write("Player A Wins!",align="center", font=("Courier",30,"normal"))
        winsound.PlaySound("win.wav",winsound.SND_ASYNC)
    elif score_b > score_a :
        score.write("Player B Wins!",align="center", font=("Courier",30,"normal"))
        winsound.PlaySound("win.wav",winsound.SND_ASYNC)
    else :
        score.write("It's a Draw!", align="center", font=("Courier",30,"normal"))
        winsound.PlaySound("tie.wav",winsound.SND_ASYNC)

    global running
    running = False

#keyboard binding
wn.listen() #listens for keyboard input
wn.onkeypress(paddle_a_up,"w") #When the user presses w, calls the paddle_a_up()
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

wn.onkeypress(quit,"q")

running = True
#Main game loop
while running : 
    wn.update() #updates the screen every time the loop runs 

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking 
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.xcor() > 390 : 
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    #Collisions with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40) :
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 
wn.mainloop()
        
