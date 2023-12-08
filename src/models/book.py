import requests
from src.utils.repository import Repository

class Book():
    title: str
    authors: list
    id: str
    imageLinks: str
    pageCount: int

class BookRepository(Repository):

    def __sersh(query, 
                chave_api = 'AIzaSyCgdWN2DzIQxQCIddJ8gHBIaEIyx8eDSi8'):
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": query,
            "key": chave_api,
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err
        
    def book_info(query) -> Book:
        book = Book()
        result = BookRepository.__sersh(query)

        book.title = result['items'][0]['volumeInfo']['title']
        book.authors = result['items'][0]['volumeInfo']['authors']
        book.id = result['items'][0]['id']
        book.imageLinks = result['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        book.pageCount = result['items'][0]['volumeInfo']['pageCount']
        
        return book

