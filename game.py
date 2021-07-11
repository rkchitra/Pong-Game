import turtle

#create a window for the game 
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) #stops the window from updating; has to be done manually 

#Main game loop
while True : 
    wn.update() #updates the screen every time the loop runs 
    