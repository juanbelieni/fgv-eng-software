from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from utils.command import Command
from models.user import user_repository, UserRepository


class SignUpCommand(Command):
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
        self.name_input = inputs['name_input']
        self.email_input = inputs['email_input']
        self.password_input = inputs['password_input']
        self.bio_input = inputs['bio_input']

    def execute(self):
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        bio = self.bio_input.text

        return user_repository.create(
            name=name,
            email=email,
            password=password,
            bio=bio,
        )


class SignUpView(App):
    def build(self):
        self.title = 'Cadastrar'
        root = AnchorLayout(anchor_x="center", anchor_y="center")

        layout = BoxLayout(orientation='vertical',
                           spacing=10, padding=10,
                           size=(400, 400), size_hint=(None, None))

        root.add_widget(layout)

        title_label = Label(text='Cadastrar', size_hint_y=None, height=44)
        layout.add_widget(title_label)

        name_input = TextInput(hint_text='Nome', multiline=False)
        layout.add_widget(name_input)

        email_input = TextInput(hint_text='Email', multiline=False)
        layout.add_widget(email_input)

        password_input = TextInput(
            hint_text='Senha', multiline=False, password=True)
        layout.add_widget(password_input)

        bio_input = TextInput(hint_text='Bio', multiline=True)
        layout.add_widget(bio_input)

        self.sign_up_command = SignUpCommand(
            name_input=name_input,
            email_input=email_input,
            password_input=password_input,
            bio_input=bio_input,
        )

        sign_up_button = Button(text='Cadastrar', size_hint_y=None, height=44)
        sign_up_button.bind(on_press=lambda _: self.sign_up_command.execute())
        layout.add_widget(sign_up_button)

        return root


if __name__ == '__main__':
    SignUpView().run()
