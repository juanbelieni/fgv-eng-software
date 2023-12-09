
import kivy
from kivy.app import App
from views.auth.log_in import LogInView
from views.auth.sign_up import SignUpView
from views.auth.profile import ProfileView
from kivy.uix.screenmanager import ScreenManager
from models.user import User
from typing import Optional

kivy.require('2.2.1')


class RootApp(App):
    user: Optional[User] = None

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpView(name='sign_up'))
        sm.add_widget(LogInView(name='log_in'))
        sm.add_widget(ProfileView(name='profile'))

        sm.current = 'log_in'

        return sm


if __name__ == '__main__':
    app = RootApp()
    app.run()
