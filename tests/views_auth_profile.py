
from unittest.mock import Mock, MagicMock
from views.auth.profile import UpdateProfileCommand
from models.user import User


def test_update_profile_command_success():
    app_mock = MagicMock()
    app_mock.root.current = "log_in"
    app_mock.user = User(
        "123", "Joãozinho", "joao@fgv.br", ""
    )

    user_repository_mock = Mock()
    user_repository_mock.update.return_value = User(
        "123", "Joãozinho", "joao@fgv.br", "Bio"
    )

    name_input_mock = Mock()
    bio_input_mock = Mock()

    bio_input_mock.text = "Bio"

    command = UpdateProfileCommand(
        app=app_mock,
        user_repository=user_repository_mock,
        name_input=name_input_mock,
        bio_input=bio_input_mock,
    )

    command.execute()

    assert user_repository_mock.update.called_with(
        user=app_mock.user,
        bio="Bio",
    )

    assert app_mock.user.bio == "Bio"
