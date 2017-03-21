#!/usr/bin/env python3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Boxes>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                BoxLayout: 
                    orientation: 'vertical'
                    padding: 10
                    BoxLayout:
                        orientation: 'horizontal'
                        Button:
                            text: "1"
                    BoxLayout:
                        orientation: 'horizontal'
                        Button:
                            text: "2"
                        Button:
                            text: "3"
                        Button:
                            text: "4"
                    BoxLayout:
                        orientation: 'horizontal'
                        Button:
                            text: "5"
                        Button:
                            text: "6"
                    BoxLayout:
                        orientation: 'horizontal'
                        Button:
                            text: "7"
                        Button:
                            text: "8"
                        Button:
                            text: "9"
                        Button:
                            text: "10"
            Screen:
                name: 'screen2'
                Label: 
                    text: 'Another Screen'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Go to Screen 2'
                on_press: _screen_manager.current = 'screen2'""")

class Boxes(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return Boxes()

if __name__ == '__main__':
    TestApp().run()
