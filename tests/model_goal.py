import pytest
from unittest.mock import Mock
from src.models.goal import Goal, GoalRepository
from src.models.user import User
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

'''
def test_create_goal(goal_repository):
    mock_result = [(
        "123", "test_name_goal",
        "user123", 1, 0, "test_name_book",
        "2023-12-31",
        )]
    goal_repository.db.execute.return_value = mock_result

    goal_data = {
        "name": "test_name_goal",
        "host": "user123",
        "public": 1,
        "hidden": 0,
        "book": "test_name_book",
        "deadline": "2023-12-31",
    }

    new_goal = goal_repository.create(**goal_data)

    assert new_goal is not None
    assert goal_repository.db.execute.called_once
'''


def test_create_goal(goal_repository):
    mock_result = [(
        "123", "test_name_goal",
        "user123", 1, 0, "test_name_book",
        "2023-12-31",
    )]
    goal_repository.db.execute.return_value = mock_result

    goal_data = {
        "name": "test_name_goal",
        "host": "user123",
        "public": 1,
        "book": "test_name_book",
        "deadline": "2023-12-31",
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
        "deadline": "2023-12-31",
    }

    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is None
    assert goal_repository.db.execute.called_once
'''


def test_create_goal_failure(goal_repository):
    goal_data = {
        "name": "Test Goal",
        "host": "user123",
        "public": 1,
        "book": "",
        "deadline": "2023-12-31",
    }

    goal_repository.db.execute.return_value = None

    created_goal = goal_repository.create(**goal_data)

    assert created_goal is None
    assert goal_repository.db.execute.called_once


'''
def test_create_goal_no_name(goal_repository):
    goal_data = {
        "name": None,
        "host": "user123",
        "public": 1,
        "hidden": 0,
        "book": "livro",
        "deadline": "2023-12-31",
    }

    mock_result = [
        [(
        "Meta de leitura para livro", 
        "test_name_goal", "user123", 1, 0,
        "livro", "2023-12-31",
        )],
        [("user123", "123")],
    ]

    goal_repository.db.execute.side_effect = mock_result
    
    created_goal = goal_repository.create(**goal_data)
    args, _ = goal_repository.db.execute.call_args_list[0]

    assert created_goal is not None
    assert args[1][1] == "Meta de leitura para livro"
    assert goal_repository.db.execute.called_once
'''


def test_create_goal_no_name(goal_repository):
    goal_data = {
        "name": None,
        "host": "user123",
        "public": 1,
        "book": "livro",
        "deadline": "2023-12-31",
    }

    mock_result = [
        [(
            "123", "Meta de leitura para livro",
            "user123", 1, 0,
            "livro", "2023-12-31",
        )],
        [(
            "123", "Meta de leitura para livro",
            "user123", 1, 0,
            "livro", "2023-12-31",
        )],
        [("user123", "123")],
    ]

    goal_repository.db.execute.side_effect = mock_result

    created_goal = goal_repository.create(**goal_data)
    args, _ = goal_repository.db.execute.call_args_list[0]

    assert created_goal is not None
    assert args[1][1] == "Meta de leitura para livro"
    assert goal_repository.db.execute.called_once


def test_read_goal_id(goal_repository):
    mock_result = [(
        "123", "meta", "user123",
        1, 0, "livro", "2024-01-01",
    )]
    goal_repository.db.execute.return_value = mock_result

    goal = goal_repository.read(id="123")
    args, _ = goal_repository.db.execute.call_args

    assert goal is not None
    assert goal_repository.db.execute.called_once
    assert "id = ?" in args[0]
    assert args[1] == ("123",)


def test_read_goal_without_id(goal_repository):
    mock_result = [
        (
            "123", "goal name", "joao123",
            1, 0, "livro", "2024-01-01"
        ),
        (
            "345", "goal name", "maria345",
            1, 0, "outro livro", "2023-12-31",
        )
    ]
    goal_repository.db.execute.return_value = mock_result

    goals = goal_repository.read(name="goal name")
    args, _ = goal_repository.db.execute.call_args

    assert goals is not None
    assert goal_repository.db.execute.called_once
    assert "name = ?" in args[0]
    assert args[1] == ("goal name",)


def test_read_goal_failure(goal_repository):
    goal_repository.db.execute.return_value = None
    goal = goal_repository.read(id="123")

    assert goal is None
    assert goal_repository.db.execute.called_once


def test_update_one_success(goal_repository):
    goal_repository.db.execute.side_effect = [
        [],
        [("123", "Minha meta", "user123", 0, 1, "O Livro", "2023-12-31")]
    ]

    old_goal = Goal(
        id="123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=0,
        book="O Livro",
        deadline="2023-12-31"
    )

    new_goal = goal_repository.update(old_goal, name="Minha meta")

    args, _ = goal_repository.db.execute.call_args_list[0]

    assert new_goal is not None
    assert new_goal.name == "Minha meta"
    assert args[1][0] == "Minha meta"
    assert goal_repository.db.execute.called_once


def test_update_many_success(goal_repository):
    goal_repository.db.execute.side_effect = [
        [],
        [("123", "Minha meta", "user123", 0, 0, "O Livro", "2024-06-31")]
    ]

    old_goal = Goal(
        id="123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=0,
        book="O Livro",
        deadline="2023-12-31"
    )

    new_goal = goal_repository.update(
        old_goal,
        name="Minha meta",
        deadline="2024-06-31"
    )

    args, _ = goal_repository.db.execute.call_args_list[0]

    assert new_goal is not None
    assert new_goal.name == "Minha meta"
    assert new_goal.deadline == "2024-06-31"
    assert args[1][0] == "Minha meta"
    assert args[1][1] == "2024-06-31"
    assert goal_repository.db.execute.called_once


def test_update_failure(goal_repository):
    # It is not possible to change the book of an existing goal.
    goal_repository.db.execute.return_value = None

    old_goal = Goal(
        id="123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=0,
        book="O Livro",
        deadline="2023-12-31"
    )

    new_goal = goal_repository.update(
        old_goal,
        book="Novo livro"
    )

    assert new_goal is None
    assert goal_repository.db.execute.called_once


def test_change_visibility_hide(goal_repository):
    goal_repository.db.execute.side_effect = [
        [],
        [("123", "Minha meta", "user123", 0, 1, "O Livro", "2024-06-31")]
    ]

    old_goal = Goal(
        id="123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=0,
        book="O Livro",
        deadline="2023-12-31"
    )

    new_goal = goal_repository.change_visibility(old_goal)

    args, _ = goal_repository.db.execute.call_args_list[0]

    assert new_goal is not None
    assert args[1][0] == 1
    assert goal_repository.db.execute.called_once


def test_change_visibility_unhide(goal_repository):
    goal_repository.db.execute.side_effect = [
        [],
        [("123", "Minha meta", "user123", 0, 0, "O Livro", "2024-06-31")]
    ]

    old_goal = Goal(
        id="123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=1,
        book="O Livro",
        deadline="2023-12-31"
    )

    new_goal = goal_repository.change_visibility(old_goal)

    args, _ = goal_repository.db.execute.call_args_list[0]

    assert new_goal is not None
    assert args[1][0] == 0
    assert goal_repository.db.execute.called_once


def test_delete_success(goal_repository):
    goal_repository.db.execute.return_value = []

    goal = Goal(
        id="123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=1,
        book="O Livro",
        deadline="2023-12-31"
    )

    goal_repository.delete(goal)
    args, _ = goal_repository.db.execute.call_args

    assert goal_repository.db.execute.called_once
    assert args[1] == ("123",)


def test_add_goal_member(goal_repository):
    goal_repository.db.execute.return_value = [("goal123", "user456")]

    goal = Goal(
        id="goal123",
        name="Meta de leitura para O Livro",
        host="user123",
        public=0,
        hidden=1,
        book="O Livro",
        deadline="2023-12-31"
    )

    new_member = User(
        id="user456",
        name="second_user",
        email="second_user@example.com",
        bio=""
    )

    result = goal_repository.add_member(goal, new_member)
    args, _ = goal_repository.db.execute.call_args

    assert result is not None
    assert args[1][0] == "user456"
    assert args[1][1] == "goal123"
    assert goal_repository.db.execute.called_once
