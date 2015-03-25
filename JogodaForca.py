# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:49:46 2015

@author: Homero
"""


import turtle
import random



erros=0
acertos=[]
erradas=[]
l=[]
leitura=[]

arquivo=open("entradamemo.csv", "r+")
leitura=arquivo.read(100)
l = leitura.split(',')
palavra = random.choice(l)
print(palavra)
numletras=len(palavra)


if palavra=="São Paulo":
    numletras=numletras-1
elif palavra=="São Bernardo do Campo":
    numletras=numletras-3
elif palavra=="Baleia Azul":
    numletras=numletras-1
elif palavra=="Leão Marinho":
    numletras=numletras-1

print(numletras)



window=turtle.Screen()
window.setup(width=1400, startx=None, starty=None)
window.title("Jogo da Forca!!!!!!!@@")
window.bgcolor("purple")


trave=turtle.Turtle()
trave.hideturtle()
trave.pensize(5)
trave.speed(2)
trave.penup()
trave.setpos(-300,0)

trave.pendown()
trave.forward(80)
trave.left(90)
trave.forward(-40)
trave.left(90)
trave.forward(80)
trave.right(90)
trave.forward(40)
trave.right(90)
trave.forward(40)
trave.left(90)
trave.forward(200)
trave.right(90)
trave.forward(80)
trave.right(90)
trave.forward(20)






def bonecocabeça():
     trave=turtle.Turtle()
     trave.hideturtle()
     trave.speed(5)
     trave.pensize(5)
     trave.penup()
     trave.setpos(-180,180)
     trave.left(180)
     trave.pendown()
     trave.circle(20)
     trave.color("black")
     
     
     
def tronco():
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,140)
    trave.pendown()
    trave.right(90)
    trave.forward(100)
    trave.color("black")
    
def bracoum():
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,120)
    trave.pendown()
    trave.right(135)
    trave.forward(40)
    trave.color("black")
    
    
def bracodois():
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,120)
    trave.pendown()
    trave.right(400)
    trave.forward(40)
    trave.color("black")
       
def pernaum():
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,40)
    trave.pendown()
    trave.left(220)
    trave.forward(50)
    trave.color("black")
    
def pernadois():
    trave=turtle.Turtle()
    trave.hideturtle()
    trave.speed(5)
    trave.pensize(5)
    trave.penup()
    trave.setpos(-180,40)
    trave.pendown()
    trave.left(310)
    trave.forward(50)
    trave.color("black")
    

i=1
x=0
y=0


while i<numletras:
    tracinho=turtle.Turtle()
    tracinho.hideturtle()
    tracinho.speed(10)
    tracinho.pensize(3)
    tracinho.penup()
    if i==1:
        tracinho.setpos(-200+y,-200)
    tracinho.pendown()
    tracinho.right(180)
    tracinho.forward(50)
    
    tracinho.color("red")
    tracinho.penup()
    tracinho.forward(x)

    i=i+1
    x=x+30
    y=y+30

    


    




bonecocabeça()
tronco()
bracoum()
bracodois()
pernaum()
pernadois()





window.exitonclick()









