# Backend Tasks

## Phase 1: Project Setup & Core Models

- [x] **1. FastAPI Project Initialization**
    - [x] Poetry or Pipenv setup
    - [x] Create initial project structure (`main.py`, `core`, `models`, `schemas`, `crud`, `api`)
    - [x] Configure basic settings (e.g., using Pydantic's `BaseSettings`)
- [x] **2. Database Setup (SQLite)**
    - [x] SQLAlchemy setup and configuration
    - [x] Create `database.py` for session management
- [x] **3. Initial Data Modeling**
    - [x] Define User model (`models/user.py`)
    - [x] Define Ingredient model (`models/ingredient.py`)
    - [x] Define Recipe model (`models/recipe.py`)
    - [x] Define relationships (e.g., user's ingredients, user's favorite recipes)
- [x] **4. Schema Definition (Pydantic)**
    - [x] Create schemas for User (`schemas/user.py`)
    - [x] Create schemas for Ingredient (`schemas/ingredient.py`)
    - [x] Create schemas for Recipe (`schemas/recipe.py`)

## Phase 2: User Authentication

- [x] **1. Google OAuth2 Integration**
    - [x] Setup Google Cloud project and credentials
    - [x] Implement OAuth2 flow for login/logout
    - [x] Create dependency for getting current user
- [x] **2. User Profile Management**
    - [x] API endpoint to get user profile
    - [x] API endpoint to update user profile (dietary preferences, allergies)

## Phase 3: Core Recipe & Ingredient Logic

- [x] **1. CRUD Operations for Ingredients**
    - [x] API endpoint to add an ingredient to a user's "fridge"
    - [x] API endpoint to list a user's ingredients
    - [x] API endpoint to remove an ingredient
- [x] **2. Gemini API Integration for Recipe Recommendation**
    - [x] Create a service/module for Gemini API calls
    - [x] Develop prompt engineering logic to generate recipes based on ingredients, user preferences.
    - [x] API endpoint that takes user ingredients and returns AI-generated recipes.
- [x] **3. Recipe Management**
    - [x] API endpoint to save a recommended recipe
    - [x] API endpoint to list saved recipes
    - [x] API endpoint to view a single recipe

## Phase 4: Advanced Features & Deployment

- [x] **1. Shopping List Generation**
    - [x] Logic to compare recipe ingredients with user's current ingredients
    - [x] API endpoint to generate a shopping list for a specific recipe
- [x] **2. Testing**
    - [x] Setup Pytest
    - [x] Write unit tests for CRUD operations
    - [x] Write integration tests for API endpoints
- [x] **3. Documentation**
    - [x] Auto-generate OpenAPI/Swagger docs
    - [x] Add descriptions and examples to endpoints
- [ ] **4. Deployment Preparation** (Skipped)
    - [ ] Dockerize the application
    - [ ] Prepare deployment scripts (e.g., for a cloud service)