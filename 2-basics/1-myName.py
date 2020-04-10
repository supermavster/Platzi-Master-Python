# Make Squared

# Library - Generate Graphics
import turtle

# set and generate a window with turtle
window = turtle.Screen()

# make a Turtle
mavs = turtle.Turtle()

## Generar lineas y dar vueltas de 90°

# Move
# A -> B
mavs.left(90) # Turn 90°
mavs.forward(50) # Make Line -> 50
mavs.right(90) # Turn 90°

# B -> C
mavs.forward(50) # Make Line -> 50
mavs.right(90) # Turn 90°

# C -> D
mavs.forward(50) # Make Line -> 50
mavs.left(90) # Turn 90°

# # D -> C
mavs.forward(0) # Make Line -> 50
mavs.left(90) # Turn 90°

# # C -> E
mavs.forward(50) # Make Line -> 50
mavs.right(90) # Turn 90°

# # E -> F
mavs.forward(50) # Make Line -> 50
mavs.right(90) # Turn 90°

# # E -> F
mavs.forward(50) # Make Line -> 50
mavs.right(90) # Turn 90°

# Miguel


#  B ----- C ----- E
# |       |       |
# |       |       |
# A       D       F  


# Stay the window
turtle.mainloop()