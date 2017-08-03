import turtle
import random #We'll need this later in the lab


turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

import time

turtle.register_shape("snake1.gif")
snake1 = turtle.clone()
snake1.shape("snake1.gif")
snake1.goto(0,0)
snakestamp=snake1.stamp()
time.sleep(2)
snake1.clearstamp(snakestamp)
snake1.hideturtle()

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos = (x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)

UP_ARROW = "Up" #Make sure you pay attention to upper and lower
#case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many
#milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Changedirection to up
    print("You pressed the up key!")
def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    print("You pressed the down key!")
def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    print("You pressed the left key!")
def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    print("You pressed the right key!")
####WRITE YOUR CODE HERE!!
turtle.onkeypress(up, UP_ARROW)# Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.listen()
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved UP!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved DOWN!")
    x_pos, y_pos = snake.pos()
    x_ok = LEFT_EDGE <= x_pos <= RIGHT_EDGE
    y_ok = DOWN_EDGE <= y_pos <= UP_EDGE
    if not x_ok or not y_ok:
        print("You hit the boundaries! You lose hahaha")
        quit()
    if pos_list[-1] in pos_list[0:-2]:
        print("you just hitted yourself")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)


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
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        new_stamp_length = snake.stamp()
        stamp_list.append(new_stamp_length)
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("nooo!! you are breaking my record")
        make_food()
move_snake()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")

food_pos = [(100,100)]
food_stamps = []

for this_food_pos in food_pos:
    x = this_food_pos[0]
    y=this_food_pos[1]
    food.goto(x,y)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
    START_LENGTH = START_LENGTH
    #food.clearstamp(food_stamp)
def make_food():
    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    randoom_food = (food_x,food_y)
    randoom_food_stamp = food.stamp()
    food_pos.append(randoom_food)
    food_stamps.append(randoom_food_stamp)

