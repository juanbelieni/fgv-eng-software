
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from models.user import User
from utils.command import Command
from typing import Optional
from models.user import user_repository, UserRepository
from utils.notification import notification_observer, NotificationObserver


class UpdateProfileCommand(Command):
    app: App
    user_repository: UserRepository
    notification_observer: NotificationObserver
    name_input: TextInput
    bio_input: TextInput

    def __init__(
        self,
        app: Optional[App] = None,
        user_repository=user_repository,
        notification_observer=notification_observer,
        **inputs: TextInput
    ):
        self.app = app or App.get_running_app()
        self.user_repository = user_repository
        self.notification_observer = notification_observer
        self.name_input = inputs['name_input']
        self.bio_input = inputs['bio_input']

    def execute(self):
        name = self.name_input.text
        bio = self.bio_input.text

        user = self.user_repository.update(
            self.app.user,
            name=name,
            bio=bio,
        )

        if user is not None:
            self.app.user = user
            self.notification_observer.notify("success", "Perfil atualizado")
        else:
            self.notification_observer.notify(
                "failure",
                "Não foi pessoal atualizar o perfil"
            )


class ProfileView(Screen):
    def __init__(self, **kwargs):
        super(ProfileView, self).__init__(**kwargs)

    def on_pre_enter(self):
        user: User = App.get_running_app().user

        self.clear_widgets()

        root = AnchorLayout(anchor_x="center", anchor_y="center")
        self.add_widget(root)

        layout = BoxLayout(orientation='vertical',
                           spacing=10, padding=10,
                           size=(400, 250), size_hint=(None, None))
        root.add_widget(layout)

        picture_layout = AnchorLayout(anchor_x="center")
        picture = AsyncImage(
            source='https://img-9gag-fun.9cache.com/photo/a9nrgrZ_460s.jpg',
            size=(100, 100), size_hint=(None, None)
        )
        picture_layout.add_widget(picture)
        layout.add_widget(picture_layout)
        layout.add_widget(BoxLayout(size=(0, 10)))

        name_input = TextInput(
            hint_text='Nome',
            multiline=False,
            text=user.name
        )
        layout.add_widget(name_input)

        bio_input = TextInput(hint_text='Bio', multiline=True, text=user.bio)
        layout.add_widget(bio_input)

        self.update_profile_command = UpdateProfileCommand(
            name_input=name_input,
            bio_input=bio_input,
        )

        update_profile_button = Button(
            text='Atualizar',
            size_hint_y=None,
            height=44
        )

        update_profile_button.bind(
            on_press=lambda _: self.update_profile_command.execute()
        )

        layout.add_widget(update_profile_button)
