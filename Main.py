#Imports:
import turtle as t
import time
'''

modified code that entities move horizontally

move turtle with a/d and left/right
fire with w/Up

'''
#setup
def game_start():
  pen.clear()
  screen.bgcolor('White')
  print('hi')
  screen.tracer(0,2) #used to be 0,2
  screen.setup(400,600)
  upHp=50
  downHp=50
  upHpTurtle=t.Turtle()
  downHpTurtle=t.Turtle()
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
  
  blackPartB = t.Turtle()
  blackPartB.shape("square")
  blackPartB.shapesize(0.6, 5.1)
  blackPartB.color("black")
  blackPartB.pu()
  blackPartB.goto(-100, -250)
  
  redPartB = t.Turtle()
  redPartB.shape("square")
  redPartB.shapesize(0.5, 5)
  redPartB.color("red")
  redPartB.pu()
  redPartB.goto(-100, -250)
  
  blackPartT = t.Turtle()
  blackPartT.shape("square")
  blackPartT.shapesize(0.6, 5.1)
  blackPartT.color("black")
  blackPartT.pu()
  blackPartT.goto(-100, 250)
  
  redPartT = t.Turtle()
  redPartT.shape("square")
  redPartT.shapesize(0.5, 5)
  redPartT.color("red")
  redPartT.pu()
  redPartT.goto(-100, 250)
  
  
  up = t.Turtle()
  up.penup()
  up.goto(0, 170)
  up.setheading(270)
  up.shape('topPlayerV1.gif')
  
  down = t.Turtle()
  down.penup()
  down.goto(0, -170)
  down.setheading(90)
  down.shape('bottomPlayerV1.gif')
  #Functions
  
  def setHealthB(health):
    redPartB.shapesize(0.5, 5 * health)
    redPartB.goto(blackPartB.xcor() -50 * (1 -health), blackPartB.ycor())
    screen.update()
  
  def setHealthT(health):
    redPartT.shapesize(0.5, 5 * health)
    redPartT.goto(blackPartT.xcor() -50 * (1 -health), blackPartT.ycor())
    screen.update()
  
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
    bullet.shapesize(0.5)
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
    bullet.shapesize(0.5)
    bullet.goto(down.pos())
    topBullets.append(bullet)
    # for i in range(300):
    #   screen.update()
    #   bullet.sety(bullet.ycor()+1.5)
  #onkeypress and game start function

  screen.onkeypress(testUpHp, 'q')
  screen.onkeypress(testDownHp, 'e')
  screen.onkeypress(upRight, 'd')
  screen.onkeypress(upLeft, 'a')
  screen.onkeypress(downRight, 'Right')
  screen.onkeypress(downLeft, 'Left')
  screen.onkeypress(upBullet,'w')
  screen.onkeypress(downBullet,'Up')
  screen.listen()
  
  #Moving blocks
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
    # upHpTurtle.write("Hp: "+str(upHp), font=("Arial", 30, "normal"))
    # downHpTurtle.write("Hp: "+str(downHp), font=("Arial", 30, "normal"))
  
    for b in topBullets:
      b.sety(b.ycor()+1)
      if b.distance(up)<20:
        upHpTurtle.clear()
        upHp-=0.1
        setHealthT(upHp/50)
      elif b.distance(goodblock1)<15 or b.distance(goodblock2)<15 or b.distance(goodblock3)<15 or b.distance(goodblock4)<15:
        b.goto(1000,1000)
        b.ht()
    for b in bottomBullets:
      b.sety(b.ycor()-1)
      if b.distance(down)<20:
        downHpTurtle.clear()
        downHp-=0.1
        setHealthB(downHp/50)
      elif b.distance(goodblock1)<15 or b.distance(goodblock2)<15 or b.distance(goodblock3)<15 or b.distance(goodblock4)<15:
        b.goto(1000,1000)
        b.ht()
  
    screen.update()
# Menues by Aprameya:

screen = t.Screen()
screen.setup(400,600)
screen.bgcolor("#0a0a14")
screen.title("MAIN MENU")
screen.tracer(0)

pen = t.Turtle()
pen.hideturtle()
pen.speed(0)

page = "splash"
username = ""
username2 = ""

bg = t.Turtle()
bg.hideturtle()
bg.speed(0)
screen.addshape("SECOND_background_space_invaders.gif")
screen.addshape('topPlayerV1.gif')
screen.addshape('bottomPlayerV1.gif')
bg.shape("SECOND_background_space_invaders.gif")
bg.goto(0, 0)

WIDTH, HEIGHT = 400, 600
HALF_W, HALF_H = WIDTH//2, HEIGHT//2

def box(x, y, w, h, fill, border):
    pen.penup()
    pen.goto(x, y)
    pen.fillcolor(fill)
    pen.pencolor(border)
    pen.pensize(2)
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()
    pen.penup()

def line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pencolor("#00c88c")
    pen.pensize(2)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

def text(t, x, y, size, color, align="center"):
    pen.penup()
    pen.goto(x, y)
    pen.pencolor(color)
    pen.write(t, align=align, font=("Courier", size, "bold"))

def grid():
    pen.pensize(1)
    pen.pencolor("#003c2d")
    for x in range(-HALF_W, HALF_W+1, 40):
        pen.penup()
        pen.goto(x, -HALF_H)
        pen.pendown()
        pen.goto(x, HALF_H)
    for y in range(-HALF_H, HALF_H+1, 40):
        pen.penup()
        pen.goto(-HALF_W, y)
        pen.pendown()
        pen.goto(HALF_W, y)
    pen.penup()

def draw_splash():
    pen.clear()
    bg.showturtle()
    text("CLICK TO START", 0, -250, 16, "#00ffb4")
    screen.update()

def draw_name_entry(player_num):
    bg.hideturtle()
    pen.clear()
    grid()

    if player_num == 1:
        accent      = "#ff8c00"
        highlight   = "#ffd080"
        label       = "ENTER PLAYER 1 NAME"
        current     = username
    else:
        accent      = "#9b30ff"
        highlight   = "#d580ff"
        label       = "ENTER PLAYER 2 NAME"
        current     = username2

    box(-HALF_W, 200, WIDTH, 80, "#141c28", accent)
    pen.penup(); pen.goto(-HALF_W, 200); pen.pencolor(accent)
    pen.pensize(2); pen.pendown(); pen.goto(HALF_W, 200); pen.penup()
    text(label, 0, 220, 16, highlight)
    box(-150, 150, 300, 40, "#0a0a14", accent)
    text(current + "_", -140, 158, 16, "#fff064", align="left")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = 7
    kx, ky = -160, 120
    kw, kh = 40, 30
    for i, ch in enumerate(letters):
        col = i % cols
        row = i // cols
        bx = kx + col * (kw + 5)
        by = ky - row * (kh + 5)
        box(bx, by - kh, kw, kh, "#141c28", accent)
        text(ch, bx + kw // 2, by - kh + 8, 12, highlight)
    box(-160, -250, 100, 40, "#141c28", accent)
    text("DEL", -110, -240, 12, "#ff6060")
    box(60, -250, 100, 40, "#141c28", accent)
    text("DONE", 110, -240, 12, highlight)
    screen.update()

def draw_welcome():
    pen.clear()
    grid()
    box(-HALF_W, 200, WIDTH, 80, "#141c28", "#00c88c")
    line(-HALF_W, 200, HALF_W, 200)
    text("Welcome, " + username + " & " + username2 + "!", 0, 220, 14, "#fff064")
    text("Modify settings?", 0, 150, 14, "#00ffb4")
    box(-140, 50, 120, 50, "#141c28", "#00ff80")
    text("YES", -80, 65, 16, "#00ff80")
    box(20, 50, 120, 50, "#141c28", "#ff6060")
    text("NO", 80, 65, 16, "#ff6060")
    screen.update()

def draw_loading():
    pen.clear()
    grid()
    box(-HALF_W, 200, WIDTH, 80, "#141c28", "#00c88c")
    line(-HALF_W, 200, HALF_W, 200)
    text("LOADING GAME", 0, 220, 20, "#00ffb4")

    bar_x = -160
    bar_y = 20
    bar_w = 320
    bar_h = 30

    box(bar_x, bar_y, bar_w, bar_h, "#0a0a14", "#00c88c")

    steps = 40
    messages = [
        (0,  "Initializing..."),
        (10, "Loading assets..."),
        (22, "Spawning enemies..."),
        (34, "Almost ready..."),
    ]
    msg_index = 0

    for i in range(steps + 1):
        fill_w = int((bar_w - 4) * i / steps)
        if fill_w > 0:
            box(bar_x + 2, bar_y + 2, fill_w, bar_h - 4, "#00c88c", "#00c88c")

        for threshold, msg in messages:
            if i == threshold:
                pen.penup()
                pen.goto(0, bar_y - 40)
                pen.pencolor("#0a0a14")
                pen.write(" " * 40, align="center", font=("Courier", 11, "bold"))
                text(msg, 0, bar_y - 40, 11, "#007858")

        pct = int(i / steps * 100)
        pen.penup()
        pen.goto(0, bar_y + 8)
        pen.pencolor("#0a0a14")
        pen.write("     ", align="center", font=("Courier", 11, "bold"))
        text(str(pct) + "%", 0, bar_y + 8, 11, "#fff064")

        screen.update()
        time.sleep(0.045)

    text("READY!", 0, bar_y - 80, 18, "#00ffb4")
    screen.update()
    time.sleep(0.8)
    game_start()

def draw_menu():
    pen.clear()
    grid()
    box(-HALF_W, 200, WIDTH, 80, "#141c28", "#00c88c")
    line(-HALF_W, 200, HALF_W, 200)
    text("M A I N   M E N U", 0, 220, 24, "#00ffb4")
    text("[ SELECT AN OPTION ]", 0, 200, 11, "#007858")
    box(-120, 60, 240, 60, "#141c28", "#00c88c")
    text("Speed Settings", 0, 80, 14, "#00ffb4")
    box(-120, -40, 240, 60, "#141c28", "#00c88c")
    text("Difficulty Levels", 0, -20, 14, "#00ffb4")
    screen.update()

def draw_sub(title):
    pen.clear()
    grid()
    box(-HALF_W, 200, WIDTH, 80, "#141c28", "#00c88c")
    line(-HALF_W, 200, HALF_W, 200)
    text(title, 0, 220, 22, "#fff064")
    box(-150, -200, 300, 50, "#141c28", "#00c88c")
    text("< BACK", -130, -185, 12, "#00ffb4", align="left")
    screen.update()

def click(x, y):
    global page, username, username2

    if page == "splash":
        page = "name1"
        draw_name_entry(1)

    elif page == "name1":
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cols = 7
        kx, ky = -160, 120
        kw, kh = 40, 30
        for i, ch in enumerate(letters):
            col = i % cols
            row = i // cols
            bx = kx + col * (kw + 5)
            by = ky - row * (kh + 5)
            if bx <= x <= bx + kw and by - kh <= y <= by:
                username += ch
                draw_name_entry(1)
                return
        if -160 <= x <= -60 and -250 <= y <= -210:
            username = username[:-1]
            draw_name_entry(1)
        elif 60 <= x <= 160 and -250 <= y <= -210:
            if len(username) > 0:
                page = "name2"
                draw_name_entry(2)

    elif page == "name2":
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cols = 7
        kx, ky = -160, 120
        kw, kh = 40, 30
        for i, ch in enumerate(letters):
            col = i % cols
            row = i // cols
            bx = kx + col * (kw + 5)
            by = ky - row * (kh + 5)
            if bx <= x <= bx + kw and by - kh <= y <= by:
                username2 += ch
                draw_name_entry(2)
                return
        if -160 <= x <= -60 and -250 <= y <= -210:
            username2 = username2[:-1]
            draw_name_entry(2)
        elif 60 <= x <= 160 and -250 <= y <= -210:
            if len(username2) > 0:
                page = "welcome"
                draw_welcome()

    elif page == "welcome":
        if -140 <= x <= -20 and 50 <= y <= 100:
            page = "menu"
            draw_menu()
        elif 20 <= x <= 140 and 50 <= y <= 100:
            page = "loading"
            draw_loading()

    elif page == "menu":
        if -120 <= x <= 120 and 60 <= y <= 120:
            page = "option1"
            draw_sub("Speed Settings")
        elif -120 <= x <= 120 and -40 <= y <= 20:
            page = "option2"
            draw_sub("Difficulty Levels")

    elif page in ["option1", "option2"]:
        if -150 <= x <= 150 and -200 <= y <= -150:
            page = "menu"
            draw_menu()

draw_splash()
screen.onclick(click)
screen.listen()

"""
WIP
def draw_player_cards():
    box(-190, 30, 170, 120, "#1a0a00", "#ff8c00")
    text(username,  -105,  110, 13, "#ffd080")
    text("P1",      -105,   80, 28, "#ff8c00")
    text("SCORE: 0",-105,   45, 11, "#ffd080")

    box(20, 30, 170, 120, "#0d001a", "#9b30ff")
    text(username2,  105,  110, 13, "#d580ff")
    text("P2",       105,   80, 28, "#9b30ff")
    text("SCORE: 0", 105,   45, 11, "#d580ff")

def draw_versus_splash():
    pen.clear()
    grid()
    draw_player_cards()
    text("V S", 0, 60, 36, "#ffffff")
    box(-60, -60, 120, 40, "#141c28", "#00c88c")
    text("PLAY", 0, -48, 16, "#00ffb4")
    screen.update()

def animate_countdown():
    for n in ["3", "2", "1", "GO!"]:
        pen.clear()
        grid()
        draw_player_cards()
        ...

def draw_hud():
    ...
"""

screen.mainloop()
