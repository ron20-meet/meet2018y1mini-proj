# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import time
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly
border = turtle.clone()

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10
score=0
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
small_stamps = []
small_pos = []

ron = turtle.Turtle()

small = turtle.Turtle()
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(my_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
def down():
    global direction
    direction=DOWN
    print("you pressed the down key")

def left():
    global direction
    direction=LEFT
    print("you pressed the left key")

def right():
    global direction
    direction=RIGHT
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    food.goto(food_x,food_y)
    stamp =food.stamp()
    food_pos.append((food_x,food_y))
    food_stamps.append(stamp)

def make_small():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    
    small_x = random.randint(min_x,max_x)*SQUARE_SIZE
    small_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    small.goto(small_x,small_y)
    stamp =small.stamp()
    small_pos.append((small_x,small_y))
    small_stamps.append(stamp)
    
      
def move_snake():
    color_tup = ("blue", 'green' , 'red', 'purple', 'orange', 'yellow')
     
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if snake.pos() in pos_list[:-1]:
        small.penup()
        small.goto(0,0)
        small.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal"))
        time.sleep(3)
        quit()
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        ##snake.color = color_list[random.randint(1, len(color_list))]
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right adge! Game over!")
        small.penup()
        small.goto(0,0)
        small.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal") )
        time.sleep(3)
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left adge! Game over!")
        small.penup()
        small.goto(0,0)
        small.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal") )
        time.sleep(3)
        quit()
    if new_y_pos >= UP_EDGE:
        print("you hit the up edge! Game over!")
        small.penup()
        small.goto(0,0)
        small.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal") )
        time.sleep(3)
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! Game over!")
        small.penup()
        small.goto(0,0)
        small.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal") )
        time.sleep(3)
        quit()
    
        
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    
    
        ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    global score
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        ron.clear()
        ron.write(score, move=False, align="left", font=("Arial", 30, "normal") )
        score+=1
        snake.color(color_tup[random.randint(0,5)])
        make_food()
        make_small()
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    
    global small_pos
    if snake.pos() in small_pos:
         print ("You ate the mouse, GAME OVER")
         small.penup()
         small.goto(0,0)
         small.write("GAME OVER", move=False, align="center", font=("Arial", 30, "normal") )
         time.sleep(3)
         quit()
        
    
    
    #HINT: This if statement may be useful for Part 8

    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()

    
    if len (food_stamps)<=6:
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)

  
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for i in food_pos :
    food.goto(i[0],i[1])
    stamp=food.stamp()
    food_stamps.append(stamp)

turtle.register_shape("small.gif")
small = turtle.clone()
small.shape("small.gif")
small_pos = [(200,200),(-200,200), (-200,-200), (200,-100)]
for i in small_pos :
    small.goto(i[0],i[1])
    stamp=small.stamp()
    small_stamps.append(stamp)



turtle.bgcolor("light yellow")
turtle.color("purple")


move_snake()




     

