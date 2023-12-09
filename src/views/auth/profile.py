
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from models.user import User


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
                           size=(400, 200), size_hint=(None, None))
        root.add_widget(layout)

        picture_layout = AnchorLayout(anchor_x="center")
        picture = AsyncImage(
            source='https://img-9gag-fun.9cache.com/photo/a9nrgrZ_460s.jpg',
            size=(100, 100), size_hint=(None, None)
        )
        picture_layout.add_widget(picture)
        layout.add_widget(picture_layout)

        name_label = Label(text=user.name, font_size=20)
        layout.add_widget(name_label)

        bio = user.bio if user.bio != "" else "Esse usuário não possui uma bio."

        bio_label = Label(text=bio, font_size=16)
        layout.add_widget(bio_label)
