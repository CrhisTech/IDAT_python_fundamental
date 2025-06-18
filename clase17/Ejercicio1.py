import turtle
turtle.bgcolor("#202421")
RADIO_C = 90
turtle.speed(0)
turtle.penup()
turtle.setposition(-200, 100)
turtle.pendown()
turtle.ht()
turtle.title("graficos")
if True:
    turtle.begin_fill()
    turtle.color("black", "red"), turtle.circle(RADIO_C)
    turtle.end_fill()
turtle.penup()
turtle.setposition(100, 100), turtle.pendown()
if True:
    lado_cuadrado, angulo_giro = 150, 90
    turtle.color("black", "lime")
    turtle.begin_fill()
    turtle.forward(lado_cuadrado)
    turtle.right(angulo_giro)
    turtle.forward(lado_cuadrado)
    turtle.right(angulo_giro)
    turtle.forward(lado_cuadrado)
    turtle.right(angulo_giro)
    turtle.forward(lado_cuadrado)
    turtle.end_fill()

turtle.done()