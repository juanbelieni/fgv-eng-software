from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.app import App
from utils.command import Command
from utils.buider import BoxLayoutBuilder
from models.user import user_repository, UserRepository
from models.progress import progress_repository, ProgressRepository
from models.user import user_repository, UserRepository, User
from typing import Optional


class CreateProgressesCommand(Command):
    app: App
    progress_repository: ProgressRepository
    book_input: TextInput
    percent_input: int
    user_id: str

    def __init__(
        self,
        app: Optional[App] = None,
        progress_repository=progress_repository,
        **inputs: TextInput
    ):
        self.app = app or App.get_running_app()
        self.user_id = App.get_running_app().user.id
        self.progress_repository = progress_repository
        self.book_input = inputs['book_input']

    def execute(self):
        book=self.book_input.text
        user_id=self.user_id
        percent=0

        progress = self.progress_repository.create(
            user=user_id,
            book=book,
            percent=percent,
        )

        if progress is not None:
            self.app.root.current = 'your_progresses'


class BoxCreateProgress(BoxLayoutBuilder):

    def build(self):
        self.set_orientation('vertical')
        self.set_spacing(10)
        self.set_padding(10)
        self.set_size((400, 200))
        self.set_size_hint((None, None))

        title_label = Label(text='Novo Progressos',
                            size_hint_y=None, height=44)
        self.add_widget(title_label)

        return self


class CreateProgressView(Screen):
    def __init__(self, **kwargs):
        super(CreateProgressView, self).__init__(**kwargs)

    def show_options(self, instance):
        self.dropdown.open(instance)

    def select_option(self, option):
        self.selected_option_label.text = f'Opção selecionada: {option}'
        self.dropdown.dismiss()

    def on_pre_enter(self):

        self.clear_widgets()

        user: User = App.get_running_app().user

        root = AnchorLayout(anchor_x="center", anchor_y="center")

        layout = BoxCreateProgress()

        root.add_widget(layout.build())

        book_input = TextInput( text = "Livro", multiline=False)
        layout.add_widget(book_input)


        self.dropdown_button = Button(text='Selecione uma opção')
        self.dropdown_button.bind(on_release=self.show_options)

        self.selected_option_label = Label(text='Nenhuma opção selecionada')
        layout.add_widget(self.selected_option_label)
        
        self.dropdown = DropDown()

        self.options = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

        for option in self.options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.new_progress = CreateProgressesCommand(
            book_input =book_input,
            percent_input = 0,
            user_id = user.id,
        )

        
        log_in_button = Button(text='Adicionar Progresso',
                               size_hint_y=None, height=44)
        log_in_button.bind( on_press=lambda x: self.new_progress.execute())
        layout.add_widget(log_in_button)

        self.add_widget(root)


if __name__ == '__main__':
    CreateProgressView().run()
