import turtle

screen = turtle.Screen()

turtle = turtle.Turtle()
turtle.pensize(5)
turtle.speed(3)

turtle .penup()
turtle .goto(-120, 0)   
turtle .pendown()
turtle .pencolor("blue")
turtle .circle(50)

turtle .penup()
turtle .goto(0, 0)      
turtle .pendown()
turtle .pencolor("black")
turtle .circle(50)

turtle .penup()
turtle .goto(120, 0)    
turtle .pendown()
turtle .pencolor("red")
turtle .circle(50)

turtle .penup()
turtle .goto(-60, -50)  
turtle .pendown()
turtle .pencolor("yellow")
turtle .circle(50)

turtle .penup()
turtle .goto(60, -50)   
turtle .pendown()
turtle .pencolor("green")
turtle .circle(50)

turtle .hideturtle()
turtle.done()


