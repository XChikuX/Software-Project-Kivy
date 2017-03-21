from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
class RootWidget(BoxLayout):
    ct=0
    orientation='vertical'
    file = ['Q1','a','b','c','Q2','d','e','f','Q3','g','h','i',]
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        optct=1
        
        g = GridLayout(rows=1, cols=3, col_default_width=10)
        for line in self.file:
            if (self.ct%4==0):
                # question here
                f = Label(text=line, font_size=32, size_hint= (1,0.3))
                self.add_widget(f)
            else:
                img = Image(size_hint= (None, None),
            size= (104, 104),
            source= 'kiwi.jpg')
                btn = Button(text= line)
                btn.add_widget(img)
                g.add_widget(btn)
                if optct%3==0:
                    # add when the last(3/3) option is in the loop
                    self.add_widget(g)
                    # reset the widget
                    g = GridLayout(rows=1, cols=3, col_default_width=10)
                optct+=1
            self.ct+=1

class Random(App):
    def build(self):
        return RootWidget()
Random().run()