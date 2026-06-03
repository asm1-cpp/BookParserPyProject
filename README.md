````markdown
# 📚 Async Book Catalog Scraper

A high-performance asynchronous web scraping solution built with Python, designed to collect product data from **books.toscrape.com**, store it safely in a local database, and generate business-ready Excel reports.

This project demonstrates modern scraping architecture using asynchronous networking, local database caching, and automated reporting. It is designed with real-world freelance and client projects in mind, where speed, reliability, and data delivery are critical.

---

## 🚀 Overview

The **Async Book Catalog Scraper** automatically:

- Fetches book data asynchronously from the target website
- Extracts product information from HTML pages
- Stores collected records in SQLite for reliability
- Prevents data loss through database persistence
- Generates a clean Excel report for end users

The final output is an Excel spreadsheet that can be delivered directly to clients, analysts, or business teams without requiring technical knowledge.

---

## ✨ Key Features

### ⚡ Asynchronous Performance

Built with **HTTPX Async Client**, allowing multiple requests to run concurrently and significantly reducing scraping time compared to traditional synchronous approaches.

### 🛡️ Fail-Safe Data Storage

All scraped data is stored in a local **SQLite database** using **AioSQLite** before export.

Benefits:

- Prevents data loss during unexpected interruptions
- Allows recovery and re-exporting without re-scraping
- Provides a persistent storage layer for future processing

### 📊 Business-Ready Excel Reports

Using **Pandas** and **OpenPyXL**, the scraper automatically exports collected data into a professional Excel spreadsheet.

Perfect for:

- Market research
- Competitor analysis
- Product monitoring
- Client reporting
- Data collection projects

### 🔄 Efficient Batch Database Operations

Records are inserted using SQLite's `executemany()` functionality, minimizing database overhead and improving performance when handling larger datasets.

### 🧩 Modular Architecture

The codebase is separated into dedicated components, making it easy to maintain, extend, and adapt for future scraping projects.

---

## 🏗️ Architecture & Tech Stack

### Core Technologies

| Technology | Purpose |
|------------|----------|
| Python 3.10+ | Main programming language |
| HTTPX | Asynchronous HTTP requests |
| BeautifulSoup4 | HTML parsing and data extraction |
| AioSQLite | Asynchronous SQLite operations |
| SQLite | Local persistent storage |
| Pandas | Data transformation and export |
| OpenPyXL | Excel file generation |

---

## 📂 Repository Structure

```text
Async-Book-Catalog-Scraper/
│
├── main.py            # Entry point
├── parser.py          # Async scraping logic
├── database.py        # SQLite operations
│
├── books.db           # Local database
├── books.xlsx         # Generated Excel report
│
├── requirements.txt   # Project dependencies
└── README.md
````

### File Responsibilities

#### `main.py`

Application entry point.

Responsibilities:

* Initialize database
* Launch scraper
* Export results to Excel

#### `parser.py`

Contains all scraping logic.

Extracts:

* Book title
* Price
* Availability status
* Product URL

#### `database.py`

Database abstraction layer.

Responsibilities:

* SQLite connection management
* Table creation
* Batch insertion using `executemany()`

#### `books.db`

Persistent local storage for scraped records.

#### `books.xlsx`

Final deliverable report generated for clients and business users.

---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/async-book-catalog-scraper.git
cd async-book-catalog-scraper
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment (Linux/macOS)

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Scraper

```bash
python main.py
```

---

## 📈 Example Workflow

```text
books.toscrape.com
          │
          ▼
Async HTTP Requests
          │
          ▼
BeautifulSoup Parsing
          │
          ▼
SQLite Database Cache
          │
          ▼
Pandas Processing
          │
          ▼
Excel Report (.xlsx)
```

---

## 💼 Why This Architecture Works for Clients

### Faster Delivery

Asynchronous requests dramatically reduce execution time, making the scraper suitable for larger datasets and recurring jobs.

### Reliable Data Collection

Database caching ensures collected data is preserved even if the process stops unexpectedly.

### Easy-to-Use Output

Excel reports can be opened immediately by managers, analysts, and non-technical stakeholders.

### Scalable Foundation

The modular design allows rapid adaptation to new websites and business requirements.

---

## 🔮 Future Enhancements

Potential production-grade improvements include:

### 🌐 Proxy Rotation

* Reduce request blocking
* Improve scraping stability
* Enable larger-scale data collection

### 🤖 Telegram Notifications

* Notify clients when scraping is complete
* Send report summaries automatically
* Real-time monitoring of scraping jobs

### 🐳 Docker Support

* Simplified deployment
* Environment consistency
* Production-ready containerization

### ☁️ Scheduled Cloud Execution

* Automated daily scraping
* VPS deployment
* CI/CD integration

---

## 📄 License

This project is provided for educational and portfolio purposes.

---

## 👨‍💻 Author

Developed as a demonstration of:

* Asynchronous Python programming
* Web scraping architecture
* Database-backed data pipelines
* Automated business reporting

A practical example of how modern Python tooling can be combined to build reliable, client-ready data collection solutions.

```
```
