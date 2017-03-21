#!/usr/bin/env python3
import kivy
kivy.require('1.9.0')
import codecs
#USE THIS FOR UR UNICODE FILE
'''f = codecs.open('unicode.rst', encoding='utf-8')
for line in f:
    print repr(line)'''
import string
from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.scatter import Scatter
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty
import random

wordfile = open('wordattack.txt')
f1 = open('Reading1.txt','r')
f12 = open('Reading2.txt','r')
f2 = open('Reading1Q.txt','r')
file = open('Reading1O.txt','r')
X = []
T =[]
Ans = ""
C = []
J = 0
i=0
for line in wordfile:
    X.append(line)
    #print (X[i])
    i+=1    
for line in file:
    C.append(line)
    #print (A[i])
    i+=1    
class RootWidget(FloatLayout):

    def Submit(self):
        with open("Reading1Ans.txt", "a") as myfile:
            myfile.write(Ans)
        print("Successfully registered "+ Ans +" write")
    def login(self,usn,psw):
        if ("a" == usn and "a" == psw):
            pass
        else:
            exit()
    def score(self):
        
        fileObj1 = open("Reading1Ans.txt")
        fileObj2 = open ("Ans.txt")
        for line in myfile:
            for ch in line:
                T.append(ch)
        i = 0
        for line in fileObj2:
            for ch in line:
                if (T[i]==ch):
                    self.D+=1
                i+=1
        
            
            
    def write_to_var(self, something):
        global Ans
        Ans = something
        print (something)
    D = 2
    B = list(C)
    A = list(X)
    rc1 = f1.read()
    rc2 = f12.read()
    text1 = f2.read()
   # text2 = f22.read()

class Sample(App):
    x=""
    
    def build(self):
        
        return RootWidget()

if __name__ == '__main__':
    Sample().run()
    with open("Reading1Ans.txt", "w") as myfile:
            pass