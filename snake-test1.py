import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

trt = turtle.clone()


turtle.setup(SIZE_X, SIZE_Y)
trt.pensize(10)
trt.penup()
trt.goto(400-1, 250-1)
trt.pendown()
trt.goto(-400+1, 250-1)
trt.goto(-400+1, -250+1)
trt.goto(400-1, -250+1)
trt.goto(400-1, 250-1)
trt.penup()
trt.goto(0,0)
turtle.penup()
turtle.ht()
trt.ht()



SQUARE_SIZE = 20
START_LENGTH = 3

pos_list= []
stamp_list= []
food_pos = []
food_stamps= []

snake = turtle.clone()
snake.shape("triangle")
color_list = ["red", 'blue', 'green', 'purple', 'pink', 'brown', 'yellow', 'orange', 'deep pink', 'cyan']

turtle.hideturtle()

TIME_STEP = 100

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

    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)

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

food = turtle.clone()
food.shape("square")
food.hideturtle()


def up():
    global direction
    if direction!= DOWN:
        direction= UP
    print("You pressed the UP key")

def down():
    global direction
    if direction != UP:
        direction= DOWN
    
    print("You pressed the DOWN key")

def left():
    global direction
    if direction != RIGHT:
        direction= LEFT
    
    print("You pressed the LEFT key")

def right():
    global direction
    if direction!=LEFT:
        direction= RIGHT
   
    print("You pressed the RIGHT key")

turtle.onkeypress( up , UP_ARROW)
turtle.onkeypress( down, DOWN_ARROW)
turtle.onkeypress( left, LEFT_ARROW)
turtle.onkeypress( right, RIGHT_ARROW)
turtle.listen()

################################

def make_food():

    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint( min_x, max_x)*SQUARE_SIZE
    food_y = random.randint( min_y, max_y)*SQUARE_SIZE
    random_food= (food_x, food_y)
    
    if random_food in pos_list:
        make_food()
    else:
        food.goto(food_x, food_y)
        new_food = food.stamp()
        food_stamps.append(new_food)
        new_food_pos = food.pos()
        food_pos.append(new_food_pos)
        
score_val = 0
score = turtle.clone()
scr = score.clone()

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
    ###pop 0 ele. in pos_list to get #RID OF THE TAIL LAST PIECE#######
    
##    the score turtle object is called "scr"

    # the snake is eating the food
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        make_food()
        global score_val
        score_val +=1
        print(score_val)
        scr.clear()
        scr.goto(250,250)
        scr.clear()
        scr.write(str(score_val), "center", font=("Ariel", 15, "normal"))
        snake.fillcolor(random.choice(color_list))

    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
#######part3
    
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! GAME OVER!")
##        turtle.sleep(3)
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! GAME OVER!")
##        turtle.sleep(3)
        quit()

    if new_y_pos >= UP_EDGE:
        print("you hit the top edge! GAME OVER!")
##        turtle.sleep(3)
        quit()

    if new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! GAME OVER!")
##        turtle.sleep(3)
        quit()
     ### SNAKE DONT EAT YOURSELF !!!
    
    if new_pos in pos_list[:-1]:
        print("you eat yourslef ! GAME OVER!")
        quit()

        
    turtle.ontimer(move_snake, TIME_STEP)

make_food()
move_snake()



##
####
##food_pos = [(100,100), (-100,100), ( -100, -100), (100, -100)]    
##for i in food_pos :
##    food.goto(i)
##    f1 = food.stamp()
##    food_stamps.append(f1)







