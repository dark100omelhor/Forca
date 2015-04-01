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
tentativas=[]
digitadas=[]
l=[]
leitura=[]
gabriel=[]
lista2=[]
letras=[]


arquivo=open("entradamemo.csv", "r+")
leitura=arquivo.read(100)
l = leitura.split(',')
palavra = random.choice(l).lower()
print(palavra)
numletras=len(palavra)
letras=palavra.split()






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
window.title("Jogo da Forca!!!!!!!###$$$@@")
#window.bgcolor("pink")
window.bgpic("batmanlogo.gif")


trave=turtle.Turtle()
trave.hideturtle()
trave.pensize(5)
trave.speed(2)
trave.penup()
trave.setpos(-300,0)
trave.pencolor("white")

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
    

e=0

while erros<6:
    wow=""
    for letra in palavra:
        wow+=letra if letra in acertos else "  " if letra==(" ") else "_ "
    getto=turtle.Turtle()
    getto.hideturtle()
    getto.penup()
    getto.setpos(-235,-200)
    getto.write(wow,move=False,align="left",font=("Arial",45,"normal"))
    
    if wow==palavra:
        break
    tentativas=window.textinput('','Digite uma letra').lower().strip()
    if tentativas=="exit":
        break
    
        
    if tentativas in digitadas:
        digitadas+=tentativas
        getto.clear()
        print("voce ja fez essa tentativa")
        continue
    else:
        digitadas+=tentativas
        getto.clear()
    if tentativas in acertos:
        continue
    if tentativas in palavra:
        acertos+=tentativas
        getto.clear
    else:
        erros=erros+1
        
    if acertos==palavra:
        print("Você ganhou")
        break
    
        
 
 
 
 
 
    if erros==1:
        bonecocabeça()
    elif erros==2:
        tronco()
    elif erros==3:
        bracoum()
    elif erros==4:
        bracodois()
    elif erros==5:
        pernaum()
    elif erros==6:
        pernadois()
        print("Perdeu")
        
       
window.exitonclick()









