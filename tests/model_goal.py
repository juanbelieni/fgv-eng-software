import pytest
from unittest.mock import Mock
from src.models.goal import Goal, GoalRepository
from src.utils.db import DB


@pytest.fixture
def goal_repository():
    mock_db = Mock(spec=DB)
    test_goal_repository = GoalRepository(mock_db)
    yield test_goal_repository

'''
def test_create_goal(goal_repository):
    mock_result = [("123", "test_name_goal", 1, "test_name_book")]
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
'''

def test_create_goal(goal_repository):
    mock_result = [(
        "123", "test_name_goal",
        "user123", 1, 0, "test_name_book",
        )]
    goal_repository.db.execute.return_value = mock_result

    goal_data = {
        "name": "test_name_goal",
        "host": "user123",
        "public": 1,
        "hidden": 0,
        "book": "test_name_book",
    }

    new_goal = goal_repository.create(**goal_data)

    assert new_goal is not None
    assert goal_repository.db.execute.called_once

'''
def test_create_goal_failure(goal_repository):
    goal_data = {
        "name": "Test Goal",
        "public": 1,
        "book": "",
        "password": "password123"
    }

    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is None
    assert goal_repository.db.execute.called_once
'''

'''
def test_create_goal_failure(goal_repository):
    goal_data = {
        "name": "Test Goal",
        "host": "user123",
        "public": 1,
        "hidden": 0,
        "book": "",
    }

    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is None
    assert goal_repository.db.execute.called_once
'''

def test_create_goal_no_book(goal_repository):
    goal_data = {
        "name": "Test Goal",
        "host": "user123",
        "public": 1,
        "hidden": 0,
        "book": None,
    }

    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is None
    assert goal_repository.db.execute.called_once

def test_create_goal_empty_str_book(goal_repository):
    goal_data = {
        "name": "Test Goal",
        "host": "user123",
        "public": 1,
        "hidden": 0,
        "book": "",
    }

    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is None
    assert goal_repository.db.execute.called_once

def test_create_goal_no_name(goal_repository):
    goal_data = {
        "name": None,
        "host": "user123",
        "public": 0,
        "hidden": 0,
        "book": "livrinho",
    }

    default_name = "Minha meta de leitura para livrinho"

    mock_result = [("123", default_name, "user123", 0, 0, "my_book")]

    goal_repository.db.execute.return_value = mock_result

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is not None
    assert created_goal.name == default_name
    assert goal_repository.db.execute.called_once
