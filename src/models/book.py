from src.utils.repository import Repository
import requests

class Book():
    title: str
    authors: list
    id: str
    imageLinks: str
    pageCount: int
    isbn: int


class BookRepository(Repository):

    def search(query, 
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
        

    def book_info(query) -> [Book]:
        result = BookRepository.search(query)
        
        books = []
    
        for item in result.get('items', []):
            book = Book()
            volume_info = item.get('volumeInfo', {})
            
            book.title = volume_info.get('title', 'N/A')
            book.authors = volume_info.get('authors', [])
            book.id = item.get('id', 'N/A')
            book.imageLinks = volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else 'N/A'
            book.pageCount = volume_info.get('pageCount', 'N/A')
            book.isbn = volume_info.get('industryIdentifiers', [{'type': 'ISBN_13', 'identifier': 'N/A'}])[0]['identifier']
            
            books.append(book)
    
        return books
    
    
    
    def search_by_isbn(isbn,
                       chave_api='AIzaSyCgdWN2DzIQxQCIddJ8gHBIaEIyx8eDSi8'):
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"isbn:{isbn}",
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
        
    def book_info_by_isbn(isbn) -> Book:
        result = BookRepository.search_by_isbn(isbn)
    
        if isinstance(result, dict) and 'items' in result and len(result['items']) > 0:
            book = Book()
            volume_info = result['items'][0]['volumeInfo']
    
            book.title = volume_info.get('title', 'N/A')
            book.authors = volume_info.get('authors', [])
            book.id = result['items'][0]['id']
            book.imageLinks = volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else 'N/A'
            book.pageCount = volume_info.get('pageCount', 'N/A')
            book.isbn = volume_info.get('industryIdentifiers', [{'type': 'ISBN_13', 'identifier': 'N/A'}])[0]['identifier']
    
            return book
        else:
            return None