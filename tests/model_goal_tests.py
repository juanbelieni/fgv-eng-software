import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from src.models.goal import Goal, GoalRepository
from src.utils.db import DB

@pytest.fixture
def db_mock():
    return MagicMock()

@pytest.fixture
def goal_repository(db_mock):
    return GoalRepository(db_mock)

@pytest.fixture
def goal_repository():
    mock_db = Mock(spec=DB)
    test_goal_repository = GoalRepository(mock_db)
    yield test_goal_repository

def test_create_goal(goal_repository):
    mock_result = [("123", "test_name_goal", 1, "test_name_book", "password123")]
    goal_repository.db.execute.return_value = mock_result

    goal_data = {
        "name": "test_name_goal",
        "public": 1,
        "book": "test_name_book",
        "password": "password123",
    }

    new_goal = goal_repository.create(**goal_data)

    assert new_goal is not None
    assert goal_repository.db.execute.called_once

def test_create_goal_failure(goal_repository):
    attrs = {
        "name": "Test Goal",
        "public": True,
        "book": "Sample Book",
        "password": "password123"
    }

    # Assuming the db.execute() returns None or an empty list for a failed insertion
    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**attrs)

    assert created_goal is None
    assert goal_repository.db.execute.called_once
    # Add more assertions based on your expected behavior for failure

    # Add more tests for read, update, delete methods as needed