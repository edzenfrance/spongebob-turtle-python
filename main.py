import turtle as t

t.speed(0)
t.Screen().title("SpongeBob SquarePants")
t.shape("classic")  # Arrow, circle, classic, square, triangle, turtle


# draw_shape Function Guidelines:
# 1. If both pen_color and fill_color are not provided, it will fill with black.
# 2. If pen_color is not provided and fill_color is provided, pen_color will be set to black.
# 3. If pen_color is provided and fill_color is not, fill_color will default to pen_color.
#
# pen_color: None,  fill_color: None   =  pen_color: Default,  fill_color: Default
# pen_color: None,  fill_color: Color  =  pen_color: Default,  fill_color: Color
# pen_color: Color, fill_color: None   =  pen_color: Color,    fill_color: pen_color


def draw_shape(h_coord, v_coord, *args, width=None, height=None, pen_color=None, fill_color=None):
    t.penup()
    t.goto(h_coord, v_coord)
    t.pendown()

    if pen_color is None:
        pen_color = "black"

    t.pencolor(pen_color)

    if fill_color is None:
        fill_color = pen_color

    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    if width is not None and height is not None:
        # Draw a rectangle
        t.setheading(0)
        t.color(pen_color, fill_color)
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
        t.end_fill()
    else:
        # Draw a line
        if args:
            for i in range(0, len(args), 2):
                set_heading = args[i]
                forward_distance = args[i + 1]
                t.setheading(set_heading)
                t.forward(forward_distance)

    if fill_color:
        t.end_fill()

    t.penup()


def draw_oval(h_coord, v_coord, setheading, radius, color):
    t.penup()
    t.goto(h_coord, v_coord)
    t.pendown()
    t.setheading(setheading)
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.circle(radius, 90)
        t.circle(radius // 2, 90)

    t.end_fill()


def draw_curve(h_coord, v_coord, setheading, range_num, left, forward, pen_color=None, fill_color=None):
    t.penup()
    t.goto(h_coord, v_coord)
    t.pendown()
    t.setheading(setheading)

    if pen_color is None:
        pen_color = "black"

    t.pencolor(pen_color)

    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    for _ in range(range_num):
        t.left(left)
        t.forward(forward)

    if fill_color:
        t.end_fill()

    t.penup()


def draw_circle(h_coord, v_coord, pen_size, circle_size, pen_color=None, fill_color=None):
    t.penup()
    t.goto(h_coord, v_coord)
    t.pendown()

    if pen_color is None:
        pen_color = "black"

    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    t.pencolor(pen_color)
    t.pensize(pen_size)
    t.circle(circle_size)

    if fill_color:
        t.end_fill()

    t.penup()


def draw_shoulder(side):
    t.color("black", "white")
    t.penup()
    t.goto(-70 if side == 'left' else 130, 15)
    t.pendown()
    t.begin_fill()
    t.setheading(180 if side == 'left' else 0)
    t.left(45 if side == 'left' else -45)

    for _ in range(60):
        t.left(0.7 if side == 'left' else -0.7)
        t.forward(1)

    t.setheading(270)
    t.left(65 if side == 'left' else -65)
    t.forward(26)
    t.setheading(90)
    t.forward(63)

    t.end_fill()


def draw_hand(side):
    t.color("black", "yellow")
    t.penup()
    t.goto(-79 if side == 'left' else 137, -116)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    t.right(2 if side == 'left' else -2)
    t.forward(69)
    t.left(68 if side == 'left' else -68)
    t.forward(12)
    t.setheading(270)
    t.right(2 if side == 'left' else -2)
    t.forward(72)

    # Hands
    t.setheading(180 if side == 'left' else 0)
    t.left(45 if side == 'left' else -45)
    for _ in range(18):
        t.left(1.6 if side == 'left' else -1.6)
        t.forward(1)

    # First finger
    t.setheading(270)
    t.right(60 if side == 'left' else -60)
    t.forward(15)
    for _ in range(15):
        t.left(12 if side == 'left' else -12)
        t.forward(1)
    t.forward(12)

    # Second Finger
    t.setheading(270)
    t.right(30 if side == 'left' else -30)
    t.forward(10)
    t.right(10 if side == 'left' else -10)
    t.forward(10)
    for _ in range(15):
        t.left(12 if side == 'left' else -12)
        t.forward(1)
    t.left(5 if side == 'left' else -5)
    t.forward(15)
    t.left(5 if side == 'left' else -5)
    t.forward(5)

    # Third Finger
    t.setheading(270)
    t.right(5 if side == 'left' else -5)
    t.forward(10)
    t.right(3 if side == 'left' else -3)
    t.forward(10)
    for _ in range(15):
        t.left(12 if side == 'left' else -12)
        t.forward(1)
    t.left(4 if side == 'left' else -4)
    t.forward(10)
    t.left(3 if side == 'left' else -3)
    t.forward(5)
    t.right(6 if side == 'left' else -6)
    t.forward(10)

    # Fourth finger
    t.setheading(270)
    t.left(40 if side == 'left' else -40)
    t.forward(15)
    for _ in range(15):
        t.left(12 if side == 'left' else -12)
        t.forward(1)
    t.forward(13)

    # Hands
    t.setheading(90)
    t.forward(9)
    t.left(20 if side == 'left' else -20)
    t.forward(2)
    t.left(16 if side == 'left' else -16)
    t.forward(10)

    t.end_fill()


def draw_nose():
    t.penup()
    t.goto(25, 50)
    t.pendown()
    t.color("black", "yellow")
    t.setheading(90)
    t.begin_fill()
    t.left(10)

    for _ in range(1):
        t.right(4)
        t.forward(5)

    for _ in range(35):
        t.right(6)
        t.forward(1)
    t.forward(10)

    t.end_fill()


def main():
    t.pensize(5)

    # Background
    draw_shape(-300, -100, width=650, height=250, pen_color="#384E77")
    draw_shape(-300, -30, width=650, height=70, pen_color="#F6FBE6")
    draw_shape(-300, 0, width=650, height=30, pen_color="#AEC5A6")
    draw_shape(-300, 20, width=650, height=20, pen_color="#1651FD")
    draw_shape(-300, 20, width=650, height=20, pen_color="#1651FD")
    draw_shape(-300, 35, width=650, height=15, pen_color="#206AFB")
    draw_shape(-300, 50, width=650, height=15, pen_color="#2779FF")
    draw_shape(-300, 65, width=650, height=15, pen_color="#3297FE")
    draw_shape(-300, 75, width=650, height=10, pen_color="#44BBFF")
    draw_shape(-300, 85, width=650, height=10, pen_color="#4CCEFD")
    draw_shape(-300, 95, width=650, height=10, pen_color="#52DDFC")
    draw_shape(-300, 265, width=650, height=170, pen_color="#75FEE4")
    draw_shape(-300, 275, width=650, height=10, pen_color="#8EFFE0")
    draw_shape(-300, 285, width=650, height=10, pen_color="#9EFFCB")
    draw_shape(-300, 295, width=650, height=10, pen_color="#ABFEC8")
    draw_shape(-300, 305, width=650, height=10, pen_color="#8EFEC4")

    t.pensize(2)

    # Yellow Body
    draw_shape(-70, 150, width=200, height=220, fill_color="yellow")

    # White Uniform
    draw_shape(-70, -40, width=200, height=30, fill_color="white")

    # Brown Pants
    draw_shape(-70, -70, width=200, height=40, fill_color="#8B6507")

    # Collar
    draw_shape(18, -40, 240, 25, 145, 38, 0, 43, fill_color="white")
    draw_shape(41, -40, 300, 25, 35, 38, 180, 43, fill_color="white")

    # Pimple
    draw_oval(-55, 115, -30, 15, "#98BE0E")
    draw_oval(-23, 130, -40, 6, "#98BE0E")
    draw_oval(85, 115, -80, 17, "#98BE0E")
    draw_oval(110, 85, -30, 6, "#98BE0E")
    draw_oval(-45, -15, -60, 20, "#98BE0E")
    draw_oval(-45, 10, -30, 6, "#98BE0E")
    draw_oval(75, -15, -47, 17, "#98BE0E")
    draw_oval(95, 10, -30, 6, "#98BE0E")

    # Belt
    draw_shape(-56, -80, width=33, height=8)
    draw_shape(-5, -80, width=72, height=8)
    draw_shape(85, -80, width=33, height=8)

    # Tie
    draw_shape(41, -40, 180, 25, 295, 20, 0, 10, 65, 20, fill_color="#FF0200")
    draw_shape(24, -59, 250, 30, 320, 20, 40, 20, 109, 30, fill_color="#FF0200")

    # Teeth
    draw_shape(10, 11, 263, 15, -10, 15, 80, 14, fill_color="white")
    draw_shape(33, 8, 277, 14, 9, 15, 95, 14, fill_color="white")

    # Eyes
    draw_circle(24, 77, 2, 31, fill_color="white")
    draw_circle(96, 77, 2, 31, fill_color="white")
    draw_circle(13, 73, 2, 12, fill_color="#34C5EB")
    draw_circle(69, 73, 2, 12, fill_color="#34C5EB")
    draw_circle(5, 72, 2, 4, fill_color="black")
    draw_circle(61, 72, 2, 4, fill_color="black")

    t.pensize(3)

    # Eye lashes
    draw_shape(-20, 101, 107, 12)
    draw_shape(-8, 106, 90, 12)
    draw_shape(4, 103, 73, 12)
    draw_shape(52, 101, 107, 12)
    draw_shape(64, 106, 90, 12)
    draw_shape(78, 102, 73, 12)

    # Cheeks
    draw_curve(-8, 42, 75, 45, 5.1, 1.6, "#AC6507", "yellow")
    draw_curve(105, 35, 50, 45, 5.1, 1.6, "#AC6507", "yellow")
    draw_circle(-37, 50, 2, 0.8, "#AC6507")
    draw_circle(-29, 55, 3, 1.4, "#AC6507")
    draw_circle(-20, 52, 3, 1, "#AC6507")
    draw_circle(80, 50, 2, 0.8, "#AC6507")
    draw_circle(90, 55, 3, 1.4, "#AC6507")
    draw_circle(98, 52, 3, 1, "#AC6507")

    t.pensize(2)

    # Mouth
    draw_curve(-25, 40, 300, 40, 3, 3.5)
    draw_curve(-19, 41, 142, 17, 8, 1)
    draw_curve(95, 34, 80, 17, 8, 1)

    draw_nose()
    draw_shoulder('left')
    draw_shoulder('right')
    draw_hand('left')
    draw_hand('right')

    # Legs
    draw_shape(-24, -128, 270, 24, 0, 11, 90, 24, fill_color="yellow")
    draw_shape(69, -128, 270, 24, 0, 11, 90, 24, fill_color="yellow")

    # Shoes
    draw_circle(-4, -200, 2, 13, fill_color="black")
    draw_circle(87, -200, 2, 13, fill_color="black")
    draw_circle(-24, -212, 2, 16, fill_color="black")
    draw_circle(112, -212, 2, 16, fill_color="black")
    draw_circle(-39, -204, 2, 6, fill_color="white")
    draw_circle(106, -204, 2, 6, fill_color="white")
    draw_shape(-30, -225, 45, 18, 90, 5, 225, 18, 270, 5, fill_color="black")
    draw_shape(-15, -212, 270, 7, 25, 11, 105, 7, 196, 10, fill_color="black")
    draw_shape(85, -225, 135, 18, 90, 5, -45, 18, 270, 5, fill_color="black")
    draw_shape(71, -212, 270, 7, 155, 11, 75, 7, fill_color="black")

    # Left Socks
    draw_shape(-24, -152, 270, 43, -20, 5, 0, 1, 20, 6, 90, 43, 180, 11, fill_color="white")
    draw_shape(-24, -161, 0, 10, pen_color="blue")
    draw_shape(-24, -169, 0, 10, pen_color="red")

    # Right Socks
    draw_shape(69, -152, 270, 43, -20, 5, 0, 1, 20, 6, 90, 43, 180, 11, fill_color="white")
    draw_shape(69, -161, 0, 10, pen_color="blue")
    draw_shape(69, -169, 0, 10, pen_color="red")

    # Brown Pants Crotch
    draw_shape(-40, -110, 270, 13, -16, 12, -18, 4, 0, 10, 18, 4, 22, 15, 90, 11, 180, 43, fill_color="#8B6507")
    draw_shape(56, -110, 270, 13, -16, 12, -18, 4, 0, 10, 18, 4, 22, 15, 90, 11, 180, 43, fill_color="#8B6507")

    t.Screen().exitonclick()


if __name__ == "__main__":
    main()
