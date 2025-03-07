import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# creating the head of the snake
head = turtle.Turtle()  # Corrected from turtle.Screen() to turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"
    

#creating the food for our snake
food = turtle.Turtle()
colors = random.choice(['blue','yellow','black'])
shapes = random.choice(['square','triangle','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

# Pen for displaying score
pen = turtle.Turtle()
pen.shape("square")  # Use a valid shape like "square", "circle", or "turtle"
pen.speed(0)
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.color("white")  # Set the pen color to white
pen.write("Score : 0 High Score : 0", align="center", font=("candara", 24, "bold"))


# assigning the key direction
def group():
    if head.direction!= "down":
        head.direction="up"

def godown():
    if head.direction!= "up":
        head.direction="down"

def goleft():
    if head.direction!= "right":
        head.direction="left"

def goright():
    if head.direction!= "left":
        head.direction="right"

def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y + 20)
    if head.direction =="down":
        y=head.ycor()
        head.sety(y - 20)
    if head.direction =="left":
        x=head.ycor()
        head.sety(x - 20)
    if head.direction =="right":
        x=head.ycor()
        head.sety(x + 20)

 
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")


segments =[]

while True:
    wn.update()
    if head.xcor()>290 or head.xcor() < -290 or head.ycor() <-290:
        time.sleep(1)
        head.direction = "Stop"
        head.goto(0,0)
        shapes= random.choice(['square','circle'])
        colors= random.choice(['red','blue','green'])
        for segments in segments:
          segments.goto(1000, 1000)
          segments.clear()
          score= 0
          delay = 0.1
          pen.write("score : {} highscore : {}".format(score, high_score))
          align ="center"
          font = ("candara", 24, "bold")
    if head.distance(food)<20:
        x = random.randint(-270, 270)
        y = random.randint(-270 , 270)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write("score : {} highscore : {}".format(score, high_score))
        

 # checking the head segment collide with the tail segments

for segments in range(len(segments)-1,0,-1):
    x=segments[index -1].xcor()
    y=segments[index -1].xcor()
    segments[index].goto(x,y)
if len(segments) > 0:
    x = head.xcor()
    y = head.xcor()
    segments[0].goto(x,y)
move()
for segments in segments:
        if segments.distance(head) < 20:
            time.sleep(1)
            head.direction = "stop"
            head.goto(0 , 0)
            colors = random.choice(['red','blue','black'])
            shapes = random.choice(['square','circle'])
            for segments in segments:
                segments.goto(1000 , 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score ), align="center" , font= ("candara", 24 , "bold"))

time.sleep(delay)

wn.mainloop()





