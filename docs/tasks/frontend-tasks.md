# Frontend Tasks

## Phase 1: Project Setup & Basic UI

- [ ] **1. Flutter Project Initialization**
    - [ ] Create new Flutter project
    - [ ] Set up folder structure (e.g., `lib/src`, `lib/src/models`, `lib/src/services`, `lib/src/screens`, `lib/src/widgets`)
    - [ ] Configure for Android and Web
- [ ] **2. Theme and Styling**
    - [ ] Define color palette and typography for a "luxurious" feel
    - [ ] Create a custom theme
- [ ] **3. Navigation**
    - [ ] Set up a routing solution (e.g., `go_router`)
    - [ ] Define initial routes (e.g., `/login`, `/home`, `/recipe_details`)

## Phase 2: User Authentication

- [ ] **1. Login Screen**
    - [ ] Design and build the login screen UI
    - [ ] Implement "Sign in with Google" button
- [ ] **2. Google Sign-In Integration**
    - [ ] Add `google_sign_in` package
    - [ ] Implement Google Sign-In logic
    - [ ] Handle authentication state (logged in/out)

## Phase 3: Core Features

- [ ] **1. Home Screen / My Fridge**
    - [ ] Design a responsive UI for the main screen
    - [ ] Create a user-friendly UX for adding/removing ingredients
        - [ ] Autocomplete search for ingredients
        - [ ] Quick-add buttons for common items
    - [ ] Display the list of current ingredients
- [ ] **2. Recipe Recommendation**
    - [ ] Button to trigger recipe recommendation
    - [ ] UI to display a list of recommended recipes (e.g., with images and titles)
    - [ ] State management for loading and displaying recipes (e.g., using Riverpod or Provider)
- [ ] **3. Recipe Details Screen**
    - [ ] UI to show the full recipe (ingredients, instructions)
    - [ ] Responsive design for both mobile and web

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

- [ ] **1. Unit & Widget Tests**
    - [ ] Write unit tests for services and models
    - [ ] Write widget tests for key screens and widgets
- [ ] **2. Build and Release**
    - [ ] Prepare for Android release (e.g., signing the app)
    - [ ] Prepare for Web deployment
