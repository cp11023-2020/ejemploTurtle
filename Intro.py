import turtle
import winsound
ventana = turtle.Screen()
#ventana.setup(0.6,0.4)
ventana.setup(800,400)
#print('ancho canv',ventana.canvwidth)
anchoJuego= ventana.canvwidth-40
#print('ancho:',anchoJuego)
#ventana.bgcolor("black")
ventana.title("Mi primer ejemplo con Turtle")
ventana.tracer(1)

#jugador1
jugador1= turtle.Turtle()
jugador1.color("blue")
jugador1.shape("square")
jugador1.speed(0)
jugador1.forward(-anchoJuego)
jugador1.setheading(90)
jugador1.shapesize(1,5)

#jugador2
jugador2= turtle.Turtle()
jugador2.color("blue")
jugador2.shape("square")
jugador2.speed(0)
jugador2.forward(anchoJuego)
jugador2.setheading(90)
jugador2.shapesize(1,5)

#funciones para el movimiento de los jugadores
def player1sube():
    #print(ventana.canvheight)
    #print(jugador1.ycor())
    if jugador1.ycor()+140<=ventana.canvheight:
        jugador1.fd(20)

def player1baja():
    #print(ventana.canvheight)
    #print(jugador1.ycor())
    if jugador1.ycor()-130 >= -ventana.canvheight:
        jugador1.bk(20)

def player2sube():
    #print(ventana.canvheight)
    #print(jugador2.ycor())
    if jugador2.ycor()+140<=ventana.canvheight:
        jugador2.fd(20)

def player2baja():
    #print(ventana.canvheight)
    #print(jugador2.ycor())
    if jugador2.ycor()-130 >= -ventana.canvheight:
        jugador2.bk(20)

#pelota
pelota= turtle.Turtle()
pelota.color("red")
pelota.shape("circle")
pelota.shapesize(2)
pelota.speed(0)
pelota.dx = 1
pelota.dy = 1

#score
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(0,ventana.canvheight/2+10)
score.write("jugardor 1: 0   jugador 2: 0 ", align="center", font=("courier",20,"bold"))
score.jugador1=0
score.jugador2=0

#teclado paraa el movimiento de los jugadores
ventana.onkeypress(player1sube, "w")
ventana.onkeypress(player1baja, "s")
ventana.onkeypress(player1sube, "W")
ventana.onkeypress(player1baja, "S")
ventana.onkeypress(player2sube, "Up")
ventana.onkeypress(player2baja, "Down")
print(ventana.screensize())

gameOver = False
while not gameOver:
    ventana.listen()

    #movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #rebote de la pelota
    if pelota.ycor()-10 == ventana.canvheight/2 or pelota.ycor() -10 == -ventana.canvheight/2 :
        pelota.dy *=-1
        #winsound.Beep(1000, 50)

    # cuando no alcanza a rebotar en el jugador1
    if pelota.xcor() < -anchoJuego-30 :
        pelota.goto(0,0)
        score.jugador2 +=1
        score.clear()
        score.write(f"jugardor 1: {score.jugador1}   jugador 2: {score.jugador2} ",
                    align="center", font=("courier", 20, "bold"))

    #cuando no alcanza a rebotar en el jugador2
    if pelota.xcor() > anchoJuego+30:
        pelota.goto(0,0)
        score.jugador1 += 1
        score.clear()
        score.write(f"jugardor 1: {score.jugador1}   jugador 2: {score.jugador2} ",
                    align="center", font=("courier", 20, "bold"))
    #rebote en el jugador1
    if pelota.xcor() == -anchoJuego + 30:
        if jugador1.ycor() - 100 <= pelota.ycor() <= jugador1.ycor() + 100:
            pelota.dx *= -1

    #rebote en el jugador2
    if pelota.xcor() ==  anchoJuego - 30:
        if jugador2.ycor()-100 <= pelota.ycor() <= jugador2.ycor()+100:
            pelota.dx *=-1


ventana.exitonclick()


