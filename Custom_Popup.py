from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.uix.popup import Popup
class CustomPopup(Popup):
    pass


class TestApp(App):
    def open_helpme(self, help_me):
    
        p = Popup(content=help_me,
                  title='Help Me',
                  size_hint=(0.8, 0.8))
    
        if p.content is not help_me:
            p.content = help_me
            p.open()
        else:
            super(HelpMeApp, self).display_helpme(HelpMe)
            
    def build(self):
        help_me_button = Button(text='HELP ME')
        help_me_button.bind(on_press=self.open_helpme)
        games_button = Button(text='GAMES')
        games_button.bind(on_press=self.open_games)
    
        buttons = BoxLayout(orientation='horizontal')
        buttons.add_widget(help_me_button)
        buttons.add_widget(game_button)
    
    
        return layout

    
if __name__ == '__main__':
    TestApp().run()
    
