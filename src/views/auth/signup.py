from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


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

        sign_up_button = Button(text='Sign Up', size_hint_y=None, height=44)
        sign_up_button.bind(on_press=self.sign_up)
        layout.add_widget(sign_up_button)

        return root

    def sign_up(self, instance):
        name = self.root.children[0].text
        email = self.root.children[1].text
        password = self.root.children[2].text
        bio = self.root.children[3].text

        print(f"Name: {name}\nEmail: {email}\nPassword: {password}\nBio: {bio}")


if __name__ == '__main__':
    SignUpView().run()
