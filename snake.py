import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

pos_list= []
stamp_list= []
food_pos = []
food_stamps= []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

P_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 10000

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#######

for loop1 in range(START_LENGTH):
    x_pos= snake.pos()[0]
    y_pos= snake.pos()[1]
    x_pos += SQUARE_SIZE

    my_pos=(x_pos, y_pos)
    snake.goto(x_pos, y_pos)

    pos_list.append(my_pos)

    stemp_id = snake.stamp()
    stamp_list.append(stemp_id)

#####

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 100

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3



def up():
    global direction
    direction= UP
    print("You pressed the UP key")

def down():
    global direction
    direction= DOWN
    
    print("You pressed the DOWN key")

def left():
    global direction
    direction= LEFT
    
    print("You pressed the LEFT key")

def right():
    global direction
    direction= RIGHT
   
    print("You pressed the RIGHT key")

turtle.onkeypress( up, UP_ARROW)
turtle.onkeypress( down, DOWN_ARROW)
turtle.onkeypress( left, LEFT_ARROW)
turtle.onkeypress( right, RIGHT_ARROW)

turtle.listen()

################################

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto( x_pos+ SQUARE_SIZE, y_pos)
        print("you moved right!")
        
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        print("you moved left!")
        
    elif direction == UP:
        snake.goto( x_pos , y_pos+SQUARE_SIZE)
        print("you moved up!")

    elif direction == DOWN:
        snake.goto( x_pos , y_pos-SQUARE_SIZE)
        print("you moved down!")


    my_pos = snake.pos()
    new_pos= my_pos
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    pos_list.append(my_pos)
    
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ###SPECIAL pop 0 elemant in pos_list to get rid of the last piece of the tail.

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
    turtle.ontimer(move_snake, TIME_STEP)
    
#######part3
    
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the edge! GAME OVER!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("you hit the edge! GAME OVER!")
        quit()

    if new_y_pos >= UP_EDGE:
        print("you hit the edge! GAME OVER!")
        quit()

    if new_x_pos <= DOWN_EDGE:
        print("you hit the edge! GAME OVER!")
        quit()


move_snake()


food = turtle.clone()
food.shape("triangle")

food_pos = [(100,100), (-100,100), ( -100, -100), (100, -100)]
food_stampe = []

if snake.pos() in food_pos:
    food_ind = food_pos.index(snake.pos())
    food.clearstamp(food_stamps[f_dx])
    food_pos.pop(food_ind)
    food_stamp.pop(food_ind)
    
    
for i in food_pos :
    food.goto(i)
    f1 = food.stamp()
    food_stempe.append(f1)
    food.hideturtle()
    




