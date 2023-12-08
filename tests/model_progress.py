import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from src.models.progress import ProgressRepository
from src.utils.db import DB

@pytest.fixture
def db_mock():
    return MagicMock()

@pytest.fixture
def progress_repository(db_mock):
    return ProgressRepository(db_mock)

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
        "page": 1,
    }

    new_progress = progress_repository.create(**progress_data)

    assert new_progress is not None
    assert progress_repository.db.execute.called_once

def test_create_progress_failure(progress_repository):
    progress_data = {
        "user": "845",
        "goal": "599",
        "page": "ssdd",
    }

    progress_repository.db.execute.return_value = None
    created_progress = progress_repository.create(**progress_data)

    assert created_progress is None
    assert progress_repository.db.execute.called_once
