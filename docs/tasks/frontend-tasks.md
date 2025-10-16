# Frontend Tasks

## Phase 1: Project Setup & Basic UI

- [x] **1. Flutter Project Initialization**
    - [x] Create new Flutter project
    - [x] Set up folder structure (e.g., `lib/src`, `lib/src/models`, `lib/src/services`, `lib/src/screens`, `lib/src/widgets`)
    - [x] Configure for Android and Web
- [x] **2. Theme and Styling**
    - [x] Define color palette and typography for a "luxurious" feel
    - [x] Create a custom theme
- [x] **3. Navigation**
    - [x] Set up a routing solution (e.g., `go_router`)
    - [x] Define initial routes (e.g., `/login`, `/home`, `/recipe_details`)

## Phase 2: User Authentication

- [x] **1. Login Screen**
    - [x] Design and build the login screen UI
    - [x] Implement "Sign in with Google" button
- [x] **2. Google Sign-In Integration**
    - [x] Add `google_sign_in` package
    - [x] Implement Google Sign-In logic
    - [x] Handle authentication state (logged in/out)

## Phase 3: Core Features

- [x] **1. Home Screen / My Fridge**
    - [x] Design a responsive UI for the main screen
    - [x] Create a user-friendly UX for adding/removing ingredients
        - [x] Autocomplete search for ingredients
        - [x] Quick-add buttons for common items
    - [x] Display the list of current ingredients
- [x] **2. Recipe Recommendation**
    - [x] Button to trigger recipe recommendation
    - [x] UI to display a list of recommended recipes (e.g., with images and titles)
    - [x] State management for loading and displaying recipes (e.g., using Riverpod or Provider)
- [x] **3. Recipe Details Screen**
    - [x] UI to show the full recipe (ingredients, instructions)
    - [x] Responsive design for both mobile and web

## Phase 4: Advanced Features & Polish

- [ ] **1. User Profile Screen**
    - [ ] UI to display user information
    - [ ] Form to edit dietary preferences and allergies
- [ ] **2. Shopping List**
    - [ ] UI to display the generated shopping list
- [ ] **3. State Management & Caching**
    - [ ] Implement a robust state management solution (e.g., Riverpod)
    - [ ] Cache server data to improve performance and reduce API calls
- [ ] **4. Animations & Final Touches**
    - [ ] Add subtle animations to enhance the user experience
    - [ ] Final UI polish for a "luxurious" feel

## Phase 5: Testing & Deployment

- [x] **1. Unit & Widget Tests**
    - [x] Write unit tests for services and models
    - [x] Write widget tests for key screens and widgets
- [ ] **2. Build and Release**
    - [ ] Prepare for Android release (e.g., signing the app)
    - [ ] Prepare for Web deployment
