
import kivy
from kivy.uix.label import Label
from kivy.app import App

kivy.require('2.2.1')


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
