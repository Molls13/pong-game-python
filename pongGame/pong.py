import turtle
wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

## score
score_a = 0
score_b = 0

## Padel A
paddle_a = turtle.Turtle()
paddle_a.speed(0) ##speed of animation
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

## Padel B
paddle_b = turtle.Turtle()
paddle_b.speed(0) ##speed of animation
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)

## ball
ball = turtle.Turtle()
ball.speed(0) ##speed of animation
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)

## scoring system : Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('player A: 0 Player B: 0', align = 'center', font = ('Courier', 24, 'normal'))

## ball x and y movement
ball.dx = 2
ball.dy = 2


### function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

##keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')

wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')



## Main loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## Border checking
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *=-1
    
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write('player A: {} Player B: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24, 'normal'))

    
    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('player A: {} Player B: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24, 'normal'))

    ## get the ball to bounce off paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1