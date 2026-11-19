"""Create database tables and insert sample products/orders."""

from app.database import get_connection


SAMPLE_PRODUCTS = [
    ("Amul Toned Milk 1L", "Dairy", 68, 34, 4.6, "Fresh toned milk", "🥛"),
    ("Brown Bread", "Bakery", 45, 8, 4.3, "Whole wheat brown bread", "🍞"),
    ("Farm Fresh Eggs (12)", "Dairy", 96, 5, 4.5, "Farm fresh eggs", "🥚"),
    ("Bananas 6 pcs", "Fruits", 42, 22, 4.4, "Naturally ripened bananas", "🍌"),
    ("Basmati Rice 5kg", "Staples", 399, 3, 4.7, "Premium long-grain rice", "🍚"),
    ("Potato Chips", "Snacks", 20, 0, 4.1, "Crunchy salted potato chips", "🥔"),
    ("Cold Coffee 250ml", "Beverages", 55, 16, 4.2, "Ready-to-drink coffee", "☕"),
    ("Dishwash Liquid", "Household", 110, 12, 4.0, "Grease-cutting dishwash liquid", "🧴"),
    ("Tomatoes 500g", "Vegetables", 30, 2, 4.2, "Fresh red tomatoes", "🍅"),
    ("Chocolate Cookies", "Snacks", 60, 19, 4.5, "Chocolate chip cookies", "🍪"),
    ("Paneer 200g", "Dairy", 90, 7, 4.6, "Fresh cottage cheese", "🧀"),
    ("Orange Juice 1L", "Beverages", 125, 11, 4.3, "Orange juice", "🧃"),
]

SAMPLE_ORDERS = [
    (1, 2, 136, "Delivered"),
    (2, 3, 135, "Delivered"),
    (4, 2, 84, "Delivered"),
    (5, 1, 399, "Delivered"),
    (7, 4, 220, "Delivered"),
    (10, 2, 120, "Delivered"),
    (11, 2, 180, "Delivered"),
    (3, 1, 96, "Delivered"),
    (8, 1, 110, "Delivered"),
]


def initialize_database():
    """Create tables and seed demo data once."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                rating REAL NOT NULL,
                description TEXT,
                emoji TEXT
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total REAL NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)

        product_count = connection.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        if product_count == 0:
            connection.executemany("""
                INSERT INTO products
                (name, category, price, stock, rating, description, emoji)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, SAMPLE_PRODUCTS)

            connection.executemany("""
                INSERT INTO orders (product_id, quantity, total, status)
                VALUES (?, ?, ?, ?)
            """, SAMPLE_ORDERS)
