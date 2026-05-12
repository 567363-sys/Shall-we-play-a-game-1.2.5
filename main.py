#need to implement captcha

import turtle as t
import time

'''

modified code that entities move horizontally

move turtle with a/d and left/right
fire with w/Up

'''
screen = t.Screen()
screen.tracer(0,2)
screen.setup(400,600)
upHp=20
downHp=20
upHpTurtle=t.Turtle()
downHpTurtle=t.Turtle()
captcha_turtle=t.Turtle()
captcha_turtle.pu()
screen.update()
upHpTurtle.pu()
downHpTurtle.pu()
topBullets=[]
bottomBullets=[]

upHpTurtle.goto(-150,250)
downHpTurtle.goto(-150,-250)

goodblock1 = t.Turtle()
goodblock1.shape('square')
goodblock1.penup()
goodblock1.goto(150, 0)

goodblock2 = t.Turtle()
goodblock2.shape('square')
goodblock2.penup()
goodblock2.goto(100, 0)

goodblock3 = t.Turtle()
goodblock3.shape('square')
goodblock3.penup()
goodblock3.goto(60, 0)

goodblock4 = t.Turtle()
goodblock4.shape('square')
goodblock4.penup()
goodblock4.goto(10, 0)


captchaImg="download.gif"
screen.addshape(captchaImg)
captcha_turtle.shape(captchaImg)


up = t.Turtle()
up.penup()
up.goto(0, 170)
up.setheading(270)
up.shapesize(3)

down = t.Turtle()
down.penup()
down.goto(0, -170)
down.setheading(90)
down.shapesize(3)

captcha_turtle.ht()
upHpTurtle.ht()
downHpTurtle.ht()
up.ht()
down.ht()
goodblock1.ht()
goodblock2.ht()
goodblock3.ht()
goodblock4.ht()


def testUpHp():
  print(upHp)
  
def testDownHp():
  print(downHp)

def upRight():
  for i in range(2):
    up.setx(up.xcor() + 10)
    screen.update()
 
def upLeft():
  for i in range(2):
    up.setx(up.xcor() - 10)
    screen.update()
 
def downRight():
  for i in range(2):
    down.setx(down.xcor() + 10)
    screen.update()
 
def downLeft():
  for i in range(2):
    down.setx(down.xcor() - 10)
    screen.update()
    
def upBullet():
  bullet=t.Turtle()
  bullet.seth(270)
  bullet.color("red")
  bullet.pu()
  bullet.shape("circle")
  bullet.goto(up.pos())
  bottomBullets.append(bullet)
  # for i in range(300):
  #   screen.update()
  #   bullet.sety(bullet.ycor()-1.5)

def downBullet():
  bullet=t.Turtle()
  bullet.seth(270)
  bullet.color("red")
  bullet.pu()
  bullet.shape("circle")
  bullet.goto(down.pos())
  topBullets.append(bullet)
  # for i in range(300):
  #   screen.update()
  #   bullet.sety(bullet.ycor()+1.5)

def captcha():
  human=False
  ans=['3','5','6','7','10']
  captcha_turtle.goto(-170,250)
  captcha_turtle.turtlesize(0.7,0.7)
  captcha_turtle.pencolor("black")
  captcha_turtle.write("Wait! Are you REALLY a human?", font=("Arial", 22, "normal"))
  captcha_turtle.goto(0,0)
  captcha_turtle.st()
  screen.update()
  print("Type in the numbers of all squares with traffic lights. Separate them with commas.")
  #answer: 3, 5, 6, 7, 10
  # while human!=True:
  while human!=True:
    if human!=True:
      user_input=input()
      user_res=user_input.split(',')
      if user_res==ans:
        human=True

  print("human verified")
  captcha_turtle.ht()
  captcha_turtle.clear()
    
    
captcha()
  
  
screen.onkeypress(testUpHp, 'q')
screen.onkeypress(testDownHp, 'e')
screen.onkeypress(upRight, 'd')
screen.onkeypress(upLeft, 'a')
screen.onkeypress(downRight, 'Right')
screen.onkeypress(downLeft, 'Left')
screen.onkeypress(upBullet,'w')
screen.onkeypress(downBullet,'Up')
screen.listen()


up.st()
down.st()
goodblock1.st()
goodblock2.st()
goodblock3.st()
goodblock4.st()

while True:
  
  goodblock1.setx(goodblock1.xcor()-0.12)
  goodblock2.setx(goodblock2.xcor()-0.12)
  goodblock3.setx(goodblock3.xcor()-0.12)
  goodblock4.setx(goodblock4.xcor()-0.12)

  if(goodblock1.xcor() < -150):
    goodblock1.setx(150)
  if(goodblock2.xcor() < -150):
    goodblock2.setx(150)
  if(goodblock3.xcor() < -150):
    goodblock3.setx(150)
  if(up.xcor()<-200):
    up.goto(200,170)
  if(up.xcor()>200):
    up.goto(-200,170)
  if(down.xcor()<-200):
    down.goto(200,-170)
  if(down.xcor()>200):
    down.goto(-200,-170)
  upHpTurtle.write("Hp: "+str(upHp), font=("Arial", 30, "normal"))
  downHpTurtle.write("Hp: "+str(downHp), font=("Arial", 30, "normal"))

  for b in topBullets:
    b.sety(b.ycor()+10)
    if b.distance(up)<20:
      upHpTurtle.clear()
      upHp-=1
    elif b.distance(goodblock1)<15 or b.distance(goodblock2)<15 or b.distance(goodblock3)<15 or b.distance(goodblock4)<15:
      b.goto(1000,1000)
      b.ht()
  for b in bottomBullets:
    b.sety(b.ycor()-10)
    if b.distance(down)<20:
      downHpTurtle.clear()
      downHp-=1
    elif b.distance(goodblock1)<15 or b.distance(goodblock2)<15 or b.distance(goodblock3)<15 or b.distance(goodblock4)<15:
      b.goto(1000,1000)
      b.ht()

  screen.update()


screen.mainloop()
