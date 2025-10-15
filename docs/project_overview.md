# Project Overview: AI Recipe Genie

## 1. Project Goal

To create a full-stack application that serves as a practical AI-powered tool for daily life. The app will recommend recipes to users based on the ingredients they currently have, and will also help with diet management and meal planning.

## 2. Key Features

- **AI Recipe Recommendations:** Users input their available ingredients, and the AI (powered by Google Gemini) suggests recipes they can make.
- **Personalized Meal Planning:** The app considers the user's dietary preferences (e.g., vegetarian, low-carb) and allergies to provide customized meal plans.
- **Automatic Shopping Lists:** Generates a shopping list by comparing the ingredients required for a recipe against what the user already has.
- **User Profiles & Authentication:** Users can sign in using Google OAuth to manage their preferences, saved recipes, and ingredient lists.

## 3. Tech Stack

### Backend

- **Framework:** FastAPI (Python)
- **Database:** SQLite
- **AI Integration:** Google Gemini API
- **Authentication:** Google OAuth

### Frontend

- **Framework:** Flutter (Dart)
- **Target Platforms:** Android and Web
- **UI/UX Focus:**
    - Responsive, mobile-friendly design.
    - An intuitive and easy-to-use interface for ingredient input.
    - A polished and "luxurious" overall aesthetic.

## 4. Folder Structure

- **`/backend`**: Contains all backend-related source code.
- **`/frontend`**: Contains all frontend-related source code.
- **`/docs`**: Contains project documentation, including this overview and detailed task lists.
