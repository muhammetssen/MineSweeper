import turtle
mines = {}
game_end = False
def create(position):
    name = name_creator(position)
    mines[name] = Mine(position)

class Mine():
    def __init__(self,position):
        self.x = position[0]
        self.y = position[1]
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.color("red")
        self.turtle.goto(position)
        self.turtle.shape("circle")
        self.turtle.hideturtle()

        self.revealed = False
class Box():
    def __init__(self,position,value):
        self.x = position[0]
        self.y = position[1]
        self.name = name_creator(position)
        self.value = value
        self.turtle  = turtle.Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.shape("square")
        self.turtle.shapesize(2,2)
        self.turtle.color("grey")
        self.turtle.goto(position)
        if value is not 0:
            self.turtle.write(value,font=('Arial',12,'normal'))
            self.turtle.color("black")
        else:
            self.turtle.showturtle()
    

def name_creator(position):
    return str(int(position[0]))+";"+str(int(position[1]))

