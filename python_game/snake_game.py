import turtle
import time
import random

# delay time
delay = 0.1

# score board
score = 0
high_score = 0

# 
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # close screen update

# create snake head
head = turtle.Turtle()
head.speed(0)  # 0: fastest
head.shape("square")
head.color("white")
head.penup()  # no draw line
head.goto(0, 0)
head.direction = "stop"  # stop

# 创建食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []  # sname body

# data board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("cuurrent score: 0  highest score: 0", align="center", font=("Courier", 24, "normal"))

# move functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# snake move fuction
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

# 键盘绑定
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# 主游戏循环
while True:
    wn.update()

    # 检查碰撞边界
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # 隐藏蛇身所有段
        for segment in segments:
            segment.goto(1000, 1000)  # 将蛇身段移出屏幕
        segments.clear()

        # 重置分数
        score = 0
        pen.clear()
        pen.write(f"分数: {score}  最高分: {high_score}", align="center", font=("Courier", 24, "normal"))

    # 检查碰撞食物
    if head.distance(food) < 20:
        # 移动食物到随机位置
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # 添加新的蛇身段
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # 增加分数
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"分数: {score}  最高分: {high_score}", align="center", font=("Courier", 24, "normal"))

    # 移动蛇身
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 检查蛇头是否撞到蛇身
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "停止"

            # 隐藏蛇身所有段
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # 重置分数
            score = 0
            pen.clear()
            pen.write(f"分数: {score}  最高分: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

