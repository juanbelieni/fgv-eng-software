

import pytest
from unittest.mock import Mock
from models.user import User, UserRepository


@pytest.fixture
def user_repository():
    mock_db = Mock()
    test_user_repository = UserRepository(mock_db)
    yield test_user_repository


def test_create_user_succes(user_repository):
    mock_result = [("123", "test_user", "test_user@example.com", "")]
    user_repository.db.execute.return_value = mock_result

    user_data = {
        "username": "test_user",
        "email": "test_user@example.com",
        "password": "password123",
    }

    new_user = user_repository.create(**user_data)

    assert new_user is not None
    assert user_repository.db.execute.called_once


def test_create_user_failure(user_repository):
    user_repository.db.execute.return_value = None

    user_data = {
        "username": "",
        "email": "test_user@example.com",
        "password": "password123",
    }

    new_user = user_repository.create(**user_data)

    assert new_user is None
    assert user_repository.db.execute.called_once


def test_read_user_with_id(user_repository):
    mock_result = [("123", "test_user", "test_user@example.com", "")]
    user_repository.db.execute.return_value = mock_result

    user = user_repository.read(id="123")
    args, _ = user_repository.db.execute.call_args

    assert user is not None
    assert user_repository.db.execute.called_once
    assert "id = ?" in args[0]
    assert args[1] == ("123",)


def test_read_user_with_password(user_repository):
    mock_result = [("123", "test_user", "test_user@example.com", "")]
    user_repository.db.execute.return_value = mock_result

    user = user_repository.read(password="password")
    args, _ = user_repository.db.execute.call_args

    assert user is not None
    assert user_repository.db.execute.called_once
    assert "password = ?" in args[0]
    assert len(args[1][0]) == 64

def test_read_user_failure_with_none(user_repository):
    user_repository.db.execute.return_value = None

    user = user_repository.read(id="123")
    args, _ = user_repository.db.execute.call_args

    assert user is None
    assert user_repository.db.execute.called_once

def test_update_user(user_repository):
    mock_result = [("123", "test_user", "test_user@example.com", "new_bio")]
    user_repository.db.execute.return_value = mock_result

    old_user = User(
        id="123",
        name="test_user",
        email="test_user@example.com",
        bio=""
    )

    new_user = user_repository.update(old_user, bio="new_bio")

    assert new_user is not None
    assert new_user.bio == "new_bio"
    assert user_repository.db.execute.called_once


def test_delete_user(user_repository):
    mock_result = []
    user_repository.db.execute.return_value = mock_result

    user = User(
        id="123",
        name="test_user",
        email="test_user@example.com",
        bio=""
    )

    user_repository.delete(user)
    args, _ = user_repository.db.execute.call_args

    assert user_repository.db.execute.called_once
    assert args[1] == ("123",)
