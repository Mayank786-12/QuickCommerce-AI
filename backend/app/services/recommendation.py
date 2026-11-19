"""Assistant logic: Gemini when configured, simple fallback otherwise."""

import os
import re

from dotenv import load_dotenv

from app.database import get_connection

load_dotenv()


def get_all_products():
    """Read all products from SQLite."""
    with get_connection() as connection:
        return [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM products ORDER BY name"
            ).fetchall()
        ]


def build_fallback_answer(question):
    """Generate a useful answer without requiring an external AI key."""
    products = get_all_products()
    question_lower = question.lower()

    # Case 1: the user asks about stock or replenishment.
    stock_keywords = ("low stock", "stock alert", "restock", "replenish")
    if any(word in question_lower for word in stock_keywords):
        low_stock_products = [product for product in products if product["stock"] <= 5]

        if not low_stock_products:
            return "All products currently have more than 5 units in stock."

        lines = [
            f'- {product["name"]}: {product["stock"]} unit(s) left'
            for product in low_stock_products
        ]
        return "These products need attention:\n" + "\n".join(lines)

    # Case 2: the user asks for recommendations.
    recommendation_keywords = ("recommend", "suggest", "breakfast", "snack", "healthy")
    if any(word in question_lower for word in recommendation_keywords):
        available_products = [p for p in products if p["stock"] > 0]
        best_products = sorted(
            available_products,
            key=lambda product: (-product["rating"], product["price"])
        )[:4]

        lines = [
            f'- {p["emoji"]} {p["name"]} — ₹{p["price"]} (rating {p["rating"]})'
            for p in best_products
        ]
        return "Here are some available recommendations:\n" + "\n".join(lines)

    # Case 3: search product names, categories and descriptions.
    search_words = re.findall(r"[a-zA-Z]{3,}", question_lower)
    matching_products = []

    for product in products:
        searchable_text = (
            f'{product["name"]} {product["category"]} {product["description"]}'
        ).lower()

        if any(word in searchable_text for word in search_words):
            matching_products.append(product)

    if matching_products:
        lines = [
            f'- {p["emoji"]} {p["name"]} — ₹{p["price"]}, stock: {p["stock"]}'
            for p in matching_products[:6]
        ]
        return "I found these matching products:\n" + "\n".join(lines)

    return (
        "I can help with product search, recommendations and inventory alerts. "
        "Try asking: 'Show dairy products' or 'Which products are low in stock?'"
    )


def get_assistant_answer(question):
    """Use Gemini if a key is configured; otherwise use fallback logic."""
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key:
        try:
            import google.generativeai as genai

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")

            catalogue_lines = [
                f'{p["name"]} | {p["category"]} | ₹{p["price"]} | stock {p["stock"]}'
                for p in get_all_products()
            ]
            prompt = (
                "You are QuickCommerce AI, a concise shopping assistant. "
                "Only recommend products present in this catalogue.\n\n"
                "PRODUCT CATALOGUE:\n"
                + "\n".join(catalogue_lines)
                + f"\n\nUSER QUESTION: {question}"
            )

            response = model.generate_content(prompt)
            return {"answer": response.text, "mode": "Gemini AI"}

        except Exception:
            # If the AI service is unavailable, the app remains usable.
            pass

    return {
        "answer": build_fallback_answer(question),
        "mode": "Built-in assistant"
    }
