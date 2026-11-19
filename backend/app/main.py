"""Application entry point: create the FastAPI app and register API routes."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.seed_data import initialize_database
from app.routes import products, orders, analytics, assistant

# Create tables and insert sample data when the backend starts.
initialize_database()

app = FastAPI(
    title="QuickCommerce AI API",
    description="Product, order, analytics and AI assistant APIs",
    version="1.0.0"
)

# Allow the React development server to call this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Register each group of API endpoints.
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(analytics.router)
app.include_router(assistant.router)


@app.get("/")
def home():
    """Simple health check for the backend."""
    return {
        "message": "QuickCommerce AI backend is running",
        "documentation": "/docs"
    }
