"""Order placement endpoint."""

from fastapi import APIRouter, HTTPException

from app.database import get_connection
from app.schemas import CreateOrderRequest

router = APIRouter(prefix="/api", tags=["Orders"])


@router.post("/orders")
def create_order(order: CreateOrderRequest):
    """Check stock, save the order and reduce inventory."""
    with get_connection() as connection:
        product = connection.execute(
            "SELECT * FROM products WHERE id = ?",
            (order.product_id,)
        ).fetchone()

        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")

        if product["stock"] < order.quantity:
            raise HTTPException(
                status_code=400,
                detail=f'Only {product["stock"]} unit(s) are available'
            )

        order_total = product["price"] * order.quantity

        connection.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (order.quantity, order.product_id)
        )

        cursor = connection.execute("""
            INSERT INTO orders (product_id, quantity, total, status)
            VALUES (?, ?, ?, ?)
        """, (order.product_id, order.quantity, order_total, "Placed"))

        return {
            "order_id": cursor.lastrowid,
            "total": order_total,
            "message": "Order placed successfully"
        }
