import pytest
from unittest.mock import Mock
from src.models.user import UserRepository
from src.utils.db import DB


@pytest.fixture
def user_repository():
    mock_db = Mock(spec=DB)
    test_user_repository = UserRepository(mock_db)
    yield test_user_repository


def test_create_user(user_repository):
    mock_result = [("user_id", "test_user", "test_user@example.com", "")]
    user_repository.db.execute.return_value = mock_result

    user_data = {
        "username": "test_user",
        "email": "test_user@example.com",
        "password": "password123",
    }

    new_user = user_repository.create(**user_data)

    assert new_user is not None
    assert user_repository.db.execute.called
