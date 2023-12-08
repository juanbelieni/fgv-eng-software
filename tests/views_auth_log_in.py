from unittest.mock import Mock
from views.auth.log_in import LogInCommand
from models.user import User


def test_log_in_command_success():
    user_repository_mock = Mock()
    user_repository_mock.create.return_value = User(
        "123", "Joãozinho", "joao@fgv.br", ""
    )

    email_input_mock = Mock()
    password_input_mock = Mock()

    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"

    command = LogInCommand(
        user_repository=user_repository_mock,
        email_input=email_input_mock,
        password_input=password_input_mock,
    )

    command.execute()

    assert user_repository_mock.read.called_with(
        email="joao@fgv.br",
        password="password",
    )
