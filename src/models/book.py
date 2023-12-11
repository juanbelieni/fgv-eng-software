import requests

class Book():
    """
    Book

    Represents a book  with attributes title, authors, id, imageLinks, pageCount and isbn.

    Attributes:
    - title (str): The title of the book.
    - authors (list): The authors of the book.
    - id (str): The unique identifier for the book.
    - imageLinks (str): The link of the image cover of the book.
    - pageCount (str): The number of pages of the book.
    - isbn (str): The International Standard Book Number of the book.
    """
    title: str
    authors: list
    id: str
    imageLinks: str
    pageCount: int
    isbn: int


# 
class BookRepository():
    def __init__(self):
        self.key_api = 'AIzaSyCgdWN2DzIQxQCIddJ8gHBIaEIyx8eDSi8'

    def search(self, query):
        """
        Searches for books in the Google Books API based on the provided query.

        Parameters:
        - query (str): The query string for book search.

        Returns:
        - dict: A dictionary containing book search results.
        """
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": query,
            "key": self.key_api,
        }

        try:
            # Sends an HTTP request to fetch books based on the query
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
        

    def book_info(self, query) -> list[Book]:
        """
        Retrieves book information based on the query and returns a list of Book objects.

        Parameters:
        - query (str): The query string for book information.

        Returns:
        - list[Book]: A list containing Book objects.
        """
        result = self.search(query)
        
        books = []
        
        for item in result.get('items', []):
            book = Book()
            volume_info = item.get('volumeInfo', {})
            
            book.title = volume_info.get('title', 'N/A')
            book.authors = volume_info.get('authors', [])
            book.id = volume_info.get('id', 'N/A')
            book.imageLinks = volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else 'N/A'
            book.pageCount = volume_info.get('pageCount', 'N/A')
            book.isbn = volume_info.get('industryIdentifiers', [{'type': 'ISBN_13', 'identifier': 'N/A'}])[0]['identifier']
            
            books.append(book)
    
        return books
    
    
    def search_by_isbn(self, isbn):
        """
        Searches for a book in the Google Books API based on the provided ISBN.

        Parameters:
        - isbn (str): The ISBN of the book to search for.

        Returns:
        - dict: A dictionary containing book search results by ISBN.
        """
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"isbn:{isbn}",
            "key": self.key_api,
        }
    
        try:
            # Sends an HTTP request to fetch a book by ISBN
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
        
    def book_info_by_isbn(self, isbn) -> Book:
        """
        Retrieves book information based on the ISBN and returns a Book object.

        Parameters:
        - isbn (str): The ISBN of the book to retrieve information for.

        Returns:
        - Book: The Book object if found, otherwise None.
        """
        result = self.search_by_isbn(isbn)
    
        if isinstance(result, dict) and 'items' in result and len(result['items']) > 0:
            book = Book()
            volume_info = result['items'][0]['volumeInfo']
    
            book.title = volume_info.get('title', 'N/A')
            book.authors = volume_info.get('authors', [])
            book.id = volume_info.get('id', 'N/A')
            book.imageLinks = volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else 'N/A'
            book.pageCount = volume_info.get('pageCount', 'N/A')
            book.isbn = volume_info.get('industryIdentifiers', [{'type': 'ISBN_13', 'identifier': 'N/A'}])[0]['identifier']
    
            return book
        else:
            return None
