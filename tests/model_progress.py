import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from src.models.progress import Progress, ProgressRepository
from src.utils.db import DB


@pytest.fixture
def progress_repository():
    mock_db = MagicMock()
    test_progress_repository = ProgressRepository(mock_db)
    yield test_progress_repository


def test_create_progress(progress_repository):
    mock_result = [("123", "123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress_data = {
        "id": "123",
        "user": "123",
        "book": "123",
        "percent": 1,
    }

    new_progress = progress_repository.create(**progress_data)

    assert new_progress is not None
    assert progress_repository.db.execute.called_once


def test_create_progress_failure(progress_repository):
    progress_data = {
        "id": "",
        "user": "845",
        "book": "",
        "percent": "ssdd"
    }

    progress_repository.db.execute.return_value = None

    created_progress = progress_repository.create(**progress_data)

    assert created_progress is None
    assert progress_repository.db.execute.called_once


def test_read_progress(progress_repository):
    mock_result = [("123", "123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress = progress_repository.read(id="123")
    args, _ = progress_repository.db.execute.call_args

    assert progress is not None
    assert progress_repository.db.execute.called_once
    assert args[1] == ("123", )


def test_read_progress_failure(progress_repository):
    progress_repository.db.execute.return_value = None

    progress = progress_repository.read(id="123")

    assert progress is None
    assert progress_repository.db.execute.called_once


def test_list_progress(progress_repository):
    mock_result = [("123", "123", "123", 1), ("256", "123", "258", 1)]
    progress_repository.db.execute.return_value = mock_result

    progresses = progress_repository.list(user="123")
    list_progresses = list(progresses)
    args, _ = progress_repository.db.execute.call_args

    assert progresses is not None
    assert len(list_progresses) == 2
    assert args[1] == ("123", )
    assert progress_repository.db.execute.called_once


def test_list_progress_failure(progress_repository):
    progress_repository.db.execute.return_value = None

    progresses = progress_repository.list()

    assert progresses is None
    assert progress_repository.db.execute.called_once


def test_update_progress(progress_repository):
    mock_result = [("123", "123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    new_progress = progress_repository.update(id="123", percent=1)

    assert new_progress is not None
    assert new_progress.percent == 1
    assert progress_repository.db.execute.called_once


def test_update_progress_failure(progress_repository):

    progress_repository.db.execute.return_value = None

    updated_progress = progress_repository.update(id="123", percent=0.5)

    assert updated_progress is None
    assert progress_repository.db.execute.called_once


def test_delete_progress(progress_repository):
    mock_result = [("123" "123", "123", 1)]
    progress_repository.db.execute.return_value = mock_result

    progress_repository.delete(id="123")
    args, _ = progress_repository.db.execute.call_args

    assert args[1] == ("123",)
    assert progress_repository.db.execute.called_once
