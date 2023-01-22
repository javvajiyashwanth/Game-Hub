import turtle

SIZE = 600
turn = 0
XO = {0: 'X', 1: 'O'}
matrix = [[None for r in range(3)] for c in range(3)]
game_over = False

screen = turtle.Screen()
screen.title('TIC-TAC-TOE')
screen.bgcolor('black')
screen.setup(SIZE, SIZE)
screen.tracer(0)

pen = turtle.Turtle()
pen.color('white')
pen.width(10)
pen.up()

pen.goto(-SIZE/2, SIZE/6)
pen.down()
pen.forward(SIZE)
pen.up()
pen.goto(-SIZE/2, -SIZE/6)
pen.down()
pen.forward(SIZE)
pen.up()
pen.hideturtle()

pen.left(90)
pen.goto(-SIZE/6, -SIZE/2)
pen.down()
pen.forward(SIZE)
pen.up()
pen.goto(SIZE/6, -SIZE/2)
pen.down()
pen.forward(SIZE)
pen.up()
pen.right(90)
pen.hideturtle()


def check_win():
    for r in range(3):
        if (matrix[r][0] != None) and (matrix[r][1] != None) and (matrix[r][2] != None):
            if (matrix[r][0] == matrix[r][1]) and (matrix[r][1] == matrix[r][2]):
                screen.bye()
                return True
    for c in range(3):
        if (matrix[0][c] != None) and (matrix[1][c] != None) and (matrix[2][c] != None):
            if (matrix[0][c] == matrix[1][c]) and (matrix[1][c] == matrix[2][c]):
                screen.bye()
                return True
    if (matrix[0][0] != None) and (matrix[1][1] != None) and (matrix[2][2] != None):
        if (matrix[0][0] == matrix[1][1]) and (matrix[1][1] == matrix[2][2]):
            screen.bye()
            return True
    if (matrix[0][2] != None) and (matrix[1][1] != None) and (matrix[2][0] != None):
        if (matrix[0][2] == matrix[1][1]) and (matrix[1][1] == matrix[2][0]):
            screen.bye()
            return True
    return False


def draw_cross(x, y):
    pen.goto(x + SIZE/30, y + SIZE/30)
    pen.down()
    pen.goto(x + SIZE*0.3, y + SIZE*0.3)
    pen.up()
    pen.goto(x + SIZE/30, y + SIZE*0.3)
    pen.down()
    pen.goto(x + SIZE*0.3, y + SIZE/30)
    pen.up()


def draw_circle(x, y):
    pen.goto(x + SIZE/6, y + SIZE/30)
    pen.down()
    pen.circle(SIZE/6 - SIZE/30)
    pen.up()


def on_click(x, y):
    global turn
    global game_over
    if ((x >= -SIZE/2) and (x <= -SIZE/6)):
        if ((y <= SIZE/2) and (y >= SIZE/6)):
            if (matrix[0][0] == None):
                matrix[0][0] = XO[turn]
                draw_cross(-SIZE/2, SIZE /
                           6) if (XO[turn] == 'X') else draw_circle(-SIZE/2, SIZE/6)
        elif ((y <= SIZE/6) and (y >= -SIZE/6)):
            if (matrix[0][1] == None):
                matrix[0][1] = XO[turn]
                draw_cross(-SIZE/2, -SIZE /
                           6) if (XO[turn] == 'X') else draw_circle(-SIZE/2, -SIZE/6)
        if ((y <= -SIZE/6) and (y >= -SIZE/2)):
            if (matrix[0][2] == None):
                matrix[0][2] = XO[turn]
                draw_cross(-SIZE/2, -SIZE /
                           2) if (XO[turn] == 'X') else draw_circle(-SIZE/2, -SIZE/2)
    elif ((x >= -SIZE/6) and (x <= SIZE/6)):
        if ((y <= SIZE/2) and (y >= SIZE/6)):
            if (matrix[1][0] == None):
                matrix[1][0] = XO[turn]
                draw_cross(-SIZE/6, SIZE /
                           6) if (XO[turn] == 'X') else draw_circle(-SIZE/6, SIZE/6)
        elif ((y <= SIZE/6) and (y >= -SIZE/6)):
            if (matrix[1][1] == None):
                matrix[1][1] = XO[turn]
                draw_cross(-SIZE/6, -SIZE /
                           6) if (XO[turn] == 'X') else draw_circle(-SIZE/6, -SIZE/6)
        if ((y <= -SIZE/6) and (y >= -SIZE/2)):
            if (matrix[1][2] == None):
                matrix[1][2] = XO[turn]
                draw_cross(-SIZE/6, -SIZE /
                           2) if (XO[turn] == 'X') else draw_circle(-SIZE/6, -SIZE/2)
    elif ((x >= SIZE/6) and (x <= SIZE/2)):
        if ((y <= SIZE/2) and (y >= SIZE/6)):
            if (matrix[2][0] == None):
                matrix[2][0] = XO[turn]
                draw_cross(
                    SIZE/6, SIZE/6) if (XO[turn] == 'X') else draw_circle(SIZE/6, SIZE/6)
        elif ((y <= SIZE/6) and (y >= -SIZE/6)):
            if (matrix[2][1] == None):
                matrix[2][1] = XO[turn]
                draw_cross(
                    SIZE/6, -SIZE/6) if (XO[turn] == 'X') else draw_circle(SIZE/6, -SIZE/6)
        if ((y <= -SIZE/6) and (y >= -SIZE/2)):
            if (matrix[2][2] == None):
                matrix[2][2] = XO[turn]
                draw_cross(
                    SIZE/6, -SIZE/2) if (XO[turn] == 'X') else draw_circle(SIZE/6, -SIZE/2)
    turn = (turn + 1) % 2
    game_over = check_win()
    if game_over:
        screen.bye()
    elif all(val is not None for row in matrix for val in row):
        screen.bye()
        print("Game Drawn")
    screen.update()

screen.onclick(on_click)
screen.listen()
turtle.mainloop()