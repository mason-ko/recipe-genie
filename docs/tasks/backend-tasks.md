# Backend Tasks

## Phase 1: Project Setup & Core Models

- [ ] **1. FastAPI Project Initialization**
    - [ ] Poetry or Pipenv setup
    - [ ] Create initial project structure (`main.py`, `core`, `models`, `schemas`, `crud`, `api`)
    - [ ] Configure basic settings (e.g., using Pydantic's `BaseSettings`)
- [ ] **2. Database Setup (SQLite)**
    - [ ] SQLAlchemy setup and configuration
    - [ ] Create `database.py` for session management
- [ ] **3. Initial Data Modeling**
    - [ ] Define User model (`models/user.py`)
    - [ ] Define Ingredient model (`models/ingredient.py`)
    - [ ] Define Recipe model (`models/recipe.py`)
    - [ ] Define relationships (e.g., user's ingredients, user's favorite recipes)
- [ ] **4. Schema Definition (Pydantic)**
    - [ ] Create schemas for User (`schemas/user.py`)
    - [ ] Create schemas for Ingredient (`schemas/ingredient.py`)
    - [ ] Create schemas for Recipe (`schemas/recipe.py`)

## Phase 2: User Authentication

- [ ] **1. Google OAuth2 Integration**
    - [ ] Setup Google Cloud project and credentials
    - [ ] Implement OAuth2 flow for login/logout
    - [ ] Create dependency for getting current user
- [ ] **2. User Profile Management**
    - [ ] API endpoint to get user profile
    - [ ] API endpoint to update user profile (dietary preferences, allergies)

## Phase 3: Core Recipe & Ingredient Logic

- [ ] **1. CRUD Operations for Ingredients**
    - [ ] API endpoint to add an ingredient to a user's "fridge"
    - [ ] API endpoint to list a user's ingredients
    - [ ] API endpoint to remove an ingredient
- [ ] **2. Gemini API Integration for Recipe Recommendation**
    - [ ] Create a service/module for Gemini API calls
    - [ ] Develop prompt engineering logic to generate recipes based on ingredients, user preferences.
    - [ ] API endpoint that takes user ingredients and returns AI-generated recipes.
- [ ] **3. Recipe Management**
    - [ ] API endpoint to save a recommended recipe
    - [ ] API endpoint to list saved recipes
    - [ ] API endpoint to view a single recipe

## Phase 4: Advanced Features & Deployment

- [ ] **1. Shopping List Generation**
    - [ ] Logic to compare recipe ingredients with user's current ingredients
    - [ ] API endpoint to generate a shopping list for a specific recipe
- [ ] **2. Testing**
    - [ ] Setup Pytest
    - [ ] Write unit tests for CRUD operations
    - [ ] Write integration tests for API endpoints
- [ ] **3. Documentation**
    - [ ] Auto-generate OpenAPI/Swagger docs
    - [ ] Add descriptions and examples to endpoints
- [ ] **4. Deployment Preparation**
    - [ ] Dockerize the application
    - [ ] Prepare deployment scripts (e.g., for a cloud service)
