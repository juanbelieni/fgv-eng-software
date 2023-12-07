
import kivy
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from models import *

kivy.require('2.2.1')


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)

        self.add_widget(Label(text='Login'))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        login_button = Button(text='Login', on_press=self.login)
        self.add_widget(login_button)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Aqui você pode adicionar lógica para verificar o nome de usuário e senha
        if sha256(password).hexdigest() == self.db.execute("select password in user where email = ?", (email,)):
            print('oi')
            return True
        else:
            print('tchal')
            return False


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
