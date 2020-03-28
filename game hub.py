from tkinter import *
import turtle
import time
import random

turn = 0

def PLAY():

    def ping_pong():

        main_window.withdraw()

        def show_main_window():

            game_window.destroy()
            main_window.update()
            main_window.deiconify()

        def winner(player):
        
            display = Tk()

            def play_again():

                display.destroy()
                PLAY()

            Label(display, text = player + ' WINS!!!', bg='white', fg='red', font=('Comic Sans MS', 40, 'bold')).grid(columnspan=2)
            Button(display, text = 'PLAY AGAIN', command = play_again).grid(row=1, column=0)
            Button(display, text = 'QUIT', command = display.destroy).grid(row=1, column=1)
            
            display.mainloop()

        def data_entry():

            game_window.withdraw()

            def show_game_window():

                entry_window.destroy()
                game_window.update()
                game_window.deiconify()

            def play_game():

                entry_window.withdraw()

                player1 = e1.get()
                player2 = e2.get()

                screen_width = 800
                screen_height = 600

                bar_width = 5
                bar_height = 1

                screen = turtle.Screen()
                screen.title('PING PONG')
                screen.bgcolor('black')
                screen.setup(screen_width, screen_height)
                screen.tracer(0)
            
                P1 = turtle.Turtle()
                P1.shape('square')
                P1.shapesize(bar_width, bar_height)
                P1.color('white')
                P1.up()
                P1.goto(-350,0)

                P2 = turtle.Turtle()
                P2.shape('square')
                P2.shapesize(bar_width, bar_height)
                P2.color('white')
                P2.up()
                P2.goto(350,0)

                ball = turtle.Turtle()
                ball.speed(0)
                ball.shape('circle')
                ball.color('white')
                ball.up()
                ball.goto(0,0)
                ball.dx = 0.2
                ball.dy = 0.2

                def P1_up():
                    y = P1.ycor()
                    if y < 250:
                        y += 10
                    else:
                        y = 250
                    P1.sety(y)

                def P1_down():
                    y = P1.ycor()
                    if y > -240:
                        y -= 10
                    else:
                        y = -240
                    P1.sety(y)

                def P2_up():
                    y = P2.ycor()
                    if y < 250:
                        y += 10
                    else:
                        y = 250
                    P2.sety(y)

                def P2_down():
                    y = P2.ycor()
                    if y > -240:
                        y -= 10
                    else:
                        y = -240
                    P2.sety(y)

                game_over = False
    
                while not game_over:
                    
                    screen.listen()
                    screen.onkeypress(P1_up,'w')
                    screen.onkeypress(P2_up,'Up')
                    screen.onkeypress(P1_down,'s')
                    screen.onkeypress(P2_down,'Down')
                    screen.update()
                    ball.setx(ball.xcor() + ball.dx)
                    ball.sety(ball.ycor() + ball.dy)
                    if(ball.ycor() > 290):
                        ball.sety(290)
                        ball.dy *= -1
                    elif(ball.ycor() < -290):
                        ball.sety(-290)
                        ball.dy *= -1
                    if(ball.xcor() > 390):
                        screen.bye()
                        winner(player1)
                        game_over = True
                    elif(ball.xcor() < -390):
                        screen.bye()
                        winner(player2)
                        game_over = True
                    if((ball.xcor() > 340 and ball.xcor() < 341) and (ball.ycor() < P2.ycor()+50 and ball.ycor() > P2.ycor()-50)):
                        ball.setx(340)
                        ball.dx *= -1
                    if((ball.xcor() < -340 and ball.xcor() > -341) and (ball.ycor() < P1.ycor()+50 and ball.ycor() > P1.ycor()-50)):
                        ball.setx(-340)
                        ball.dx *= -1

                screen.mainloop()
        
            entry_window = Tk()

            Label(entry_window, text = 'PLEASE ENTER YOUR NAMES TO START THE GAME!!!').grid(columnspan=2)
            Label(entry_window, text = "PLAYER 1").grid(row=2)
            Label(entry_window, text = "PLAYER 2").grid(row=3)

            e1 = Entry(entry_window)
            e2 = Entry(entry_window)

            e1.grid(row=2, column=1)
            e2.grid(row=3, column=1)

            Button(entry_window, text = 'CONTINUE', command = play_game).grid(columnspan=2)
            Button(entry_window, text = 'BACK', command = show_game_window).grid(row=6, column=0)
            Button(entry_window, text = 'QUIT', command = entry_window.destroy).grid(row=6, column=1)

            entry_window.mainloop()

        game_window = Tk()

        topframe = Frame(game_window)
        topframe.pack()
        bottomframe = Frame(game_window)
        bottomframe.pack()

        Button(topframe, text = 'PLAY GAME', command = data_entry).pack()
        Button(bottomframe, text = 'BACK', command = show_main_window).pack(side=LEFT)
        Button(bottomframe, text = 'QUIT', command = game_window.destroy).pack(side=RIGHT)

        game_window.mainloop()

    def tic_tac_toe():

        main_window.withdraw()

        def show_main_window():

            game_window.destroy()
            main_window.update()
            main_window.deiconify()

        def winner(player):
        
            display = Tk()

            def play_again():

                display.destroy()
                PLAY()

            Label(display, text = player + ' WINS!!!', bg='white', fg='red', font=('Comic Sans MS', 40, 'bold')).grid(columnspan=2)
            Button(display, text = 'PLAY AGAIN', command = play_again).grid(row=1, column=0)
            Button(display, text = 'QUIT', command = display.destroy).grid(row=1, column=1)
            
            display.mainloop()

        def data_entry():

            game_window.withdraw()

            def show_game_window():

                entry_window.destroy()
                game_window.update()
                game_window.deiconify()

            def play_game():

                entry_window.withdraw()

                player1 = e1.get()
                player2 = e2.get()

                SIZE = 600
                XO = {0:'X', 1:'O'} 
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

                while not game_over:

                    screen.update()

                    def winning_turn():
                        for r in range(3):
                            if (matrix[r][0] != None) and (matrix[r][1] != None) and (matrix[r][2] != None): 
                                if (matrix[r][0] == matrix[r][1]) and (matrix[r][1] == matrix[r][2]):
                                    screen.bye()
                                    if XO[turn] == 'X':
                                        winner(player1)
                                    else:
                                        winner(player2)
                        for c in range(3):
                            if (matrix[0][c] != None) and (matrix[1][c] != None) and (matrix[2][c] != None):
                                if (matrix[0][c] == matrix[1][c]) and (matrix[1][c] == matrix[2][c]):
                                    screen.bye()
                                    if XO[turn] == 'X':
                                        winner(player1)
                                    else:
                                        winner(player2)
                        if (matrix[0][0] != None) and (matrix[1][1] != None) and (matrix[2][2] != None):
                            if (matrix[0][0] == matrix[1][1]) and (matrix[1][1] == matrix[2][2]):
                                screen.bye()
                                if XO[turn] == 'X':
                                    winner(player1)
                                else:
                                    winner(player2)
                        if (matrix[0][2] != None) and (matrix[1][1] != None) and (matrix[2][0] != None):
                            if (matrix[0][2] == matrix[1][1]) and (matrix[1][1] == matrix[2][0]):
                                screen.bye()
                                if XO[turn] == 'X':
                                    winner(player1)
                                else:
                                    winner(player2)
                    
                    def draw_cross(x,y):
                        pen.goto(x + SIZE/30, y + SIZE/30)
                        pen.down()
                        pen.goto(x + SIZE*0.3, y + SIZE*0.3)
                        pen.up()
                        pen.goto(x + SIZE/30, y + SIZE*0.3)
                        pen.down()
                        pen.goto(x + SIZE*0.3, y + SIZE/30)
                        pen.up()
                        winning_turn()

                    def draw_circle(x,y):
                        pen.goto(x + SIZE/6, y + SIZE/30)
                        pen.down()
                        pen.circle(SIZE/6 - SIZE/30)
                        pen.up()
                        winning_turn()

                    def draw(x,y):
                        
                        global turn
                        if ((x >= -SIZE/2) and (x <= -SIZE/6)):
                            if ((y <= SIZE/2) and (y >= SIZE/6)):
                                if (matrix[0][0] == None):
                                    matrix[0][0] = XO[turn]
                                    draw_cross(-SIZE/2, SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/2, SIZE/6)
                            elif ((y <= SIZE/6) and (y >= -SIZE/6)):
                                if (matrix[0][1] == None):
                                    matrix[0][1] = XO[turn]
                                    draw_cross(-SIZE/2, -SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/2, -SIZE/6)
                            if ((y <= -SIZE/6) and (y >= -SIZE/2)):
                                if (matrix[0][2] == None):
                                    matrix[0][2] = XO[turn]
                                    draw_cross(-SIZE/2, -SIZE/2) if(XO[turn] == 'X') else draw_circle(-SIZE/2, -SIZE/2)
                        elif ((x >= -SIZE/6) and (x <= SIZE/6)):
                            if ((y <= SIZE/2) and (y >= SIZE/6)):
                                if (matrix[1][0] == None):
                                    matrix[1][0] = XO[turn]
                                    draw_cross(-SIZE/6, SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/6, SIZE/6)
                            elif ((y <= SIZE/6) and (y >= -SIZE/6)):
                                if (matrix[1][1] == None):
                                    matrix[1][1] = XO[turn]
                                    draw_cross(-SIZE/6, -SIZE/6) if(XO[turn] == 'X') else draw_circle(-SIZE/6, -SIZE/6)
                            if ((y <= -SIZE/6) and (y >= -SIZE/2)):
                                if (matrix[1][2] == None):
                                    matrix[1][2] = XO[turn]
                                    draw_cross(-SIZE/6, -SIZE/2) if(XO[turn] == 'X') else draw_circle(-SIZE/6, -SIZE/2)
                        elif ((x >= SIZE/6) and (x <= SIZE/2)):
                            if ((y <= SIZE/2) and (y >= SIZE/6)):
                                if (matrix[2][0] == None):
                                    matrix[2][0] = XO[turn]
                                    draw_cross(SIZE/6, SIZE/6) if(XO[turn] == 'X') else draw_circle(SIZE/6, SIZE/6)
                            elif ((y <= SIZE/6) and (y >= -SIZE/6)):
                                if (matrix[2][1] == None):
                                    matrix[2][1] = XO[turn]
                                    draw_cross(SIZE/6, -SIZE/6) if(XO[turn] == 'X') else draw_circle(SIZE/6, -SIZE/6)
                            if ((y <= -SIZE/6) and (y >= -SIZE/2)):
                                if (matrix[2][2] == None):
                                    matrix[2][2] = XO[turn]
                                    draw_cross(SIZE/6, -SIZE/2) if(XO[turn] == 'X') else draw_circle(SIZE/6, -SIZE/2)
                    
                        turn += 1
                        turn %= 2

                    screen.onscreenclick(draw)
                    screen.mainloop()
        
            entry_window = Tk()

            Label(entry_window, text = 'PLEASE ENTER YOUR NAMES TO START THE GAME!!!').grid(columnspan=2)
            Label(entry_window, text = "PLAYER 1").grid(row=2)
            Label(entry_window, text = "PLAYER 2").grid(row=3)

            e1 = Entry(entry_window)
            e2 = Entry(entry_window)

            e1.grid(row=2, column=1)
            e2.grid(row=3, column=1)

            Button(entry_window, text = 'CONTINUE', command = play_game).grid(columnspan=2)
            Button(entry_window, text = 'BACK', command = show_game_window).grid(row=6, column=0)
            Button(entry_window, text = 'QUIT', command = entry_window.destroy).grid(row=6, column=1)

            entry_window.mainloop()

        game_window = Tk()

        topframe = Frame(game_window)
        topframe.pack()
        bottomframe = Frame(game_window)
        bottomframe.pack()

        Button(topframe, text = 'PLAY GAME', command = data_entry).pack()
        Button(bottomframe, text = 'BACK', command = show_main_window).pack(side=LEFT)
        Button(bottomframe, text = 'QUIT', command = game_window.destroy).pack(side=RIGHT)

        game_window.mainloop()    
    

    def snake_game():

        main_window.withdraw()

        def show_main_window():

            game_window.destroy()
            main_window.update()
            main_window.deiconify()

        def display_score(player, score):
        
            display = Tk()

            def play_again():

                display.destroy()
                PLAY()

            Label(display, text = player, bg='white', fg='red', font=('Comic Sans MS', 40, 'bold')).grid(columnspan=2)
            Label(display, text = 'SCORE:\t' + str(score), fg='red', font=('Comic Sans MS', 40, 'bold')).grid(columnspan=2)
            Button(display, text = 'PLAY AGAIN', command = play_again).grid(row=2, column=0)
            Button(display, text = 'QUIT', command = display.destroy).grid(row=2, column=1)
            
            display.mainloop()

        def data_entry():

            game_window.withdraw()

            def show_game_window():

                entry_window.destroy()
                game_window.update()
                game_window.deiconify()

            def play_game():

                entry_window.withdraw()

                player_name = e.get()

                delay = 0.1
                score = 0
                
                boundary_width = 620
                boundary_height = 620

                screen = turtle.Screen()
                screen.title('Snake Game')
                screen.bgcolor('green')
                screen.setup(width = 1500, height = 800)
                screen.tracer(0)

                boundary = turtle.Turtle()
                boundary.speed(0)
                boundary.color('black')
                boundary.hideturtle()
                boundary.pensize(3)
                boundary.up()
                boundary.goto(-boundary_width/2, -boundary_height/2)
                boundary.down()
                for i in range(4):
                    if i%2 == 0:
                        boundary.forward(boundary_width)
                    else:
                        boundary.forward(boundary_height)
                    boundary.left(90)

                snake_head = turtle.Turtle()
                snake_head.speed(0)
                snake_head.color('blue')
                snake_head.shape('square')
                snake_head.up()
                snake_head.direction = 'stop'

                snake_body = []

                snake_food = turtle.Turtle()
                snake_food.speed(0)
                snake_food.color('red')
                snake_food.shape('circle')
                snake_food.up()
                snake_food.goto(random.randint(-boundary_width/2 + 15, boundary_width/2 - 15), random.randint(-boundary_height/2 + 15, boundary_height/2 - 15))

                pen = turtle.Turtle()
                pen.speed(0)
                pen.color('white')
                pen.hideturtle()
                pen.up()
                pen.goto(0, -boundary_height/2 - 50)
                pen.write('SCORE: {}'.format(score), align = 'center', font = ('Comic Sans MS', 20, 'bold'))

                def go_up():
                    if snake_head.direction != 'down':
                        snake_head.direction = 'up'

                def go_down():
                    if snake_head.direction != 'up':
                        snake_head.direction = 'down'

                def go_left():
                    if snake_head.direction != 'right':
                        snake_head.direction = 'left'

                def go_right():
                    if snake_head.direction != 'left':
                        snake_head.direction = 'right'

                def move():
                
                    if snake_head.direction == 'up':
                        snake_head.sety(snake_head.ycor() + 20)

                    if snake_head.direction == 'down':
                        snake_head.sety(snake_head.ycor() - 20)

                    if snake_head.direction == 'left':
                        snake_head.setx(snake_head.xcor() - 20)

                    if snake_head.direction == 'right':
                        snake_head.setx(snake_head.xcor() + 20)

                turtle.listen()
                turtle.onkeypress(go_left, 'Left')
                turtle.onkeypress(go_right, 'Right')
                turtle.onkeypress(go_up, 'Up')
                turtle.onkeypress(go_down, 'Down')

                while True:

                    screen.update()

                    if snake_head.distance(snake_food) < 20:
                        score += 1
                        snake_food.goto(random.randint(-boundary_width/2 + 15, boundary_width/2 - 15), random.randint(-boundary_height/2 + 15, boundary_height/2 - 15))
                    
                        body = turtle.Turtle()
                        body.speed(0)
                        body.color('black')
                        body.shape('square')
                        body.up()
                        snake_body.append(body)

                        pen.clear()
                        pen.write('SCORE: {}'.format(score), align = 'center', font = ('Comic Sans MS', 20, 'bold'))

                        delay -= 0.001

                    for i in range(len(snake_body)-1, 0, -1):
                        snake_body[i].goto(snake_body[i-1].xcor(), snake_body[i-1].ycor())

                    if len(snake_body) > 0:
                        snake_body[0].goto(snake_head.xcor(), snake_head.ycor())

                    move()

                    if (snake_head.xcor() > (boundary_width/2 - 10)) or (snake_head.xcor() < (-boundary_width/2 + 10)) or (snake_head.ycor() > (boundary_height/2 - 10)) or (snake_head.ycor() < (-boundary_height/2 + 10)):
                        screen.bye()
                        display_score(player_name, score)

                    for i in range(1, len(snake_body)):
                        if(snake_body[i].distance(snake_head) < 20):
                            screen.bye()
                            display_name(player_name, score)
                        
                    time.sleep(delay)

                screen.mainloop()
        
            entry_window = Tk()

            Label(entry_window, text = 'PLEASE ENTER YOUR NAME TO START THE GAME!!!').grid(columnspan=2)
            Label(entry_window, text = "PLAYER NAME").grid(row=2)

            e = Entry(entry_window)
            e.grid(row=2, column=1)

            Button(entry_window, text = 'CONTINUE', command = play_game).grid(columnspan=2)
            Button(entry_window, text = 'BACK', command = show_game_window).grid(row=5, column=0)
            Button(entry_window, text = 'QUIT', command = entry_window.destroy).grid(row=5, column=1)

            entry_window.mainloop()

        game_window = Tk()

        topframe = Frame(game_window)
        topframe.pack()
        bottomframe = Frame(game_window)
        bottomframe.pack()

        Button(topframe, text = 'PLAY GAME', command = data_entry).pack()
        Button(bottomframe, text = 'BACK', command = show_main_window).pack(side=LEFT)
        Button(bottomframe, text = 'QUIT', command = game_window.destroy).pack(side=RIGHT)

        game_window.mainloop()

    main_window = Tk()

    Label(main_window, text = 'PLEASE CHOOSE A GAME').pack()
    Button(main_window, text = 'PING PONG', command = ping_pong).pack()
    Button(main_window, text = 'TIC TAC TOE', command = tic_tac_toe).pack()
    Button(main_window, text = 'SNAKE GAME', command = snake_game).pack()
    Button(main_window, text = 'QUIT', command = main_window.destroy).pack()

    main_window.mainloop()

PLAY()
