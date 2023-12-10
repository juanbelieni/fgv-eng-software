from unittest.mock import Mock, MagicMock
from views.auth.sign_up import SignUpCommand
from models.user import User


def test_sign_up_command_success():
    app_mock = MagicMock()
    app_mock.root.current = "sign_up"

    user_repository_mock = Mock()
    user_repository_mock.create.return_value = User(
        "123", "Joãozinho", "joao@fgv.br", ""
    )

    name_input_mock = Mock()
    email_input_mock = Mock()
    password_input_mock = Mock()
    bio_input_mock = Mock()

    name_input_mock.text = "Joãozinho"
    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"
    bio_input_mock.text = ""

    command = SignUpCommand(
        app=app_mock,
        user_repository=user_repository_mock,
        name_input=name_input_mock,
        email_input=email_input_mock,
        password_input=password_input_mock,
        bio_input=bio_input_mock,
    )

    command.execute()

    assert user_repository_mock.create.called_with(
        name="Joãozinho",
        email="joao@fgv.br",
        password="password",
        bio="",
    )

    assert command.app.root.current == 'log_in'


def test_sign_up_command_failure():
    app_mock = MagicMock()
    app_mock.root.current = "sign_up"

    notification_observer = MagicMock()

    user_repository_mock = Mock()
    user_repository_mock.create.return_value = None

    name_input_mock = Mock()
    email_input_mock = Mock()
    password_input_mock = Mock()
    bio_input_mock = Mock()

    name_input_mock.text = "Joãozinho"
    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"
    bio_input_mock.text = ""

    command = SignUpCommand(
        app=app_mock,
        user_repository=user_repository_mock,
        notification_observer=notification_observer,
        name_input=name_input_mock,
        email_input=email_input_mock,
        password_input=password_input_mock,
        bio_input=bio_input_mock,
    )

    command.execute()

    assert command.app.root.current == 'sign_up'

    args, _ = notification_observer.notify.call_args
    assert args[0] == "failure"

    assert user_repository_mock.create.called_with(
        name="Joãozinho",
        email="joao@fgv.br",
        password="password",
        bio="",
    )

