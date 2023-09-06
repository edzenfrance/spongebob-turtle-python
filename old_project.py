# SPONGEBOB BY EDZEN FRANCE B. ARABIA
# 3/24/2022

import turtle

draw = turtle.Turtle()
draw.speed(0)

# ---------------------------------------
# Background
# ---------------------------------------
draw.penup()
draw.goto(-300,300)
draw.pendown()
draw.pensize(5)
draw.color("black")
draw.begin_fill()

draw.forward(650)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.end_fill()

draw.setheading(270)
draw.forward(400)
draw.color("#384E77")
draw.begin_fill()
draw.forward(250)
draw.left(90)
draw.forward(650)
draw.left(90)
draw.forward(250)
draw.left(90)
draw.forward(650)
draw.end_fill()

draw.color("#F6FBE6")
draw.begin_fill()
draw.right(90)
draw.forward(70)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(70)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(70)
draw.end_fill()

draw.color("#AEC5A6")
draw.begin_fill()
draw.forward(30)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(30)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(30)
draw.end_fill()

draw.color("#1651FD")
draw.begin_fill()
draw.forward(20)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(20)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(20)
draw.end_fill()

draw.color("#206AFB")
draw.begin_fill()
draw.forward(15)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(15)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(15)
draw.end_fill()

draw.color("#2779FF")
draw.begin_fill()
draw.forward(15)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(15)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(15)
draw.end_fill()

draw.color("#3297FE")
draw.begin_fill()
draw.forward(15)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(15)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(15)
draw.end_fill()

draw.color("#44BBFF")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

draw.color("#4CCEFD")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

draw.color("#52DDFC")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

draw.color("#75FEE4")
draw.begin_fill()
draw.forward(170)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(170)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(170)
draw.end_fill()

draw.color("#8EFFE0")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

draw.color("#9EFFCB")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

draw.color("#ABFEC8")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

draw.color("#8EFEC4")
draw.begin_fill()
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.right(90)
draw.forward(650)
draw.right(90)
draw.forward(10)
draw.end_fill()

# ---------------------------------------
# Yellow Body
# ---------------------------------------
draw.pensize(2)
draw.setheading(0)
draw.penup()
draw.goto(-70,-70)
draw.pendown()
draw.color("black", "yellow")
#draw.color("#fbec5d", "yellow")
draw.begin_fill()
draw.forward(200)
draw.left(90)
draw.forward(220)
draw.left(90)
draw.forward(200)
draw.left(90)
draw.forward(220)
draw.end_fill()

# ---------------------------------------
# Brown Pants
# ---------------------------------------
draw.color("black", "#8B6507")
draw.begin_fill()
draw.forward(40)
draw.left(90)
draw.forward(200)
draw.left(90)
draw.forward(40)
draw.left(90)
draw.forward(200)
draw.left(90)
draw.end_fill()

# ---------------------------------------
# White Uniform
# ---------------------------------------
draw.color("black", "white")
#draw.color("#c0c0c0", "white")
draw.begin_fill()
draw.left(90)
draw.forward(200)
draw.left(90)
draw.forward(30)
draw.left(90)
draw.forward(200)
draw.left(90)
draw.forward(40)
draw.end_fill()

draw.penup()
draw.goto(18, -40)
draw.pendown()

draw.right(30)
draw.forward(25)
draw.right(95)
draw.forward(38)

draw.setheading(270)
draw.penup()
draw.goto(41, -40)
draw.pendown()

draw.left(30)
draw.forward(25)
draw.left(95)
draw.forward(38)


# -------------------
# Draw Pimples
# -------------------

draw.color("#98BE0E")
draw.penup()
draw.goto(-55, 115)
draw.pendown()
draw.begin_fill()
draw.setheading(-30)
for i in range(2):
    draw.circle(15,90)
    draw.circle(15//2,90)
draw.end_fill()

draw.penup()
draw.goto(-23, 130)
draw.pendown()
draw.begin_fill()
draw.setheading(-40)
for i in range(2):
    draw.circle(6,90)
    draw.circle(6//2,90)
draw.end_fill()
# ---------------------
draw.penup()
draw.goto(85, 115)
draw.pendown()
draw.begin_fill()
draw.setheading(-80)
for i in range(2):
    draw.circle(17,90)
    draw.circle(17//2,90)
draw.end_fill()

draw.penup()
draw.goto(110, 85)
draw.pendown()
draw.begin_fill()
draw.setheading(-30)
for i in range(2):
    draw.circle(6,90)
    draw.circle(6//2,90)
draw.end_fill()
# ---------------------
draw.penup()
draw.goto(-45, -15)
draw.pendown()
draw.begin_fill()
draw.setheading(-60)
for i in range(2):
    draw.circle(20,90)
    draw.circle(20//2,90)
draw.end_fill()

draw.penup()
draw.goto(-45, 10)
draw.pendown()
draw.begin_fill()
draw.setheading(-30)
for i in range(2):
    draw.circle(6,90)
    draw.circle(6//2,90)
draw.end_fill()
# ---------------------
draw.penup()
draw.goto(75, -15)
draw.pendown()
draw.begin_fill()
draw.setheading(-47)
for i in range(2):
    draw.circle(17,90)
    draw.circle(17//2,90)
draw.end_fill()

draw.penup()
draw.goto(95, 10)
draw.pendown()
draw.begin_fill()
draw.setheading(-30)
for i in range(2):
    draw.circle(6,90)
    draw.circle(6//2,90)
draw.end_fill()

# ---------------------------------------
# Black Box
# ---------------------------------------
draw.penup()
draw.goto(-56, -80)
draw.pendown()
draw.color("black")
draw.setheading(0)
draw.begin_fill()
draw.forward(33)
draw.right(90)
draw.forward(8)
draw.right(90)
draw.forward(33)
draw.right(90)
draw.forward(8)
draw.end_fill()

draw.penup()
draw.goto(-5, -80)
draw.pendown()

draw.setheading(0)
draw.begin_fill()
draw.forward(72)
draw.right(90)
draw.forward(8)
draw.right(90)
draw.forward(72)
draw.right(90)
draw.forward(8)
draw.end_fill()

draw.penup()
draw.goto(85, -80)
draw.pendown()

draw.setheading(0)
draw.begin_fill()
draw.forward(32)
draw.right(90)
draw.forward(8)
draw.right(90)
draw.forward(32)
draw.right(90)
draw.forward(8)
draw.end_fill()

# ---------------------------------------
# Red Tie
# ---------------------------------------
draw.color("black", "#FF0200")
draw.setheading(180)
draw.penup()
draw.goto(41, -40)
draw.pendown()
draw.begin_fill()

draw.forward(25)
draw.left(115)
draw.forward(20)
draw.setheading(0)
draw.forward(10)
draw.left(65)
draw.forward(20)
draw.end_fill()

draw.penup()
draw.goto(24, -59)
draw.pendown()
draw.begin_fill()

draw.setheading(270)
draw.right(20)
draw.forward(30)
draw.left(70)
draw.forward(20)
draw.left(80)
draw.forward(20)
draw.left(67)
draw.forward(31)
draw.setheading(180)
draw.forward(11)
draw.end_fill()


# ---------------------------------------
# Teeth
# ---------------------------------------
draw.penup()
draw.goto(10, 11)
draw.pendown()
draw.color("black", "white")
draw.begin_fill()

draw.setheading(270)
draw.right(7)
draw.forward(15)
draw.left(90)
draw.forward(15)
draw.left(90)
draw.forward(13)
draw.end_fill()

draw.penup()
draw.goto(33, 8)
draw.pendown()
draw.begin_fill()

draw.setheading(270)
draw.left(7)
draw.forward(14)
draw.left(90)
draw.forward(15)
draw.left(90)
draw.forward(14)
draw.end_fill()


# ---------------------------------------
# Eyes
# ---------------------------------------
# Left Eye
draw.color("black", "white")
draw.penup()
draw.goto(-36, 64)
draw.pendown()
draw.begin_fill()
draw.setheading(90)
draw.left(25)
for i in range(22):
    draw.right(13)
    draw.forward(7)
draw.end_fill()

# Right Eye
draw.penup()
draw.goto(95, 64)
draw.pendown()
draw.begin_fill()
draw.setheading(90)
draw.right(25)
for i in range(23):
    draw.left(13)
    draw.forward(7)
draw.end_fill()

# Left Pupil
draw.color("black", "#34C5EB")
draw.penup()
draw.goto(2, 60)
draw.pendown()
draw.begin_fill()
for _ in range(75):
    draw.left(5)
    draw.forward(1)
draw.end_fill()

draw.penup()
draw.goto(62, 61)
draw.pendown()
draw.begin_fill()
for _ in range(80):
    draw.left(5)
    draw.forward(1)
draw.end_fill()

draw.color("black", "black")
draw.penup()
draw.goto(4, 70)
draw.pendown()
draw.begin_fill()
for _ in range(22):
    draw.left(16)
    draw.forward(1)
draw.end_fill()

draw.penup()
draw.goto(61, 70)
draw.pendown()
draw.begin_fill()
for _ in range(22):
    draw.left(16)
    draw.forward(1)
draw.end_fill()

# ---------------------------------------
# Eye Lashes
# ---------------------------------------
draw.pensize(3)
draw.color("black")

# Left eyelashes
draw.penup()
draw.goto(-20, 101)
draw.pendown()
draw.setheading(90)
draw.left(17)
draw.forward(12)

draw.penup()
draw.goto(-8, 106)
draw.pendown()
draw.setheading(90)
draw.forward(12)

draw.penup()
draw.goto(4, 102)
draw.pendown()
draw.setheading(90)
draw.right(17)
draw.forward(12)

# Right eyelashes
draw.penup()
draw.goto(52, 101)
draw.pendown()
draw.setheading(90)
draw.left(17)
draw.forward(12)

draw.penup()
draw.goto(64, 106)
draw.pendown()
draw.setheading(90)
draw.forward(12)

draw.penup()
draw.goto(78, 102)
draw.pendown()
draw.setheading(90)
draw.right(17)
draw.forward(12)

# ---------------------------------------
# Cheeks
# ---------------------------------------
draw.penup()
draw.goto(-40, 35)
draw.pendown()
draw.color("#AC6507", "yellow")

draw.setheading(180)
draw.right(50)
draw.begin_fill()

for i in range(45):
    draw.right(5.1)
    draw.forward(1.6)
    
draw.end_fill()

draw.penup()
draw.goto(105, 35)
draw.pendown()
draw.begin_fill()
draw.setheading(0)
draw.left(50)

for i in range(45):
    draw.left(5.1)
    draw.forward(1.6)
    
draw.end_fill()

draw.penup()
draw.goto(-37, 50)
draw.pendown()
draw.pensize(2)
draw.circle(0.8)

draw.penup()
draw.goto(-29, 55)
draw.pendown()
draw.pensize(3)
draw.circle(1.4)

draw.penup()
draw.goto(-20, 52)
draw.pendown()
draw.pensize(3)
draw.circle(1)

draw.penup()
draw.goto(80, 50)
draw.pendown()
draw.pensize(2)
draw.circle(0.8)

draw.penup()
draw.goto(90, 55)
draw.pendown()
draw.pensize(3)
draw.circle(1.4)

draw.penup()
draw.goto(98, 52)
draw.pendown()
draw.pensize(3)
draw.circle(1)


# ---------------------------------------
# Mouth
# ---------------------------------------
draw.pensize(2)
draw.penup()
draw.goto(-25, 40)
draw.pendown()
draw.color("black")
draw.setheading(0)
draw.right(60)

for i in range(40):
    draw.left(3)
    draw.forward(3.5)

draw.penup()
draw.goto(-30, 34)
draw.pendown()
draw.setheading(90)
draw.left(15)

for i in range(17):
    draw.right(8)
    draw.forward(1)

draw.penup()
draw.goto(95, 34)
draw.pendown()
draw.setheading(90)
draw.right(15)

for i in range(17):
    draw.left(8)
    draw.forward(1)


# ---------------------------------------
# Nose
# ---------------------------------------
draw.pensize(2)
draw.penup()
draw.goto(25, 50)
draw.pendown()
draw.color("black", "yellow")
draw.begin_fill()

draw.setheading(90)
draw.left(10)

for i in range(1):
    draw.right(4)
    draw.forward(5)

for i in range(35):
    draw.right(6)
    draw.forward(1)

draw.forward(10)
draw.end_fill()


# ---------------------------------------
# Shoulder
# ---------------------------------------
draw.color("black", "white")
draw.penup()
draw.goto(-70, 15)
draw.pendown()
draw.begin_fill()
draw.setheading(180)
draw.left(45)
for _ in range(60):
    draw.left(0.7)
    draw.forward(1)
draw.setheading(270)
draw.left(65)
draw.forward(26)
draw.setheading(90)
draw.forward(63)
draw.end_fill()

draw.penup()
draw.goto(130, 15)
draw.pendown()
draw.begin_fill()

draw.setheading(0)
draw.right(45)
for _ in range(60):
    draw.right(0.7)
    draw.forward(1)
draw.setheading(270)
draw.right(65)
draw.forward(26)
draw.setheading(90)
draw.forward(63)
draw.end_fill()



# ---------------------------------------
# Hands Left
# ---------------------------------------
draw.color("black", "yellow")
draw.penup()
draw.goto(-79, -116)
draw.pendown()
draw.begin_fill()
draw.setheading(90)
draw.right(2)
draw.forward(69)
draw.left(68)
draw.forward(12)
draw.setheading(270)
draw.right(2)
draw.forward(72)

# Hands
draw.setheading(180)
draw.left(45)
for _ in range(18):
    draw.left(1.6)
    draw.forward(1)

# First finger
draw.setheading(270)
draw.right(60)
draw.forward(15)
for _ in range(15):
    draw.left(12)
    draw.forward(1)
draw.forward(12)

# Second Finger
draw.setheading(270)
draw.right(30)
draw.forward(10)
draw.right(10)
draw.forward(10)
for _ in range(15):
    draw.left(12)
    draw.forward(1)
draw.left(5)
draw.forward(15)
draw.left(5)
draw.forward(5)

# Third Finger
draw.setheading(270)
draw.right(5)
draw.forward(10)
draw.right(3)
draw.forward(10)
for _ in range(15):
    draw.left(12)
    draw.forward(1)
draw.left(4)
draw.forward(10)
draw.left(3)
draw.forward(5)
draw.right(6)
draw.forward(10)

# Fourth finger
draw.setheading(270)
draw.left(40)
draw.forward(15)
for _ in range(15):
    draw.left(12)
    draw.forward(1)
draw.forward(13)

# Hands
draw.setheading(90)
draw.forward(9)
draw.left(20)
draw.forward(2)
draw.left(16)
draw.forward(10)
    
draw.end_fill()

# ---------------------------------------
# Hands Left
# ---------------------------------------
draw.penup()
draw.goto(137, -116)
draw.pendown()
draw.color("black", "yellow")
draw.begin_fill()
draw.setheading(90)
draw.left(2)
draw.forward(69)
draw.right(68)
draw.forward(12)
draw.setheading(270)
draw.left(2)
draw.forward(72)

# Hands
draw.setheading(0)
draw.right(45)
for _ in range(18):
    draw.right(1.6)
    draw.forward(1)

# First finger
draw.setheading(270)
draw.left(60)
draw.forward(15)
for _ in range(15):
    draw.right(12)
    draw.forward(1)
draw.forward(12)

# Second Finger
draw.setheading(270)
draw.left(30)
draw.forward(10)
draw.left(10)
draw.forward(10)
for _ in range(15):
    draw.right(12)
    draw.forward(1)
draw.right(5)
draw.forward(15)
draw.right(5)
draw.forward(5)

# Third Finger
draw.setheading(270)
draw.left(5)
draw.forward(10)
draw.left(3)
draw.forward(10)
for _ in range(15):
    draw.right(12)
    draw.forward(1)
draw.right(4)
draw.forward(10)
draw.right(3)
draw.forward(5)
draw.left(6)
draw.forward(10)

# Fourth finger
draw.setheading(270)
draw.right(40)
draw.forward(15)
for _ in range(15):
    draw.right(12)
    draw.forward(1)
draw.forward(13)

# Hands
draw.setheading(90)
draw.forward(9)
draw.right(20)
draw.forward(2)
draw.right(16)
draw.forward(10)
    
draw.end_fill()


# ---------------------------------------
# Left and Right Leg
# ---------------------------------------
draw.penup()
draw.goto(-24, -128)
draw.pendown()
draw.color("black", "yellow")
draw.begin_fill()

draw.setheading(270)
draw.forward(24)
draw.left(90)
draw.forward(11)
draw.left(90)
draw.forward(24)
draw.end_fill()

draw.penup()
draw.goto(69, -128)
draw.pendown()
draw.begin_fill()

draw.setheading(270)
draw.forward(24)
draw.left(90)
draw.forward(11)
draw.left(90)
draw.forward(24)
draw.end_fill()



# ---------------------------------------
# Left Shoes
# ---------------------------------------
draw.penup()
draw.goto(-4, -200)
draw.pendown()
draw.color("black")
draw.begin_fill()
draw.circle(13)
draw.end_fill()

draw.penup()
draw.goto(-24, -212)
draw.pendown()
draw.begin_fill()
draw.circle(16)
draw.end_fill()

draw.penup()
draw.goto(-40, -204)
draw.pendown()
draw.color("white")
draw.begin_fill()
draw.circle(4)
draw.end_fill()

draw.penup()
draw.goto(-30, -225)
draw.pendown()
draw.color("black")
draw.begin_fill()
draw.setheading(0)
draw.left(45)
draw.forward(18)
draw.setheading(90)
draw.forward(5)
draw.left(135)
draw.forward(18)
draw.setheading(270)
draw.forward(5)
draw.end_fill()

draw.penup()
draw.goto(-15, -212)
draw.pendown()
draw.begin_fill()
draw.forward(7)
draw.left(115)
draw.forward(11)
draw.setheading(90)
draw.left(15)
draw.forward(7)
draw.setheading(180)
draw.left(16)
draw.forward(10)
draw.end_fill()


# ---------------------------------------
# Right Shoes
# ---------------------------------------
draw.setheading(90)
draw.penup()
draw.goto(87, -200)
draw.pendown()
draw.color("black")
draw.begin_fill()
draw.circle(13)
draw.end_fill()

draw.penup()
draw.goto(112, -212)
draw.pendown()
draw.begin_fill()
draw.circle(16)
draw.end_fill()

draw.penup()
draw.goto(105, -204)
draw.pendown()
draw.color("white")
draw.begin_fill()
draw.circle(4)
draw.end_fill()

draw.penup()
draw.goto(85, -225)
draw.pendown()
draw.color("black")
draw.begin_fill()
draw.setheading(180)
draw.right(45)
draw.forward(18)
draw.setheading(90)
draw.forward(5)
draw.right(135)
draw.forward(18)
draw.setheading(270)
draw.forward(5)
draw.end_fill()

draw.penup()
draw.goto(71, -218)
draw.pendown()
draw.begin_fill()
draw.right(115)
draw.forward(11)
draw.setheading(90)
draw.right(15)
draw.forward(7)
draw.setheading(0)
draw.right(16)
draw.forward(10)
draw.end_fill()


# ---------------------------------------
# Left Socks
# ---------------------------------------
draw.penup()
draw.goto(-24, -153)
draw.pendown()
draw.color("black", "white")

draw.begin_fill()
draw.setheading(270)
draw.forward(43)
draw.left(60)
for i in range(23):
    draw.left(2.9)
    draw.forward(0.5)
draw.setheading(90)
draw.forward(43)
draw.left(90)
draw.forward(11)
draw.end_fill()

draw.penup()
draw.goto(-24, -161)
draw.pendown()
draw.color("blue")
draw.setheading(0)
draw.forward(9)

draw.penup()
draw.goto(-24, -169)
draw.pendown()
draw.color("red")
draw.setheading(0)
draw.forward(9)

# ---------------------------------------
# Right Socks
# ---------------------------------------]
draw.penup()
draw.goto(69, -153)
draw.pendown()
draw.color("black", "white")

draw.begin_fill()
draw.setheading(270)
draw.forward(43)
draw.left(60)
for i in range(23):
    draw.left(2.9)
    draw.forward(0.5)
draw.setheading(90)
draw.forward(43)
draw.left(90)
draw.forward(11)
draw.end_fill()

draw.penup()
draw.goto(69, -161)
draw.pendown()
draw.color("blue")
draw.setheading(0)
draw.forward(9)

draw.penup()
draw.goto(69, -169)
draw.pendown()
draw.color("red")
draw.setheading(0)
draw.forward(9)

# ---------------------------------------
# Brown Pant Left
# ---------------------------------------
draw.penup()
draw.goto(-40, -110)
draw.pendown()
draw.color("black", "#8B6507")
draw.begin_fill()

draw.setheading(270)
draw.forward(13)
draw.left(60)

for i in range(23):
    draw.left(2.9)
    draw.forward(2)

draw.setheading(90)
draw.forward(9)
draw.left(90)
draw.forward(43)
draw.end_fill()

# ---------------------------------------
# Brown Pant Right
# ---------------------------------------
draw.penup()
draw.goto(56, -110)
draw.pendown()
draw.color("black", "#8B6507")
draw.begin_fill()

draw.setheading(270)
draw.forward(13)
draw.left(60)

for i in range(23):
    draw.left(2.9)
    draw.forward(2)

draw.setheading(90)
draw.forward(9)
draw.left(90)
draw.forward(43)
draw.end_fill()
