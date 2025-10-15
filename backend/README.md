# Recipe Genie Backend

This directory contains the backend code for the AI Recipe Genie application, built with FastAPI.

## Features

- **User Authentication**: Secure login with Google OAuth2.
- **Ingredient Management**: CRUD operations for users to manage their ingredients.
- **Recipe Generation**: AI-powered recipe recommendations using the Google Gemini API.
- **Recipe Management**: CRUD operations for users to save and manage their favorite recipes.
- **Shopping List**: Automatic generation of a shopping list based on missing ingredients for a recipe.
- **Interactive API Docs**: Automatic generation of interactive API documentation with Swagger UI and ReDoc.

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python
- **Database**: SQLite
- **Authentication**: Google OAuth with `httpx-oauth`
- **AI**: Google Gemini API
- **Dependency Management**: Poetry
- **Testing**: Pytest

## Getting Started

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)

### Installation & Setup

1.  **Install dependencies:**

    ```bash
    poetry install
    ```

2.  **Set up environment variables:**

    Create a `.env` file in the `backend` directory by copying the example:

    ```bash
    cp .env.example .env
    ```

    You will need to fill in the following values in the `.env` file:

    - `GOOGLE_CLIENT_ID`: Your Google OAuth client ID.
    - `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret.
    - `GEMINI_API_KEY`: Your Google Gemini API key.
    - `SECRET_KEY`: A secret key for signing session cookies. You can generate one using `openssl rand -hex 32`.

### Running the Server

To run the development server, use the following command:

```bash
poetry run uvicorn app.main:app --reload
```

The server will be available at `http://localhost:8000`.

### Running Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

## API Documentation

Once the server is running, you can access the interactive API documentation at the following URLs:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`