
import kivy
from kivy.app import App
from views.auth.log_in import LogInView
from views.auth.sign_up import SignUpView
from kivy.uix.screenmanager import ScreenManager

kivy.require('2.2.1')


class RootApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpView(name='sign_up'))
        sm.add_widget(LogInView(name='log_in'))
        return sm


if __name__ == '__main__':
    RootApp().run()
