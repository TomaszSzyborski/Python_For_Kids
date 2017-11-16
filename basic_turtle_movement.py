# allows us to use the turtles library
import turtle               

# methods to help with setup of out turtle
import helpers

# creates a graphics window
window = turtle.Screen()

helpers.set_background_image_from_image_url(window)

# create a turtle named "tom"
tom = turtle.Turtle()

# reshapes tom from arrow to turtle
tom.shape("turtle")      

# places the stamp of the turtle shape 
tom.stamp()

# tell tom to move forward by 150 units
tom.forward(150)
tom.stamp()

# turn by 90 degrees
tom.left(90)

# complete the second side of a rectangle
tom.forward(75)
tom.stamp()

# turn by 90 degrees
tom.left(90)

# complete the third side of rectangle
tom.forward(150)
tom.stamp()

# turn by 90 degrees
tom.left(90)

# complete last side of a rectangle
tom.forward(75)

# wait for click to close the window
window.exitonclick()
# closes the window
# window.close()