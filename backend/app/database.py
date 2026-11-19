"""Database connection helpers for the QuickCommerce application."""

import sqlite3
from pathlib import Path

# Store the database inside the backend folder.
BACKEND_FOLDER = Path(__file__).resolve().parents[1]
DATABASE_PATH = BACKEND_FOLDER / "quickcommerce.db"


def get_connection():
    """Create and return a SQLite connection with dictionary-like rows."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
