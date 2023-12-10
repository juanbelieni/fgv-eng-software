
import kivy
from kivy.app import App
from views.auth.log_in import LogInView
from views.auth.sign_up import SignUpView
from views.auth.profile import ProfileView
from views.home.your_progresses import YourProgressesView
from views.home.create_progress import CreateProgressView
from views.home.home import HomeView
from kivy.uix.screenmanager import ScreenManager
from models.user import User
from typing import Optional

kivy.require('2.2.1')

from models.user import user_repository, UserRepository
from models.progress import progress_repository, ProgressRepository

class RootApp(App):
    user: Optional[User] = None

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpView(name='sign_up'))
        sm.add_widget(LogInView(name='log_in'))
        sm.add_widget(HomeView(name='home'))
        sm.add_widget(ProfileView(name='profile'))
        sm.add_widget(YourProgressesView(name='your_progresses'))
        sm.add_widget(CreateProgressView(name='create_progress'))

        sm.current = 'log_in'

        return sm


if __name__ == '__main__':
    app = RootApp()
    app.run()
