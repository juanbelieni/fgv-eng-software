from unittest.mock import Mock, MagicMock
from views.auth.log_in import LogInCommand
from models.user import User


def test_log_in_command_success():
    app_mock = MagicMock()
    app_mock.root.current = "log_in"

    user_repository_mock = Mock()
    user_repository_mock.read.return_value = User(
        "123", "Joãozinho", "joao@fgv.br", ""
    )

    email_input_mock = Mock()
    password_input_mock = Mock()

    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"

    command = LogInCommand(
        app=app_mock,
        user_repository=user_repository_mock,
        email_input=email_input_mock,
        password_input=password_input_mock,
    )

    command.execute()

    assert user_repository_mock.read.called_with(
        email="joao@fgv.br",
        password="password",
    )

    assert type(app_mock.user) == User
    assert app_mock.root.current == "profile"


def test_log_in_command_failure():
    app_mock = MagicMock()
    app_mock.user = None
    app_mock.root.current = "log_in"

    user_repository_mock = Mock()
    user_repository_mock.read.return_value = None

    email_input_mock = Mock()
    password_input_mock = Mock()

    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"

    command = LogInCommand(
        app=app_mock,
        user_repository=user_repository_mock,
        email_input=email_input_mock,
        password_input=password_input_mock,
    )

    command.execute()

    assert user_repository_mock.read.called_with(
        email="joao@fgv.br",
        password="password",
    )

    assert app_mock.user is None
    assert app_mock.root.current == "log_in"
