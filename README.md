# QuickCommerce AI — Quick-Commerce Intelligence Platform

A beginner-friendly full-stack project that demonstrates product discovery, order placement,
sales analytics, inventory alerts, and an AI shopping assistant.

## 1. Project structure

```text
QuickCommerce_AI_Clean/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Starts FastAPI and registers routes
│   │   ├── database.py             # Opens SQLite database connections
│   │   ├── seed_data.py             # Creates tables and inserts demo records
│   │   ├── schemas.py               # Validates API request data
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── products.py          # Product listing and search
│   │   │   ├── orders.py            # Order placement
│   │   │   ├── analytics.py         # Sales and stock summary
│   │   │   └── assistant.py         # AI assistant endpoint
│   │   └── services/
│   │       ├── __init__.py
│   │       └── recommendation.py    # Recommendation and fallback logic
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   └── src/
│       ├── main.jsx                # React entry point
│       ├── App.jsx                 # Main application and navigation
│       ├── api.js                  # All backend API calls
│       ├── components/
│       │   ├── Sidebar.jsx
│       │   ├── Header.jsx
│       │   ├── StatCard.jsx
│       │   ├── ProductCard.jsx
│       │   └── AssistantPanel.jsx
│       ├── pages/
│       │   ├── Dashboard.jsx
│       │   └── Products.jsx
│       └── styles.css
│
├── run_backend.bat                 # Windows helper to start the backend
└── run_frontend.bat                # Windows helper to start the frontend
```

## 2. Requirements

- Python 3.10 or newer
- Node.js 18 or newer
- VS Code (recommended)

## 3. Run the project on Windows

### Terminal 1 — Backend


