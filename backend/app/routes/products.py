"""Product catalogue endpoints."""

from fastapi import APIRouter
from typing import Optional

from app.database import get_connection

router = APIRouter(prefix="/api", tags=["Products"])


@router.get("/products")
def list_products(search: Optional[str] = None, category: Optional[str] = None):
    """Return products, optionally filtered by a search term or category."""
    sql = "SELECT * FROM products WHERE 1 = 1"
    parameters = []

    if search:
        sql += " AND (name LIKE ? OR category LIKE ? OR description LIKE ?)"
        search_value = f"%{search}%"
        parameters.extend([search_value, search_value, search_value])

    if category and category != "All":
        sql += " AND category = ?"
        parameters.append(category)

    sql += " ORDER BY name"

    with get_connection() as connection:
        return [
            dict(row)
            for row in connection.execute(sql, parameters).fetchall()
        ]


@router.get("/categories")
def list_categories():
    """Return all distinct product categories."""
    with get_connection() as connection:
        categories = connection.execute(
            "SELECT DISTINCT category FROM products ORDER BY category"
        ).fetchall()

    return ["All"] + [row["category"] for row in categories]
