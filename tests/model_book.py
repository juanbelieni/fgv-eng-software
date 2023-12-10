import pytest
from unittest.mock import MagicMock
from models.book import Book, BookRepository

@pytest.fixture
def book_repository():
    mock_success_response = {
        "items": [
            {
                "volumeInfo": {
                    "title": "Mock Title",
                    "authors": ["Author 1", "Author 2"],
                    "id": "123",
                    "imageLinks": {"thumbnail": "image_link"},
                    "pageCount": 200,
                    "industryIdentifiers": [{"type": "ISBN_13", "identifier": "123456789"}]
                }
            }
        ]
    }

    mock_search_success = MagicMock()
    mock_search_success.json.return_value = mock_success_response

    mock_requests = MagicMock()
    mock_requests.get.return_value = mock_search_success

    mock_repository = BookRepository()
    mock_repository.search = mock_requests.get

    return mock_repository


def test_book_info_success(book_repository, monkeypatch):
    monkeypatch.setattr(book_repository, "search", MagicMock(return_value={
        "items": [
            {
                "volumeInfo": {
                    "title": "Mock Title",
                    "authors": ["Author 1", "Author 2"],
                    "id": "123",
                    "imageLinks": {"thumbnail": "image_link"},
                    "pageCount": 200,
                    "industryIdentifiers": [{"type": "ISBN_13", "identifier": "123456789"}]
                }
            }
        ]
    }))

    books = book_repository.book_info("Python")

    assert len(books) >= 1
    assert isinstance(books[0], Book)
    assert books[0].title == "Mock Title"
    assert books[0].authors == ["Author 1", "Author 2"]
    assert books[0].id == "123"
    assert books[0].imageLinks == "image_link"
    assert books[0].pageCount == 200
    assert books[0].isbn == "123456789"


def test_book_info_failure(book_repository, monkeypatch):
    monkeypatch.setattr(book_repository, "search", MagicMock(return_value={}))
    books = book_repository.book_info(123)
    
    assert len(books) == 0


def test_book_info_by_isbn_success(book_repository, monkeypatch):
    monkeypatch.setattr(book_repository, "search_by_isbn", MagicMock(return_value={
        "items": [
            {
                "volumeInfo": {
                    "title": "Mock Title",
                    "authors": ["Author 1", "Author 2"],
                    "id": "123",
                    "imageLinks": {"thumbnail": "image_link"},
                    "pageCount": 200,
                    "industryIdentifiers": [{"type": "ISBN_13", "identifier": "123456789"}]
                }
            }
        ]
    }))
    
    book = book_repository.book_info_by_isbn("123456789")

    assert book is not None
    assert isinstance(book, Book)
    assert book.title == "Mock Title"
    assert book.authors == ["Author 1", "Author 2"]
    assert book.id == "123"
    assert book.imageLinks == "image_link"
    assert book.pageCount == 200
    assert book.isbn == "123456789"


def test_book_info_by_isbn_failure(book_repository, monkeypatch):
    monkeypatch.setattr(book_repository, "search_by_isbn", MagicMock(return_value={}))
    book = book_repository.book_info_by_isbn("Invalid ISBN")
    
    assert book is None