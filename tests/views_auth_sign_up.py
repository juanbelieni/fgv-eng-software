from unittest.mock import Mock
from views.auth.sign_up import SignUpCommand


def test_sign_up_command():
    user_repository_mock = Mock()
    name_input_mock = Mock()
    email_input_mock = Mock()
    password_input_mock = Mock()
    bio_input_mock = Mock()

    name_input_mock.text = "Joãozinho"
    email_input_mock.text = "joao@fgv.br"
    password_input_mock.text = "password"
    bio_input_mock.text = ""

    command = SignUpCommand(
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
