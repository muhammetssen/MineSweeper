import turtle
import random
import mine
width = 800
height = 800
column = 20
row = 20
screen = turtle.Screen()
screen.setup(width+5, height+5)
kalem = turtle.Turtle()
kalem.color("black")
kalem.penup()
turtle.tracer(100)
kalem.goto(-width/2,height/2)
for col in range(1,column+1):
    kalem.penup()
    kalem.goto(-width/2 + col * width/column,height/2)
    kalem.pendown()
    kalem.goto(-width/2 + col * width/column,-height/2)
kalem.penup()
kalem.goto(-width/2,height/2)
for r in range(1,row+1):
    kalem.penup()
    kalem.goto(-width/2,height/2 - r* height/row)
    kalem.pendown()
    kalem.goto(+width/2,height/2 - r* height/row)
kalem.hideturtle()
mine_count = 50
turtle.tracer(mine_count/2)
positions = {}
boxes = {}
for x in range(int(-width/2),int(width/2),int(width/column)):
    x = int(x+(width/column)/2)
    positions[str(x)] = [[int(x),int(a-(height/row)/2)] for a in range(int(height/2),int(-height/2),int(-height/row)) ]
for i in range(mine_count):
    mine.create(random.choice(positions[random.choice(list(positions.keys()))]))
coors = [[-1,-1],[-1,0],[-1,1],[0,1],[1,-1],[1,0],[1,1],[0,-1]]
coors2 =[[-1,0],[0,1],[1,0],[0,-1]]
 
def counter(current_name,x,y):
    if x < -width/2 or x > width/2 or y < -height/2 or y > height/2:
        return
    total = 0
    for n in coors:
        x1= x + n[0]*width/column
        y1 = y + n[1]*height/row
        n_name = mine.name_creator([x1,y1])

        if n_name in list(mine.mines.keys()):
            total += 1
    boxes[current_name] = mine.Box([x,y],total)
    if total is 0  :
        for n in coors2:
            x1= x + n[0]*width/column
            y1 = y + n[1]*height/row
            n_name = mine.name_creator([x1,y1])
            if n_name  not in boxes:
                counter(n_name,x1,y1)

def round(x, y):
    x += width/2
    y += height/2
    x = int((x//(width/column)*width/column) + width/column/2 - width/2)
    y = int((y//(height/row)*height/row) + height/row/2 - height/2)
    current_name = mine.name_creator([x,y]) 
    if current_name in list(mine.mines.keys()):
        print("game over")
        for m in list(mine.mines.keys()):
            mine.mines[m].turtle.showturtle()
        turtle.exitonclick()    
    else:
        counter(current_name,x,y)

    return [x,y]
turtle.onscreenclick(round)
going = True
turtle.onclick(round)
turtle.mainloop()
