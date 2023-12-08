import pytest
from unittest.mock import Mock
from src.models.progress import Progress, ProgressRepository
from src.utils.db import DB


@pytest.fixture
def progress_repository():
    mock_db = Mock(spec=DB)
    test_progress_repository = ProgressRepository(mock_db)
    yield test_progress_repository


def test_create_progress(progress_repository):
    mock_result = [("123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress_data = {
        "user": "123",
        "goal": "123",
        "percent": 1,
    }

    new_progress = progress_repository.create(**progress_data)

    assert new_progress is not None
    assert progress_repository.db.execute.called_once


def test_create_progress_failure(progress_repository):
    progress_data = {
        "user": "845",
        "goal": "",
        "percent": 0.8,
    }

    progress_repository.db.execute.return_value = None

    created_progress = progress_repository.create(**progress_data)

    assert created_progress is None
    assert progress_repository.db.execute.called_once 


def test_read_progress_with_user_and_goal(progress_repository):
    mock_result = [("123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress = progress_repository.read(user="123", goal="123")
    args, _ = progress_repository.db.execute.call_args

    assert progress is not None
    assert progress_repository.db.execute.called_once
    assert args[1] == ("123", "123")


def test_read_progress_with_user_and_no_goal(progress_repository):
    progress_repository.db.execute.return_value = None

    progress = progress_repository.read(user="123")

    assert progress is None
    assert progress_repository.db.execute.called_once


def test_read_progress_with_user_and_goal_absents_in_database(progress_repository):
    progress_repository.db.execute.return_value = None

    progress = progress_repository.read(user="123", goal="123")

    assert progress is None
    assert progress_repository.db.execute.called_once


def test_read_progress_with_goal_and_no_user(progress_repository):
    progress_repository.db.execute.return_value = None

    progress = progress_repository.read(goal="123")

    assert progress is None
    assert progress_repository.db.execute.called_once


def test_update_progress(progress_repository):
    mock_result = [("123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress_data = {
        "user": "123",
        "goal": "123",
        "percent": 1,
    }

    new_progress = progress_repository.update(**progress_data)

    assert new_progress is not None
    assert new_progress.percent == 1
    assert progress_repository.db.execute.called_once


def test_update_progress_failure(progress_repository):
    progress_data = {
        "user": "845",
        "goal": "599",
        "percent": "ssdd",
    }

    progress_repository.db.execute.return_value = None

    updated_progress = progress_repository.update(**progress_data)

    assert updated_progress is None
    assert progress_repository.db.execute.called_once


def test_delete_progress(progress_repository):
    mock_result = [("123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress = Progress(
        user = "123",
        goal = "123",
        percent = 1,
    )

    progress_repository.delete(progress)
    args, _ = progress_repository.db.execute.call_args

    assert args[1] == ("123", "123")
    assert progress_repository.db.execute.called_once
