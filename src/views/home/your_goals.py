from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.app import App
from utils.command import Command
from models.goal import goal_repository, GoalRepository
from utils.notification import notification_observer, NotificationObserver
from typing import Optional


class CreateGoalCommand(Command):
    app: App
    goal_repository: GoalRepository
    notification_observer: NotificationObserver
    name_input: TextInput
    book_input: TextInput
    deadline_input: TextInput

    def __init__(
        self,
        app: Optional[App] = None,
        goal_repository=goal_repository,
        **inputs: TextInput
    ):
        self.app = app or App.get_running_app()
        self.goal_repository = goal_repository
        self.notification_observer = notification_observer
        self.name_input = inputs['name_input']
        self.book_input = inputs['book_input']
        self.deadline_input = inputs['deadline_input']
        self.host = self.app.get_running_app().user

    def execute(self, cancel):
        if cancel == True:
            # change next line to move to home page
            self.app.root.current = "profile"
        else:
            name = self.name_input.text
            book = self.book_input.text
            deadline = self.deadline_input.text.strip()
            host = self.host

            if (deadline == None or len(deadline) == 0):
                format_deadline = None
            else:
                format_deadline = ""
                for i in deadline.split('/')[::-1]:
                    format_deadline += i+'-'
                format_deadline = format_deadline.strip('-')

                if (len(format_deadline) != 10 or
                        len(format_deadline.split('-')) != 3):
                    format_deadline = None
                elif (len(format_deadline.split('-')[0]) != 4 or
                        len(format_deadline.split('-')[1]) != 2 or
                        len(format_deadline.split('-')[2]) != 2):
                    format_deadline = None

            goal = self.goal_repository.create(
                name=name,
                host=host,
                public=0,
                book=book,
                deadline=format_deadline,
            )

            if goal is not None:
                # change next line to move to home page
                self.app.root.current = "profile"
                self.notification_observer.notify(
                    "success", "Meta criada com sucesso!"
                )
            else:
                self.app.root.current = "create_goal"
                self.notification_observer.notify(
                    "failure", "Algo deu errado!"
                )


class CreateGoalView(Screen):
    def __init__(self, **kwargs):
        super(CreateGoalView, self).__init__(**kwargs)

        root = AnchorLayout(anchor_x="center", anchor_y="center")

        layout = BoxLayout(orientation='vertical',
                           spacing=10, padding=10,
                           size=(400, 330), size_hint=(None, None))

        root.add_widget(layout)

        title_label = Label(text='Nova meta de leitura',
                            size_hint_y=None, height=44)
        layout.add_widget(title_label)

        name_input = TextInput(hint_text='Nome da meta', multiline=False)
        layout.add_widget(name_input)

        book_input = TextInput(hint_text='Livro', multiline=False)
        layout.add_widget(book_input)

        deadline_input = TextInput(
            hint_text='Prazo (DD/MM/AAAA)', multiline=False)
        layout.add_widget(deadline_input)

        self.create_goal_command = CreateGoalCommand(
            name_input=name_input,
            book_input=book_input,
            deadline_input=deadline_input
        )

        cancel_button = Button(
            text='Cancelar', size_hint_y=None,
            height=38, pos_hint={'x': 0, 'y': .15}
        )
        save_goal_button = Button(
            text='Criar', size_hint_y=None,
            height=38, pos_hint={'x': 0, 'y': .15}
        )

        save_goal_button.bind(
            on_press=lambda _: self.create_goal_command.execute(cancel=False)
        )
        cancel_button.bind(
            on_press=lambda _: self.create_goal_command.execute(cancel=True)
        )
        layout.add_widget(cancel_button)
        layout.add_widget(save_goal_button)

        self.add_widget(root)
