
import kivy
from kivy.app import App
from views.auth.log_in import LogInView
from views.auth.sign_up import SignUpView
from views.auth.profile import ProfileView
from views.home.your_progresses import YourProgressesView
from views.home.create_progress import CreateProgressView
from views.home.home import HomeView
from views.home.your_goals import CreateGoalView
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.user import User
from typing import Optional
from utils.notification import notification_observer

kivy.require('2.2.1')

from models.user import user_repository, UserRepository
from models.progress import progress_repository, ProgressRepository

class RootApp(App):
    user: Optional[User] = None

    def __init__(self, **kwargs):
        super(RootApp, self).__init__(**kwargs)

        notification_observer.subscribe("success", lambda message: Popup(
            title="Sucesso",
            content=Label(text=message),
            size_hint=(None, None),
            size=(250, 200)
        ).open())

        notification_observer.subscribe("failure", lambda message: Popup(
            title="Falha",
            content=Label(text=message),
            size_hint=(None, None),
            size=(250, 200)
        ).open())

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpView(name='sign_up'))
        sm.add_widget(LogInView(name='log_in'))
        sm.add_widget(HomeView(name='home'))
        sm.add_widget(ProfileView(name='profile'))
        sm.add_widget(YourProgressesView(name='your_progresses'))
        sm.add_widget(CreateProgressView(name='create_progress'))
        sm.add_widget(CreateGoalView(name='create_goal'))

        sm.current = 'create_goal'
        return sm


if __name__ == '__main__':
    app = RootApp()
    app.run()
