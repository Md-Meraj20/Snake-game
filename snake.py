import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create the head of the snake
head = turtle.Turtle()  # Corrected from turtle.Screen() to turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create the food for the snake
food = turtle.Turtle()
colors = random.choice(['blue', 'yellow', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# Pen for displaying score
pen = turtle.Turtle()
pen.shape("square")  # Correct shape (square, circle, etc.)
pen.speed(0)
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.color("black")  # Set the color to black
pen.write("Score : 0 High Score : 0", align="center", font=("candara", 24, "bold"))


# Assigning the key directions
def group():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Listen for keypresses
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []  # List for snake's body segments

# Main game loop
while True:
    wn.update()

    # Check if the head goes out of bounds
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() < -290 or head.ycor() > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Hide all segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list and reset the game
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))
    
    # Check if the snake eats food
    if head.distance(food) < 20:
        # Move food to random position
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        
        # Add new segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)
        
        # Update delay and score
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))
    
    # Move the segments of the snake
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    
    # Move the first segment to the head's current position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()

    # Check if the snake collides with itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide all segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop()
