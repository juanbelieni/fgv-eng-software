from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from utils.command import Command
from models.user import user_repository, UserRepository


class LogInCommand(Command):
    user_repository: UserRepository
    name_input: TextInput
    email_input: TextInput
    password_input: TextInput
    email_input: TextInput

    def __init__(
        self,
        user_repository=user_repository,
        **inputs: TextInput
    ):
        self.user_repository = user_repository
        self.email_input = inputs['email_input']
        self.password_input = inputs['password_input']

    def execute(self):
        email = self.email_input.text
        password = self.password_input.text

        user_repository.read(
            email=email,
            password=password,
        )


class LogInView(Screen):
    def __init__(self, **kwargs):
        super(LogInView, self).__init__(**kwargs)

        root = AnchorLayout(anchor_x="center", anchor_y="center")

        layout = BoxLayout(orientation='vertical',
                           spacing=10, padding=10,
                           size=(400, 200), size_hint=(None, None))

        root.add_widget(layout)

        title_label = Label(text='Entrar', size_hint_y=None, height=44)
        layout.add_widget(title_label)

        email_input = TextInput(hint_text='Email', multiline=False)
        layout.add_widget(email_input)

        password_input = TextInput(
            hint_text='Senha', multiline=False, password=True)
        layout.add_widget(password_input)

        self.log_in_command = LogInCommand(
            email_input=email_input,
            password_input=password_input,
        )

        log_in_button = Button(text='Entrar', size_hint_y=None, height=44)
        log_in_button.bind(on_press=lambda _: self.log_in_command.execute())
        layout.add_widget(log_in_button)

        self.add_widget(root)


if __name__ == '__main__':
    LogInView().run()
