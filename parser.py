import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com?catalogue/page-{}.html"

async def parse_page(client: httpx.AsyncClient, page_number: int):
    url = BASE_URL.format(page_number)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = await client.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    books_html = soup.find_all('article', class_='product_pod')
    page_data = []

    for book in books_html:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='availability').text.strip()
        link = "https://books.toscrape.com/catalogue/" + book.find('h3').find('a')['href']

        page_data.append((title, price, availability, link))

    return page_data

async def get_all_books(total_pages: int):
    all_books = []
    timeout = httpx.Timeout(20.0, connect=30.0)
    
    async with httpx.AsyncClient(timeout=timeout) as client:
        for page in range(1, total_pages + 1):
            print(f"Парсим страницу {page} из {total_pages}...")
            try:
                page_data = await parse_page(client, page)
                all_books.extend(page_data)
            except httpx.ConnectTimeout:
                print(f"Ошибка: Превышено время ожидания для страницы {page}. Пропускаем...")
                continue
            except Exception as e:
                print(f"Непредвиденная ошибка на странице {page}: {e}")
                continue
            
    return all_books
