import asyncio
import aiosqlite
import pandas as pd
from database import init_db, save_books
from parser import get_all_books

async def export_to_excel():
    print("Генерируем Excel-отчет...")

    async with aiosqlite.connect("books.db") as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT title, price, availability, link FROM books") as cursor:
            rows = await cursor.fetchall()
            data = [dict(row) for row in rows]

        if not data:
            print("База данных пуста, нечего экспортировать!")
            return

        df = pd.DataFrame(data)

        df.columns = ["Название книги", "Цена", "Доступность", "Ссылка на товар"]

        output_file = "books.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Готово! Данные успешно сохранены в файл: {output_file}")

async def main():
    print("Инициализация базы данных...")
    await init_db()

    total_pages_to_parse = 5
    print(f"Запуск парсера на {total_pages_to_parse} страниц...")

    books_data = await get_all_books(total_pages_to_parse)

    if books_data:
        print(f"Сохраняем {len(books_data)} книг в базу данных...")
        await save_books(books_data)
    else:
        print("Не удалось собрать данные.")
        return

    await export_to_excel()
    print("Программа успешно завершила работу!")

if __name__ == "__main__":
    asyncio.run(main())
