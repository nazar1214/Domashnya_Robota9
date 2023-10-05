import turtle

window = turtle.Screen()
window.bgcolor("white")

rob = turtle.Turtle()
rob.shape("turtle")
rob.speed(0)

def move_forward():
    rob.forward(hod)

def move_backward():
    rob.backward(hod)

def turn_left():
    rob.left(hod)
 
def turn_right():
    rob.right(hod)

ss = input("виперідь колір сліду-black red blue: ")
rob.color(ss)

bb = input("виберідь колір заднього фону-black red blue: ")
window.bgcolor(bb)

while True:
    ap = input("Виберіть що хочете вперед назад вправо вліво або підняти пен або упустити пен або виіти ")

    if ap == "вперед":
        hod = int(input("Скільки СМ вперед ви хочете: "))
        move_forward()
    elif ap == "назад":
        hod = int(input("Скільки СМ назад ви хочете: "))
        move_backward()
    elif ap == "вправо":
        hod = int(input("Скільки СМ вправо ви хочете: "))
        turn_left()
    elif ap == "вліво":
        hod = int(input("Скільки СМ вліво ви хочете: "))
        turn_right()
    elif ap == "упустити пен":
        rob.penup()
    elif ap == "підняти пен":
        rob.penup()
    elif ap == "виіти":
        break
    else:
        print("ви написали неправилюню дію впешіть правилюну")