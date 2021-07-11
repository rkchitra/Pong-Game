import turtle

#create a window for the game 
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
#In the game, (0,0) is in the center; x-coordinates go from -400 to 400; y-coordinates from -300 to 300
wn.tracer(0) #stops the window from updating; has to be done manually 

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
ball.shape("square") #there's several such shapes available
ball.color("white")
ball.penup() #prevents it from drawing lines by default
ball.goto(0,0)

#move the ball by 2 px 
ball.dx = 0.1
ball.dy = 0.1

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

#keyboard binding
wn.listen() #listens for keyboard input
wn.onkeypress(paddle_a_up,"w") #When the user presses w, calls the paddle_a_up()
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main game loop
while True : 
    wn.update() #updates the screen every time the loop runs 

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking 
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball
    
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390 : 
        ball.goto(0,0)
        ball.dx *= -1
    
    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
