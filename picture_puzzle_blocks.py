#-----Assignment Description-----------------------------------------#
#
#  PICTURE PUZZLE BLOCKS
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "stack_blocks".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a pile of picture puzzle blocks
#  whose arrangement is determined by data stored in a list which
#  specifies the blocks' locations.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

#
#--------------------------------------------------------------------#



#-----Functions for Managing the Canvas------------------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Set the coordinate system so that location (0, 0) is centred on
    # the point where the blocks will be stacked
    setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
                        canvas_width / 2, canvas_height - top_and_bottom_border)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 50 # pixels
    penup()
    goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(top_and_bottom_border + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(top_and_bottom_border + overlap)
    end_fill()
    penup()

    # Draw a friendly sun peeking into the image
    goto(-canvas_width / 2, block_size * 2)
    color('yellow')
    dot(250)

    # Reset everything ready for the student's solution
    color('black')
    width(2)
    penup()
    home()
    setheading(0)
    tracer(True)
    

# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

    # Go to each coordinate, draw a dot and print the coordinate, in the given colour
    def draw_each_coordinate(colour):
        color(colour)
        for x_coord, y_coord in coordinates:
            goto(x_coord, y_coord)
            dot(4)
            write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

    # Don't draw lines between the coordinates
    penup()

    # The list of coordinates to display
    coordinates = []

    # Only mark the corners if the corresponding argument is True
    if show_corners:
        coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
                       [-block_size, block_size], [0, block_size], [block_size, block_size],
                       [-block_size, 0], [0, 0], [block_size, 0]]
        draw_each_coordinate('dark blue')

    # Only mark the centres if the corresponding argument is True
    if show_centres:
        coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
                       [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
        draw_each_coordinate('red')

    # Put the cursor back how it was
    color('black')
    home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# the blocks:
#
# 1. The name of the block, from 'Block A' to 'Block D'
# 2. The place to put the block, either 'Top left', 'Top right',
#    'Bottom left' or 'Bottom right'
# 3. The block's orientation, meaning the direction in which the top
#    of the block is pointing, either 'Up', 'Down', 'Left' or 'Right'
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#

# The following data set doesn't require drawing any blocks
# at all.  You may find it useful as a dummy argument when you
# first start developing your "stack_blocks" function.

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up']]
arrangement_02 = [['Block B', 'Bottom right', 'Up']]
arrangement_03 = [['Block C', 'Bottom left', 'Up']]
arrangement_04 = [['Block D', 'Bottom right', 'Up']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down']]
arrangement_11 = [['Block A', 'Bottom right', 'Left']]
arrangement_12 = [['Block A', 'Bottom left', 'Right']]

arrangement_13 = [['Block B', 'Bottom left', 'Down']]
arrangement_14 = [['Block B', 'Bottom right', 'Left']]
arrangement_15 = [['Block B', 'Bottom left', 'Right']]

arrangement_16 = [['Block C', 'Bottom left', 'Down']]
arrangement_17 = [['Block C', 'Bottom right', 'Left']]
arrangement_18 = [['Block C', 'Bottom left', 'Right']]

arrangement_19 = [['Block D', 'Bottom left', 'Down']]
arrangement_20 = [['Block D', 'Bottom right', 'Left']]
arrangement_21 = [['Block D', 'Bottom left', 'Right']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up'],
                  ['Block D', 'Top right', 'Up']]
arrangement_31 = [['Block A', 'Top left', 'Up'],
                  ['Block C', 'Bottom left', 'Up']]

arrangement_32 = [['Block B', 'Bottom right', 'Up'],
                  ['Block D', 'Bottom left', 'Up'],
                  ['Block C', 'Top right', 'Up']]
arrangement_33 = [['Block B', 'Bottom right', 'Up'],
                  ['Block D', 'Bottom left', 'Up'],
                  ['Block A', 'Top left', 'Up']]
arrangement_34 = [['Block B', 'Bottom left', 'Up'],
                  ['Block A', 'Bottom right', 'Up'],
                  ['Block D', 'Top left', 'Up'],
                  ['Block C', 'Top right', 'Up']]

arrangement_40 = [['Block C', 'Bottom right', 'Left'],
                  ['Block D', 'Top right', 'Right']]
arrangement_41 = [['Block A', 'Top left', 'Down'],
                  ['Block C', 'Bottom left', 'Up']]

arrangement_42 = [['Block B', 'Bottom right', 'Left'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block C', 'Top right', 'Down']]
arrangement_43 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block A', 'Top left', 'Right']]
arrangement_44 = [['Block B', 'Bottom left', 'Down'],
                  ['Block A', 'Bottom right', 'Left'],
                  ['Block D', 'Top left', 'Right'],
                  ['Block C', 'Top right', 'Up']]

arrangement_50 = [['Block B', 'Bottom right', 'Left'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block C', 'Top right', 'Down']]
arrangement_51 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block A', 'Top left', 'Right']]
arrangement_52 = [['Block B', 'Bottom left', 'Down'],
                  ['Block A', 'Bottom right', 'Left'],
                  ['Block D', 'Top left', 'Right'],
                  ['Block C', 'Top right', 'Up']]

arrangement_60 = [['Block B', 'Bottom right', 'Left'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block C', 'Top right', 'Down']]
arrangement_61 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block A', 'Top left', 'Right']]
arrangement_62 = [['Block B', 'Bottom left', 'Down'],
                  ['Block A', 'Bottom right', 'Left'],
                  ['Block D', 'Top left', 'Right'],
                  ['Block C', 'Top right', 'Up']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left'],
                  ['Block D', 'Top right', 'Left'],
                  ['Block A', 'Bottom left', 'Left'],
                  ['Block B', 'Top left', 'Left']]

arrangement_81 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Right'],
                  ['Block A', 'Top right', 'Right'],
                  ['Block C', 'Top left', 'Right']]

arrangement_89 = [['Block A', 'Bottom right', 'Down'],
                  ['Block C', 'Top right', 'Down'],
                  ['Block B', 'Bottom left', 'Down'],
                  ['Block D', 'Top left', 'Down']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up'],
                  ['Block D', 'Bottom right', 'Up'],
                  ['Block B', 'Top right', 'Up'],
                  ['Block A', 'Top left', 'Up']]

arrangement_91 = [['Block D', 'Bottom right', 'Up'],
                  ['Block C', 'Bottom left', 'Up'],
                  ['Block A', 'Top left', 'Up'],
                  ['Block B', 'Top right', 'Up']]

arrangement_92 = [['Block D', 'Bottom right', 'Up'],
                  ['Block B', 'Top right', 'Up'],
                  ['Block C', 'Bottom left', 'Up'],
                  ['Block A', 'Top left', 'Up']]

arrangement_99 = [['Block C', 'Bottom left', 'Up'],
                  ['Block D', 'Bottom right', 'Up'],
                  ['Block A', 'Top left', 'Up'],
                  ['Block B', 'Top right', 'Up']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "stack_blocks" function.
#

#Defining a variable for the width of the letters "D" and "C" of the logo
letter_width = 25

#Drawing "Block A"
def Draw_Block_A():
    
    #Drawing the red background
    fillcolor("red")
    begin_fill()
    pendown()
    forward(block_size)
    right(90)
    penup()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    pendown()
    forward(block_size)
    right(90)
    penup()
    end_fill()

    #Drawing the gold "D"
    forward(block_size)
    right(90)
    forward(letter_width)
    right(90)
    pendown()
    fillcolor("gold")
    begin_fill()
    forward(block_size - letter_width)
    left(90)
    forward(block_size - letter_width)
    left(90)
    penup()
    forward(letter_width)
    pendown()
    left(90)
    forward(block_size - (letter_width*2))
    right(90)
    forward(block_size - (letter_width*2))
    end_fill()

    #Drawing the white "C"
    right(180)
    pendown()
    fillcolor("white")
    begin_fill()
    circle(block_size - (letter_width*2), extent = 90)
    left(90)
    penup()
    forward(letter_width)
    left(90)
    pendown()
    circle(-(block_size - (letter_width*3)), extent = 90)
    left(90)
    penup()
    forward(letter_width)
    end_fill()

    #Drawing the gold "lightning bolt"
    fillcolor("gold")
    begin_fill()
    backward(125)
    left(125)
    pendown()
    forward(131)
    left(145)
    penup()
    forward(108)
    left(90)
    forward(74)
    end_fill()

    #Resetting the turtle orientation
    setheading(0)

#Drawing "Block B"
def Draw_Block_B():
    
    #Drawing the red background
    fillcolor("red")
    begin_fill()
    pendown()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    penup()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    end_fill()

    #Drawing the gold "D"
    right(90)
    forward(letter_width)
    left(90)
    pendown()
    fillcolor("gold")
    begin_fill()
    circle(-(block_size - letter_width), extent = 90)
    right(90)
    penup()
    forward(letter_width)
    right(90)
    pendown()
    circle(block_size - (letter_width*2), extent = 90)
    right(90)
    penup()
    forward(letter_width)
    end_fill()

    #Drawing the white "C"
    backward(letter_width)
    right(90)
    pendown()
    fillcolor("white")
    begin_fill()
    forward(block_size - letter_width)
    right(90)
    forward(letter_width)
    right(90)
    forward(block_size - letter_width)
    right(90)
    penup()
    forward(letter_width)
    end_fill()

    #Drawing the gold "lightning bolt"
    forward(letter_width*2)
    right(90)
    forward(block_size)
    right(145)
    pendown()
    fillcolor("gold")
    begin_fill()
    forward(305.5)
    penup()
    backward(305.5)
    left(15)
    pendown()
    forward(300)
    left(130)
    forward(79)
    right(145)
    forward(35)
    right(35)
    penup()
    forward(108)
    right(90)
    forward(74)
    end_fill()

    #Resetting the turtle orientation
    setheading(0)

#Drawing "Block C"
def Draw_Block_C():
    
    #Drawing the red background
    fillcolor("red")
    begin_fill()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    pendown()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    penup()
    end_fill()

    #Drawing the gold "D"
    forward(letter_width)
    right(90)
    pendown()
    fillcolor("gold")
    begin_fill()
    forward(block_size - letter_width)
    left(90)
    forward(block_size - letter_width)
    left(90)
    penup()
    forward(letter_width)
    pendown()
    left(90)
    forward(block_size - (letter_width*2))
    right(90)
    forward(block_size - (letter_width*2))
    end_fill()

    #Drawing the white "C"
    penup()
    forward(letter_width)
    right(180)
    forward(letter_width)
    pendown()
    fillcolor("white")
    begin_fill()
    circle(block_size - (letter_width*2), extent = 90)
    left(90)
    penup()
    forward(letter_width)
    left(90)
    pendown()
    circle(-(block_size - (letter_width*3)), extent = 90)
    left(90)
    penup()
    forward(letter_width)
    end_fill()

    #Drawing the gold "lightning bolt"
    forward(letter_width*2)
    left(90)
    forward(block_size)
    left(125)
    pendown()
    fillcolor("gold")
    begin_fill()
    forward(304)
    penup()
    backward(304)
    left(15)
    pendown()
    forward(300)
    left(130)
    forward(79)
    right(145)
    forward(35)
    right(35)
    penup()
    forward(108)
    right(90)
    forward(74)
    end_fill()

    #Resetting the turtle orientation
    setheading(0)

#Drawing "Block D"    
def Draw_Block_D():
    
    #Drawing the red background
    fillcolor("red")
    begin_fill()
    forward(block_size)
    right(90)
    pendown()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    penup()
    forward(block_size)
    right(90)
    end_fill()

    #Drawing the gold "D"
    forward(block_size - letter_width)
    right(90)
    pendown()
    fillcolor("gold")
    begin_fill()
    circle(-(block_size - letter_width), extent = 90)
    right(90)
    penup()
    forward(letter_width)
    right(90)
    pendown()
    circle(block_size - (letter_width*2), extent = 90)
    right(90)
    penup()
    forward(letter_width)
    end_fill()

    #Drawing the white "C"
    backward(letter_width)
    right(90)
    pendown()
    penup()
    circle(-(block_size - (letter_width*2)), extent = 90)
    right(180)
    pendown()
    fillcolor("white")
    begin_fill()
    forward(block_size - letter_width)
    left(90)
    forward(letter_width)
    left(90)
    forward(block_size - letter_width)
    end_fill()

    #Drawing the gold "lightning bolt"
    left(90)
    penup()
    backward(block_size - (letter_width*3))
    fillcolor("gold")
    begin_fill()
    forward(letter_width*3)
    left(125)
    pendown()
    forward(131)
    left(145)
    penup()
    forward(108)
    left(90)
    forward(74)
    end_fill()

    #Resetting the turtle orientation
    setheading(0)
            
#Defining a function to position each block according to the given arrangement    
def stack_blocks(data_set):
    for element in data_set:

        #Positioning "Block A" according to the given position and orientation
        if element[0] == "Block A":
            if element [1] == "Top left":
                if element [2] == "Up":
                    goto(-250, 500)
                elif element [2] == "Down":
                    goto(0, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 250)
                    setheading(90)
                else:
                    goto(0, 500)
                    setheading(270)
            elif element [1] == "Top right":
                if element [2] == "Up":
                    goto(0, 500)
                elif element [2] == "Down":
                    goto(250, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 250)
                    setheading(90)
                else:
                    goto(250, 500)
                    setheading(270)
            elif element [1] == "Bottom left":
                if element [2] == "Up":
                    goto(-250, 250)
                elif element [2] == "Down":
                    goto(0, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 0)
                    setheading(90)
                else:
                    goto(0, 250)
                    setheading(270)
            else:
                if element [2] == "Up":
                    goto(0, 250)
                elif element [2] == "Down":
                    goto(250, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 0)
                    setheading(90)
                else:
                    goto(250, 250)
                    setheading(270)
                    
            #Calling the predefined function to draw "Block A"
            Draw_Block_A()

        #Positioning "Block B" according to the given position and orientation
        elif element[0] == "Block B":
            if element [1] == "Top left":
                if element [2] == "Up":
                    goto(-250, 500)
                elif element [2] == "Down":
                    goto(0, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 250)
                    setheading(90)
                else:
                    goto(0, 500)
                    setheading(270)
            elif element [1] == "Top right":
                if element [2] == "Up":
                    goto(0, 500)
                elif element [2] == "Down":
                    goto(250, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 250)
                    setheading(90)
                else:
                    goto(250, 500)
                    setheading(270)
            elif element [1] == "Bottom left":
                if element [2] == "Up":
                    goto(-250, 250)
                elif element [2] == "Down":
                    goto(0, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 0)
                    setheading(90)
                else:
                    goto(0, 250)
                    setheading(270)
            else:
                if element [2] == "Up":
                    goto(0, 250)
                elif element [2] == "Down":
                    goto(250, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 0)
                    setheading(90)
                else:
                    goto(250, 250)
                    setheading(270)
                    
            #Calling the predefined function to draw "Block B"
            Draw_Block_B()

        #Positioning "Block C" according to the given position and orientation
        elif element[0] == "Block C":
            if element [1] == "Top left":
                if element [2] == "Up":
                    goto(-250, 500)
                elif element [2] == "Down":
                    goto(0, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 250)
                    setheading(90)
                else:
                    goto(0, 500)
                    setheading(270)
            elif element [1] == "Top right":
                if element [2] == "Up":
                    goto(0, 500)
                elif element [2] == "Down":
                    goto(250, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 250)
                    setheading(90)
                else:
                    goto(250, 500)
                    setheading(270)
            elif element [1] == "Bottom left":
                if element [2] == "Up":
                    goto(-250, 250)
                elif element [2] == "Down":
                    goto(0, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 0)
                    setheading(90)
                else:
                    goto(0, 250)
                    setheading(270)
            else:
                if element [2] == "Up":
                    goto(0, 250)
                elif element [2] == "Down":
                    goto(250, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 0)
                    setheading(90)
                else:
                    goto(250, 250)
                    setheading(270)
                    
            #Calling the predefined function to draw "Block C"
            Draw_Block_C()

        #Positioning "Block D" according to the given position and orientation 
        else:
            if element [1] == "Top left":
                if element [2] == "Up":
                    goto(-250, 500)
                elif element [2] == "Down":
                    goto(0, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 250)
                    setheading(90)
                else:
                    goto(0, 500)
                    setheading(270)
            elif element [1] == "Top right":
                if element [2] == "Up":
                    goto(0, 500)
                elif element [2] == "Down":
                    goto(250, 250)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 250)
                    setheading(90)
                else:
                    goto(250, 500)
                    setheading(270)
            elif element [1] == "Bottom left":
                if element [2] == "Up":
                    goto(-250, 250)
                elif element [2] == "Down":
                    goto(0, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(-250, 0)
                    setheading(90)
                else:
                    goto(0, 250)
                    setheading(270)
            else:
                if element [2] == "Up":
                    goto(0, 250)
                elif element [2] == "Down":
                    goto(250, 0)
                    setheading(180)
                elif element [2] == "Left":
                    goto(0, 0)
                    setheading(90)
                else:
                    goto(250, 250)
                    setheading(270)
                    
            #Calling the predefined function to draw "Block C"
            Draw_Block_D()

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('DC Flash Logo - Joshua Young (10404074)')

# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(True, True)

#############################################################################
### Call the student's function to display the stack of blocks
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)  # see the available arrangement lists above
#############################################################################

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

