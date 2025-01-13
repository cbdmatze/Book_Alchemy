import requests

def fetch_book_cover(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and 'volumeInfo' in data['items'][0]:
            return data['items'][0]['volumeInfo'].get('imageLinks', {}).get('thumbnail', None)
    return '/static/images/default_cover.jpg'  # Fallback to a default image if no cover found
