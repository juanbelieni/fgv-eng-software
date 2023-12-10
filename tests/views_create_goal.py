from unittest.mock import Mock, MagicMock
from views.home.your_goals import CreateGoalCommand
from models.user import User
from models.goal import Goal

def test_create_goal_command_success():
    app_mock = MagicMock()
    app_mock.root.current = "create_goal"

    app_mock.user = User(
        "user123", "Joãozinho", "joao@fgv.br", ""
    )

    goal_repository_mock = Mock()
    goal_repository_mock.create.return_value = Goal(
        id="123",
        name="Minha meta",
        host="user123",
        public=0,
        hidden=0,
        book="Livro",
        deadline="2023-12-31"
    )

    name_input_mock = Mock()
    book_input_mock = Mock()
    deadline_input_mock = Mock()

    name_input_mock.text = "Minha meta"
    book_input_mock.text = "Era uma vez"
    deadline_input_mock.text = "21/12/2023"

    command = CreateGoalCommand(
        app=app_mock,
        goal_repository=goal_repository_mock,
        name_input=name_input_mock,
        book_input=book_input_mock,
        deadline_input=deadline_input_mock,
    )

    command.execute()

    assert goal_repository_mock.create.called_with(
        name="Minha meta",
        host="user123",
        public=0,
        book="Livro",
        deadline="2023-12-21",
    )
    assert type(app_mock.user) == User
    assert command.app.root.current == 'create_goal'

def test_create_goal_command_failure():
    app_mock = MagicMock()
    app_mock.root.current = "create_goal"
    app_mock.user = None

    notification_observer = MagicMock()

    goal_repository_mock = Mock()
    goal_repository_mock.read.return_value = None

    name_input_mock = Mock()
    book_input_mock = Mock()
    deadline_input_mock = Mock()

    name_input_mock.text = "Minha meta"
    book_input_mock.text = "Era uma vez"
    deadline_input_mock.text = "21/12/2023"

    command = CreateGoalCommand(
        app=app_mock,
        goal_repository=goal_repository_mock,
        name_input=name_input_mock,
        book_input=book_input_mock,
        deadline_input=deadline_input_mock,
    )

    command.execute()

    assert app_mock.user is None
    assert app_mock.root.current == "create_goal"

    args, _ = notification_observer.notify.call_args
    assert args[0] == "failure"

    assert goal_repository_mock.create.called_with(
        name="Minha meta",
        host="user123",
        public=0,
        book="Livro",
        deadline="2023-12-21",
    )
