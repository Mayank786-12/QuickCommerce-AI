"""Sales and inventory analytics endpoint."""

from fastapi import APIRouter

from app.database import get_connection

router = APIRouter(prefix="/api", tags=["Analytics"])


@router.get("/analytics")
def get_analytics():
    """Calculate revenue, order count, stock alerts and category sales."""
    with get_connection() as connection:
        products = [
            dict(row)
            for row in connection.execute("SELECT * FROM products").fetchall()
        ]
        orders = [
            dict(row)
            for row in connection.execute("SELECT * FROM orders").fetchall()
        ]

    revenue = sum(order["total"] for order in orders)
    units_sold = sum(order["quantity"] for order in orders)
    low_stock_products = [p for p in products if p["stock"] <= 5]

    # Add order revenue to the category of the ordered product.
    category_sales = {}
    for order in orders:
        product = next(
            (p for p in products if p["id"] == order["product_id"]),
            None
        )
        if product:
            category = product["category"]
            category_sales[category] = (
                category_sales.get(category, 0) + order["total"]
            )

    # Count how many units of each product have been ordered.
    product_units = []
    for product in products:
        units = sum(
            order["quantity"]
            for order in orders
            if order["product_id"] == product["id"]
        )
        product_units.append({"name": product["name"], "units": units})

    return {
        "revenue": revenue,
        "orders": len(orders),
        "units_sold": units_sold,
        "products": len(products),
        "low_stock": len(low_stock_products),
        "low_stock_items": low_stock_products,
        "category_sales": [
            {"category": name, "sales": amount}
            for name, amount in sorted(
                category_sales.items(),
                key=lambda item: item[1],
                reverse=True
            )
        ],
        "top_products": sorted(
            product_units,
            key=lambda item: item["units"],
            reverse=True
        )[:5]
    }
