import turtle
import winsound
ventana = turtle.Screen()
ventana.setup(0.6,0.4)
anchoJuego= ventana.canvwidth-40

#ventana.bgcolor("black")
ventana.title("Mi primer ejemplo con Turtle")
ventana.tracer(1)

jugador2= turtle.Turtle()
jugador2.color("blue")
jugador2.shape("square")
jugador2.speed(0)
jugador2.forward(anchoJuego)
jugador2.setheading(90)
jugador2.shapesize(1,5)
def player2sube():
    print(ventana.canvheight)
    print(jugador2.ycor())
    if jugador2.ycor()+140<=ventana.canvheight:
        jugador2.fd(20)
def player2baja():
    print(ventana.canvheight)
    print(jugador2.ycor())
    if jugador2.ycor()-130 >= -ventana.canvheight:
        jugador2.bk(20)
pelota= turtle.Turtle()
pelota.color("red")
pelota.shape("circle")
pelota.shapesize(2)
pelota.dx = 1
pelota.dy = 1

#score = turtle.Turtle()
#score.write("jugardor 1: 0   jugador 2: 0 ", align="center", font=("courier",20,"bold"))

gameOver = False
ventana.onkeypress(player2sube, "Up")
ventana.onkeypress(player2baja, "Down")
print(ventana.screensize())
while not gameOver:
    ventana.listen()
    if pelota.ycor()-10 == ventana.canvheight/2 or pelota.ycor() -10 == -ventana.canvheight/2 :
        pelota.dy *=-1
        #winsound.Beep(1000, 50)
    if pelota.xcor() ==  anchoJuego-30:
        if jugador2.ycor()-100 <= pelota.ycor() <= jugador2.ycor()+100:
            pelota.dx *=-1
    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)






ventana.exitonclick()


