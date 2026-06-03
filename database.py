import aiosqlite 

DB_NAME = "books.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                price TEXT,
                availability TEXT,
                link TEXT
            )
        """)
        await db.commit()

async def save_books(books_list):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.executemany(
            "INSERT INTO books (title, price, availability, link) VALUES (?, ?, ?, ?)", books_list
        )
        await db.commit()
