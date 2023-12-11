from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from utils.command import Command
from utils.buider import BoxLayoutBuilder
from models.user import user_repository, UserRepository
from models.progress import progress_repository, ProgressRepository
from models.user import user_repository, UserRepository, User
from models.book import BookRepository, Book
from typing import Optional


class YourProgressesCommand(Command):
    """Comando para navegar entre a tela de criar progresso e excluir progresso."""

    app: App
    progress_repository: ProgressRepository

    def __init__(
        self,
        app: Optional[App] = None,
        command: str = 'create',
        id: str = None
    ):
        """
        Construtor do comando.

        Parameters:
        - app (Optional[App]): Instância do aplicativo Kivy.
        - command (str): Comando a ser executado ('create' ou 'delete').
        - id (str): ID do progresso a ser excluído.
        """
        self.app = app or App.get_running_app()
        self.command = command
        self.id = id

    def execute(self):
        """Executa o comando com base no comando especificado."""

        if self.command == 'create':
            self.app.root.current = 'create_progress'
        elif self.command == 'delete':
            progress_repository.delete(self.id)
            self.app.root.get_screen('your_progresses').on_pre_enter()


class BoxProgress(BoxLayoutBuilder):
    """Builder para criar um layout de progresso."""

    def build(self):
        """Constrói o layout de progresso."""
        self.set_orientation('vertical')
        self.set_spacing(10)
        self.set_padding(10)
        self.set_size((400, 200))

        title_label = Label(text='Seus Progressos',
                            size_hint_y=None, height=44)
        self.add_widget(title_label)

        return self

    def add_widget_progress(self, book, percent, id):
        """
        Adiciona widgets de progresso ao layout.

        Parameters:
        - book (str): Título do livro associado ao progresso.
        - percent (float): Percentual de progresso.
        - id (str): ID do progresso.
        """

        book_label = Label(text=book, size_hint_y=44, height=20)
        self.add_widget(book_label)

        porcent_label = Label(text=str(percent),
                              size_hint_y=44, height=20)
        self.add_widget(porcent_label)

        delete_button = Button(text='Deletar',
                               size_hint_y=None, height=44)
        delete_button.bind(
            on_press=lambda _: YourProgressesCommand(command='delete', id=id).execute())
        self.add_widget(delete_button)


class YourProgressesView(Screen):
    """Tela para exibir os progressos do usuário."""

    def __init__(self, **kwargs):
        """
        Construtor da tela de progressos do usuário.

        Parameters:
        - **kwargs: Argumentos adicionais passados para o construtor da superclasse.
        """
        super(YourProgressesView, self).__init__(**kwargs)

    def on_pre_enter(self):
        """Método chamado antes de entrar na tela."""

        self.clear_widgets()

        user: User = App.get_running_app().user

        root = AnchorLayout(anchor_x="center", anchor_y="center")

        layout = BoxProgress()

        root.add_widget(layout.build())

        list_progresses = progress_repository.list(user=user.id)

        if list_progresses is not None and len(list_progresses) > 0:
            for progress in list_progresses:
                # book_title = BookRepository().book_info_by_isbn(progress.book).title
                layout.add_widget_progress(book=progress.book,
                                           percent=progress.percent,
                                           id=progress.id)

        else:
            layout.add_widget(
                Label(text='Você não possui progressos cadastrados'))

        new_progress_button = Button(text='Adicionar Progresso',
                                     size_hint_y=None, height=44)
        new_progress_button.bind(
            on_press=lambda _: YourProgressesCommand().execute())
        layout.add_widget(new_progress_button)

        self.add_widget(root)


if __name__ == '__main__':
    YourProgressesView().run()
