from unittest.mock import Mock, MagicMock
from views.auth.create_progress import CreateProgressesCommand, BoxCreateProgress
from models.progress import ProgressRepository, Progress


def test_create_progress_command():
    app_mock = MagicMock()
    app_mock.user = None
    app_mock.root.current = "create_progress"

    notification_observer = MagicMock()

    user_repository_mock = Mock()
    user_repository_mock.read.return_value = None

    email_input_mock = Mock()
    password_input_mock = Mock()

    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"

    command = LogInCommand(
        app=app_mock,
        user_repository=user_repository_mock,
        notification_observer=notification_observer,
        email_input=email_input_mock,
        password_input=password_input_mock,
    )

    command.execute()

    assert app_mock.user is None
    assert app_mock.root.current == "log_in"

    args, _ = notification_observer.notify.call_args
    assert args[0] == "failure"

    assert user_repository_mock.read.called_with(
        email="joao@fgv.br",
        password="password",
    )
