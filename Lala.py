#!/usr/bin/env python3
#!/usr/bin/env python3
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
from kivy.uix.popup import Popup
import codecs
wordfile = open('wordattack.txt')
ct=0
X = []
i=0
for line in wordfile:
    X.append(line)
    print (X[i])
    i+=1    
#print (A[0])



class RootWidget(BoxLayout):
    
        
        
    def build(self):
          
        return f
    A = list(X)

class wordattack(App):
    
    def build(self):
        
        return RootWidget()

if __name__ == '__main__':
    wordattack().run()

