﻿# 🔍 DuckDuckGo Search API and Craw4Ai Crawling.

This is a lightweight FastAPI server that provides two endpoints to perform web and image searches using the DuckDuckGo engine via the `duckduckgo-search` Python package.

---

## 🚀 Requirements

- Python 3.7+
- pip

---

## 📦 Installation

1. Clone this repository or copy the files:

2. Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. run setup of craw4ai:

```bash
crawl4ai-setup
```

## ▶️ How to Run

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at: <http://localhost:8000>

## 🌐 API Endpoints

### 🔎 GET /buscar

Performs a web text search.

**Query Parameters:**

- `term` (string): The search keyword.

**Example:**

```bash
GET http://localhost:8000/buscar?termo=fastapi
```

**Response:**

```json
{
  "results": [
    {
      "title": "Example Title",
      "href": "https://example.com",
      "body": "A short description of the result..."
    },
    ...
  ]
}
```

### 🖼️ GET /buscar_imagens

Performs an image search related to a keyword.

**Query Parameters:**

- `term` (string): The search keyword.

**Example:**

```bash
GET http://localhost:8000/buscar_imagens?termo=cats
```

**Response:**

```json
{
  "images": [
    {
      "title": "Cat Picture",
      "image": "https://example.com/image.jpg",
      "thumbnail": "https://example.com/thumb.jpg",
      "source": "https://source-website.com"
    },
    ...
  ]
}
```

## ℹ️ Notes

This project uses duckduckgo-search which is a Python package to access DuckDuckGo search results.

No API keys or authentication required.
