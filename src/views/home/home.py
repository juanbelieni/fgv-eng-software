from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from utils.command import Command
from models.user import user_repository, UserRepository
from models.progress import progress_repository, ProgressRepository
from models.user import user_repository, UserRepository
from typing import Optional

class HomeCommand(Command):
    app: App
    progress_repository: ProgressRepository

    def __init__(
        self,
        app: Optional[App] = None,
        progress_repository=progress_repository,
    ):
        self.app = app or App.get_running_app()
        self.progress_repository = progress_repository

    def execute(self, command: str):
        if (command == 'create_progress'):
            self.app.root.current = 'create_progress'
        elif (command == 'your_progresses'):
            self.app.root.current = 'your_progresses'
        elif (command == 'profile'):
            self.app.root.current = 'profile'





class HomeView(Screen):
    def __init__(self, user_id= None, **kwargs):
        super(HomeView, self).__init__(**kwargs)

    def on_pre_enter(self):

        #user: User = App.get_running_app().user

        root = AnchorLayout(anchor_x="center", anchor_y="center")

        layout = BoxLayout(orientation='vertical',
                           spacing=10, padding=10,
                           size=(400, 200), size_hint=(None, None))

        root.add_widget(layout)

        title_label = Label(text='Home', size_hint_y=None, height=44)
        layout.add_widget(title_label)

        
        create_progress_button = Button(text='Criar Progresso', size_hint_y=None, height=44)
        create_progress_button.bind(on_press=lambda x: HomeCommand().execute('create_progress'))
        layout.add_widget(create_progress_button)
        create_progress_button = Button(text='Seus Progressos', size_hint_y=None, height=44)
        create_progress_button.bind(on_press=lambda x: HomeCommand().execute('your_progresses'))
        layout.add_widget(create_progress_button)
        create_progress_button = Button(text='Perfil', size_hint_y=None, height=44)
        create_progress_button.bind(on_press=lambda x: HomeCommand().execute('profile'))
        layout.add_widget(create_progress_button)

        self.add_widget(root)


if __name__ == '__main__':
    HomeView().run()
