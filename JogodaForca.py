# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:49:46 2015

@author: Homero
"""

palavra=input("Digite a palavra aqui:")
erros=0
acertos=0
digitados=[]

while True:
    tentativas=[]
    tentativas=input("Digite uma letra:")
    
    
    if erros==1:
        print("Você tem mais 5 tentativas!")
    elif erros==2:
        print("Você tem mais 4 tentativas!")
    elif erros==3:
        print("Você tem mais 3 tentativas!")
    elif erros==4:
        print("Você tem mais 2 tentativas!")
    elif erros==5:
        print("Você tem mais 1 tentativa!")
    elif erros==6:
        print("Sinto Muito, você perdeu!")
    break
