# Weekly Menu App — Master TODO

This file is read by the `LonelyManager` to dispatch tasks to worker agents.
Each task includes an `[AGENT]` tag indicating which agent type should handle it,
a `[PRIORITY]` level (P1 = critical, P2 = high, P3 = medium, P4 = low),
and a `[STATUS]` field (TODO, IN_PROGRESS, DONE, BLOCKED).

---

## Phase 1 — Project Planning & Architecture

### 1.1 Stack & Architecture Decisions
- [AGENT:planner] [P1] [STATUS:TODO] Define final technology stack for Android app (Kotlin + Jetpack Compose + MVVM)
- [AGENT:planner] [P1] [STATUS:TODO] Define backend stack (Node.js + TypeScript + Express + PostgreSQL)
- [AGENT:planner] [P1] [STATUS:TODO] Define cloud infrastructure plan (GCP Cloud Run + Cloud SQL + Secret Manager)
- [AGENT:planner] [P1] [STATUS:TODO] Define authentication strategy (JWT + bcryptjs, 24h expiry)
- [AGENT:planner] [P1] [STATUS:TODO] Define data storage strategy (PostgreSQL schema, local Room DB for offline support)
- [AGENT:planner] [P2] [STATUS:TODO] Define API versioning strategy (v1 prefix on all routes)
- [AGENT:planner] [P2] [STATUS:TODO] Define CorrelationId strategy for request tracing
- [AGENT:planner] [P2] [STATUS:TODO] Define offline-first vs online-first architecture decision
- [AGENT:planner] [P2] [STATUS:TODO] Define i18n strategy (English + French minimum per VaultWares guidelines)
- [AGENT:planner] [P3] [STATUS:TODO] Evaluate AI/ML meal suggestion integration options (HuggingFace, OpenAI, local model)

### 1.2 Repository Structure
- [AGENT:planner] [P1] [STATUS:TODO] Create Android project scaffold (Gradle, Kotlin DSL, Jetpack Compose)
- [AGENT:planner] [P1] [STATUS:TODO] Create backend project scaffold (Node.js, TypeScript, Express)
- [AGENT:planner] [P1] [STATUS:TODO] Create .env.example with all required environment variables
- [AGENT:planner] [P2] [STATUS:TODO] Configure GitHub Actions CI/CD pipeline for Android build
- [AGENT:planner] [P2] [STATUS:TODO] Configure GitHub Actions CI/CD pipeline for backend deployment to Cloud Run
- [AGENT:planner] [P3] [STATUS:TODO] Configure Gradle signing config for release APK/AAB

---

## Phase 2 — Data Modeling & Database

### 2.1 Core Data Models
- [AGENT:data] [P1] [STATUS:TODO] Define User model (id, email, passwordHash, name, createdAt, updatedAt)
- [AGENT:data] [P1] [STATUS:TODO] Define UserProfile model (userId, numberOfPeople, dietaryProfile, budgetType, budgetAmount, locale)
- [AGENT:data] [P1] [STATUS:TODO] Define DietaryRestriction model (id, userId, type, value) — enum: ALLERGY, INTOLERANCE, PREFERENCE, EXCLUDED_GROUP
- [AGENT:data] [P1] [STATUS:TODO] Define FoodGroup model (id, name, category) — MEAT, POULTRY, FISH, SEAFOOD, VEGAN, VEGETARIAN, CARBS, DAIRY, EGGS, LEGUMES, NUTS, FRUITS, VEGETABLES
- [AGENT:data] [P1] [STATUS:TODO] Define Ingredient model (id, name, foodGroupId, unit, caloriesPer100g, cost, isCommon, allergens[])
- [AGENT:data] [P1] [STATUS:TODO] Define Recipe model (id, name, description, servings, prepTimeMinutes, cookTimeMinutes, difficulty, mealType, cuisineType, imageUrl)
- [AGENT:data] [P1] [STATUS:TODO] Define RecipeIngredient join model (recipeId, ingredientId, quantity, unit, isOptional)
- [AGENT:data] [P1] [STATUS:TODO] Define WeeklyMenu model (id, userId, weekStartDate, generatedAt, totalEstimatedCost, nutritionSummary)
- [AGENT:data] [P1] [STATUS:TODO] Define DayMenu model (weeklyMenuId, dayOfWeek, breakfast, lunch, dinner, snacks[])
- [AGENT:data] [P1] [STATUS:TODO] Define MealSlot model (id, dayMenuId, mealType, recipeId, portionScale, actualCost, includesSide)
- [AGENT:data] [P2] [STATUS:TODO] Define ShoppingList model (id, weeklyMenuId, userId, generatedAt, items[])
- [AGENT:data] [P2] [STATUS:TODO] Define ShoppingListItem model (shoppingListId, ingredientId, totalQuantity, unit, estimatedCost, isOwned, isPurchased)
- [AGENT:data] [P2] [STATUS:TODO] Define NutritionInfo model (recipeId, calories, protein, carbohydrates, fat, fiber, sugar, sodium)
- [AGENT:data] [P2] [STATUS:TODO] Define UserAvailableIngredient model (userId, ingredientId, quantity, unit, expiryDate)
- [AGENT:data] [P3] [STATUS:TODO] Define FavoriteMeal model (userId, recipeId, addedAt)
- [AGENT:data] [P3] [STATUS:TODO] Define MealRating model (userId, recipeId, rating, comment, ratedAt)
- [AGENT:data] [P3] [STATUS:TODO] Define CuisinePreference model (userId, cuisineType, preferenceLevel)

### 2.2 Database Schema & Migrations
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 001 — create users table
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 002 — create user_profiles table
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 003 — create food_groups table with seed data
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 004 — create ingredients table
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 005 — create recipes table
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 006 — create recipe_ingredients join table
- [AGENT:data] [P1] [STATUS:TODO] Write PostgreSQL schema migration 007 — create weekly_menus, day_menus, meal_slots tables
- [AGENT:data] [P2] [STATUS:TODO] Write PostgreSQL schema migration 008 — create dietary_restrictions table
- [AGENT:data] [P2] [STATUS:TODO] Write PostgreSQL schema migration 009 — create shopping_lists and shopping_list_items tables
- [AGENT:data] [P2] [STATUS:TODO] Write PostgreSQL schema migration 010 — create nutrition_info table
- [AGENT:data] [P2] [STATUS:TODO] Write PostgreSQL schema migration 011 — create user_available_ingredients table
- [AGENT:data] [P3] [STATUS:TODO] Write PostgreSQL schema migration 012 — create favorite_meals, meal_ratings tables
- [AGENT:data] [P3] [STATUS:TODO] Write PostgreSQL schema migration 013 — add Row-Level Security policies for all user-scoped tables
- [AGENT:data] [P2] [STATUS:TODO] Seed database with 100+ common recipes across all diet types
- [AGENT:data] [P2] [STATUS:TODO] Seed database with 200+ common ingredients with nutritional data
- [AGENT:data] [P2] [STATUS:TODO] Seed database with food groups and allergen data

### 2.3 Android Local Database (Room)
- [AGENT:data] [P2] [STATUS:TODO] Define Room entity for WeeklyMenu (offline cache)
- [AGENT:data] [P2] [STATUS:TODO] Define Room entity for Recipe (offline cache)
- [AGENT:data] [P2] [STATUS:TODO] Define Room entity for ShoppingList (offline editable)
- [AGENT:data] [P2] [STATUS:TODO] Define Room entity for UserPreferences (offline primary)
- [AGENT:data] [P2] [STATUS:TODO] Create Room DAO interfaces for all entities
- [AGENT:data] [P3] [STATUS:TODO] Implement sync strategy between Room cache and backend API

---

## Phase 3 — Backend API (Node.js + TypeScript + Express)

### 3.1 Project Setup
- [AGENT:backend] [P1] [STATUS:TODO] Initialize backend/ directory with Node.js + TypeScript (strict mode)
- [AGENT:backend] [P1] [STATUS:TODO] Configure tsconfig.json with strict mode, paths, and output directory
- [AGENT:backend] [P1] [STATUS:TODO] Install and configure Express with TypeScript types
- [AGENT:backend] [P1] [STATUS:TODO] Install and configure pg (node-postgres) for PostgreSQL
- [AGENT:backend] [P1] [STATUS:TODO] Install and configure Zod for input validation
- [AGENT:backend] [P1] [STATUS:TODO] Install and configure jsonwebtoken + bcryptjs for auth
- [AGENT:backend] [P1] [STATUS:TODO] Set up middleware: CORS, JSON body parser, error handler, request logger
- [AGENT:backend] [P1] [STATUS:TODO] Implement CorrelationId middleware (attach c+6alphanum to every request)
- [AGENT:backend] [P1] [STATUS:TODO] Implement centralized error handler (structured JSON, no stack traces exposed)
- [AGENT:backend] [P1] [STATUS:TODO] Implement isDbConnected() health check with mock fallback for development
- [AGENT:backend] [P2] [STATUS:TODO] Configure GCP Secret Manager integration for production secrets
- [AGENT:backend] [P2] [STATUS:TODO] Write Dockerfile for Cloud Run deployment
- [AGENT:backend] [P2] [STATUS:TODO] Write cloudbuild.yaml for Cloud Build CI/CD

### 3.2 Authentication Routes (/api/v1/auth)
- [AGENT:backend] [P1] [STATUS:TODO] POST /api/v1/auth/register — validate input (Zod), hash password, create user, return JWT
- [AGENT:backend] [P1] [STATUS:TODO] POST /api/v1/auth/login — validate credentials, compare bcrypt hash, return JWT
- [AGENT:backend] [P1] [STATUS:TODO] POST /api/v1/auth/refresh — validate refresh token, return new access JWT
- [AGENT:backend] [P1] [STATUS:TODO] POST /api/v1/auth/logout — invalidate refresh token
- [AGENT:backend] [P1] [STATUS:TODO] Implement JWT auth middleware (verify signature, check expiry, attach userId to req)

### 3.3 User & Profile Routes (/api/v1/users)
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/users/me — return authenticated user profile
- [AGENT:backend] [P1] [STATUS:TODO] PUT /api/v1/users/me — update user profile (name, email)
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/users/me/preferences — return user's dietary & menu preferences
- [AGENT:backend] [P1] [STATUS:TODO] PUT /api/v1/users/me/preferences — update preferences (people count, diet type, budget)
- [AGENT:backend] [P2] [STATUS:TODO] GET /api/v1/users/me/restrictions — return dietary restrictions and allergies
- [AGENT:backend] [P2] [STATUS:TODO] POST /api/v1/users/me/restrictions — add a dietary restriction or allergy
- [AGENT:backend] [P2] [STATUS:TODO] DELETE /api/v1/users/me/restrictions/:id — remove a dietary restriction

### 3.4 Menu Generation Routes (/api/v1/menus)
- [AGENT:backend] [P1] [STATUS:TODO] POST /api/v1/menus/generate — core endpoint: generate 7-day menu based on user preferences
  - Accept: baseType (meat/vegan/vegetarian/mixed/carbs), includeSides (bool), availableIngredients[], budget (loose/strict/amount), numberOfPeople, specialDiets[], allergies[], excludedFoodGroups[], cuisinePreferences[]
  - Algorithm: balanced macro distribution across 7 days, respect restrictions, avoid repetition, optimize for budget
  - Return: complete WeeklyMenu with all 7 DayMenus and MealSlots
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/menus — list user's past generated menus (paginated)
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/menus/:id — get a specific weekly menu with all details
- [AGENT:backend] [P2] [STATUS:TODO] PUT /api/v1/menus/:id/meals/:mealSlotId — swap a single meal in a menu
- [AGENT:backend] [P2] [STATUS:TODO] DELETE /api/v1/menus/:id — delete a saved menu
- [AGENT:backend] [P2] [STATUS:TODO] POST /api/v1/menus/:id/save — save/bookmark a generated menu
- [AGENT:backend] [P3] [STATUS:TODO] POST /api/v1/menus/:id/share — generate shareable link for a menu

### 3.5 Recipe Routes (/api/v1/recipes)
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/recipes — list recipes with filtering (diet type, meal type, cuisine, max prep time)
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/recipes/:id — get recipe details with ingredients and nutrition
- [AGENT:backend] [P2] [STATUS:TODO] POST /api/v1/recipes/search — full-text search on recipes
- [AGENT:backend] [P2] [STATUS:TODO] GET /api/v1/recipes/:id/alternatives — get alternative recipes with similar nutritional profile
- [AGENT:backend] [P3] [STATUS:TODO] POST /api/v1/recipes — create a custom user recipe
- [AGENT:backend] [P3] [STATUS:TODO] PUT /api/v1/recipes/:id — update a custom user recipe
- [AGENT:backend] [P3] [STATUS:TODO] DELETE /api/v1/recipes/:id — delete a custom user recipe

### 3.6 Ingredients Routes (/api/v1/ingredients)
- [AGENT:backend] [P2] [STATUS:TODO] GET /api/v1/ingredients — list ingredients with search
- [AGENT:backend] [P2] [STATUS:TODO] GET /api/v1/ingredients/food-groups — list all food groups
- [AGENT:backend] [P2] [STATUS:TODO] GET /api/v1/users/me/pantry — get user's available ingredients (pantry)
- [AGENT:backend] [P2] [STATUS:TODO] POST /api/v1/users/me/pantry — add ingredient to user's pantry
- [AGENT:backend] [P2] [STATUS:TODO] PUT /api/v1/users/me/pantry/:id — update ingredient quantity/expiry
- [AGENT:backend] [P2] [STATUS:TODO] DELETE /api/v1/users/me/pantry/:id — remove ingredient from pantry

### 3.7 Shopping List Routes (/api/v1/shopping-lists)
- [AGENT:backend] [P1] [STATUS:TODO] POST /api/v1/shopping-lists/generate — generate shopping list from a weekly menu (subtract pantry items)
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/shopping-lists — list user's shopping lists
- [AGENT:backend] [P1] [STATUS:TODO] GET /api/v1/shopping-lists/:id — get shopping list with all items
- [AGENT:backend] [P2] [STATUS:TODO] PUT /api/v1/shopping-lists/:id/items/:itemId — mark item as purchased or update quantity
- [AGENT:backend] [P2] [STATUS:TODO] DELETE /api/v1/shopping-lists/:id — delete a shopping list

### 3.8 Menu Generation Algorithm
- [AGENT:backend] [P1] [STATUS:TODO] Implement MenuGenerationService — core business logic
  - Filter recipe pool by user restrictions (allergies, intolerances, excluded groups)
  - Filter by available ingredients when pantry mode is enabled
  - Score recipes by nutritional balance (protein/carb/fat ratios across week)
  - Apply budget scoring (loose = prefer cost-efficient, strict = hard cap)
  - Ensure variety (no same recipe twice in a week; limit same protein type to 2x/week)
  - Balance meal complexity (mix of quick <30min and elaborate meals)
  - Assign breakfast, lunch, dinner, optional snacks for each day
  - Respect special diets: keto, Mediterranean, DASH, paleo, gluten-free, low-sodium
- [AGENT:backend] [P2] [STATUS:TODO] Implement NutritionCalculationService — calculate weekly totals and per-day macros
- [AGENT:backend] [P2] [STATUS:TODO] Implement BudgetEstimationService — estimate cost per meal and weekly total
- [AGENT:backend] [P2] [STATUS:TODO] Implement ShoppingListService — aggregate ingredients, subtract pantry, group by category

---

## Phase 4 — Android Application (Kotlin + Jetpack Compose)

### 4.1 Project Structure
- [AGENT:android] [P1] [STATUS:TODO] Create Android project with Kotlin DSL Gradle, min SDK 24, target SDK 35
- [AGENT:android] [P1] [STATUS:TODO] Configure Jetpack Compose with Material 3
- [AGENT:android] [P1] [STATUS:TODO] Configure Hilt for dependency injection
- [AGENT:android] [P1] [STATUS:TODO] Configure Retrofit + OkHttp for API calls
- [AGENT:android] [P1] [STATUS:TODO] Configure Room for local database
- [AGENT:android] [P1] [STATUS:TODO] Configure DataStore for preferences storage
- [AGENT:android] [P1] [STATUS:TODO] Configure Navigation Compose for screen routing
- [AGENT:android] [P2] [STATUS:TODO] Configure Coil for image loading
- [AGENT:android] [P2] [STATUS:TODO] Configure WorkManager for background sync
- [AGENT:android] [P2] [STATUS:TODO] Configure Firebase Crashlytics for error reporting

### 4.2 Project Folder Structure (MVVM)
- [AGENT:android] [P1] [STATUS:TODO] Create app/src/main/java/com/vaultwares/weeklymenu/ package structure:
  - data/ (repository, datasource, room entities/DAOs, retrofit services)
  - domain/ (use cases, models, repository interfaces)
  - ui/ (screens, components, viewmodels, theme)
  - di/ (Hilt modules)
  - util/ (extensions, constants, coroutine helpers)

### 4.3 Authentication Screens
- [AGENT:android] [P1] [STATUS:TODO] Create WelcomeScreen — app logo, tagline, Login/Register buttons
- [AGENT:android] [P1] [STATUS:TODO] Create LoginScreen — email/password form, validation, error states, forgot password link
- [AGENT:android] [P1] [STATUS:TODO] Create RegisterScreen — name, email, password, confirm password fields with real-time validation
- [AGENT:android] [P1] [STATUS:TODO] Implement AuthViewModel — handle login/register API calls, JWT storage in DataStore
- [AGENT:android] [P1] [STATUS:TODO] Implement JWT token refresh interceptor in OkHttp

### 4.4 Onboarding & Preferences Screens
- [AGENT:android] [P1] [STATUS:TODO] Create OnboardingScreen Step 1 — number of people to feed (stepper: 1–10+)
- [AGENT:android] [P1] [STATUS:TODO] Create OnboardingScreen Step 2 — base diet type selection (chips: Omnivore, Vegan, Vegetarian, Pescatarian, Flexitarian)
- [AGENT:android] [P1] [STATUS:TODO] Create OnboardingScreen Step 3 — special diets (multi-select chips: Keto, Mediterranean, DASH, Paleo, Gluten-Free, Low-Sodium, Low-Carb, High-Protein)
- [AGENT:android] [P1] [STATUS:TODO] Create OnboardingScreen Step 4 — food allergies and intolerances (multi-select: Gluten, Dairy, Eggs, Nuts, Peanuts, Shellfish, Fish, Soy, Sesame)
- [AGENT:android] [P1] [STATUS:TODO] Create OnboardingScreen Step 5 — excluded food groups (chips: Pork, Beef, Poultry, Seafood, Dairy, etc.)
- [AGENT:android] [P1] [STATUS:TODO] Create OnboardingScreen Step 6 — budget preference (radio: No budget / Loose budget / Strict budget + amount input)
- [AGENT:android] [P2] [STATUS:TODO] Create OnboardingScreen Step 7 — cuisine preferences (multi-select: Italian, Asian, Mexican, Mediterranean, French, American, etc.)
- [AGENT:android] [P2] [STATUS:TODO] Create OnboardingScreen Step 8 — meal prep preference (Quick <30min / Normal / Elaborate)
- [AGENT:android] [P2] [STATUS:TODO] Create OnboardingScreen Step 9 — include sides (Yes / No / Sometimes)
- [AGENT:android] [P1] [STATUS:TODO] Implement PreferencesViewModel — collect, validate, and save preferences
- [AGENT:android] [P1] [STATUS:TODO] Implement step progress indicator at top of onboarding flow

### 4.5 Home / Dashboard Screen
- [AGENT:android] [P1] [STATUS:TODO] Create HomeScreen — show current week menu summary, quick actions, recent menus
- [AGENT:android] [P1] [STATUS:TODO] Create WeekSummaryCard — horizontal scrollable day selector, macro summary bar
- [AGENT:android] [P2] [STATUS:TODO] Create QuickStatsRow — weekly calories, estimated cost, number of unique ingredients
- [AGENT:android] [P2] [STATUS:TODO] Create RecentMenuCard — thumbnail, week date range, diet type badge
- [AGENT:android] [P1] [STATUS:TODO] Implement HomeViewModel — fetch current menu, refresh state, navigation triggers

### 4.6 Menu Generation Screen
- [AGENT:android] [P1] [STATUS:TODO] Create GenerateMenuScreen — form with all generation options (override onboarding defaults)
  - Base type selector (Meat / Vegan / Vegetarian / Mixed / Carbs-focus)
  - Include sides toggle
  - Budget override (use saved / enter amount)
  - Use pantry toggle (use available ingredients)
  - Number of people override stepper
  - Cuisine preferences chips (optional override)
  - Special diet chips (optional override)
- [AGENT:android] [P1] [STATUS:TODO] Create GeneratingAnimationScreen — loading state with animated cooking icon and progress steps
- [AGENT:android] [P1] [STATUS:TODO] Implement GenerateMenuViewModel — API call, loading states, error handling, navigation to result

### 4.7 Weekly Menu View Screen
- [AGENT:android] [P1] [STATUS:TODO] Create WeeklyMenuScreen — top-level screen with day tabs
- [AGENT:android] [P1] [STATUS:TODO] Create DayMenuView — show all meals for a day (breakfast, lunch, dinner, snacks)
- [AGENT:android] [P1] [STATUS:TODO] Create MealCard — recipe name, prep time, calories, diet badges, swap button
- [AGENT:android] [P2] [STATUS:TODO] Create NutritionSummaryBar — daily macro breakdown (protein/carbs/fat progress bars)
- [AGENT:android] [P2] [STATUS:TODO] Create DayCostChip — estimated cost for the day
- [AGENT:android] [P1] [STATUS:TODO] Implement meal swap dialog — show alternative recipes, confirm swap
- [AGENT:android] [P1] [STATUS:TODO] Implement WeeklyMenuViewModel — load menu, swap meals, save/unsave menu

### 4.8 Recipe Detail Screen
- [AGENT:android] [P1] [STATUS:TODO] Create RecipeDetailScreen — full recipe with header image, info row, ingredients, steps
- [AGENT:android] [P1] [STATUS:TODO] Create IngredientsList — scrollable list with quantity/unit, owned indicator
- [AGENT:android] [P1] [STATUS:TODO] Create CookingStepsList — numbered steps with timing indicators
- [AGENT:android] [P2] [STATUS:TODO] Create NutritionCard — full macro breakdown table (calories, protein, carbs, fat, fiber, etc.)
- [AGENT:android] [P2] [STATUS:TODO] Create ServingScaler — adjust serving count and auto-scale ingredient quantities
- [AGENT:android] [P2] [STATUS:TODO] Implement favorite toggle on recipe detail
- [AGENT:android] [P1] [STATUS:TODO] Implement RecipeDetailViewModel — load recipe, handle favorite, serving scale

### 4.9 Shopping List Screen
- [AGENT:android] [P1] [STATUS:TODO] Create ShoppingListScreen — categorized list of all needed ingredients
- [AGENT:android] [P1] [STATUS:TODO] Create ShoppingListItem — ingredient name, quantity, unit, cost estimate, checkbox
- [AGENT:android] [P2] [STATUS:TODO] Create CategorySection headers (Produce, Dairy, Meat, Pantry, etc.)
- [AGENT:android] [P2] [STATUS:TODO] Create BudgetSummaryCard — estimated total vs budget, items remaining
- [AGENT:android] [P2] [STATUS:TODO] Implement check-off functionality with strike-through animation
- [AGENT:android] [P3] [STATUS:TODO] Implement share shopping list (text/WhatsApp/clipboard)
- [AGENT:android] [P1] [STATUS:TODO] Implement ShoppingListViewModel — generate list, load list, toggle items

### 4.10 Pantry / Available Ingredients Screen
- [AGENT:android] [P2] [STATUS:TODO] Create PantryScreen — list of user's stocked ingredients
- [AGENT:android] [P2] [STATUS:TODO] Create AddIngredientBottomSheet — search ingredients, enter quantity and unit, optional expiry
- [AGENT:android] [P2] [STATUS:TODO] Create PantryItemCard — ingredient name, quantity, expiry indicator (green/yellow/red)
- [AGENT:android] [P2] [STATUS:TODO] Implement PantryViewModel — load, add, update, delete pantry items

### 4.11 Settings & Profile Screen
- [AGENT:android] [P2] [STATUS:TODO] Create SettingsScreen — edit preferences, theme toggle, account settings, logout
- [AGENT:android] [P2] [STATUS:TODO] Create EditPreferencesScreen — re-run onboarding flow with saved values pre-filled
- [AGENT:android] [P3] [STATUS:TODO] Create ThemeSelector — choose from VaultWares skins (light/dark + accent)
- [AGENT:android] [P2] [STATUS:TODO] Create AccountSection — change email, change password, delete account
- [AGENT:android] [P2] [STATUS:TODO] Implement SettingsViewModel — update preferences, handle account actions

### 4.12 Navigation & App Shell
- [AGENT:android] [P1] [STATUS:TODO] Implement bottom navigation bar (Home, Generate, Shopping List, Pantry, Settings)
- [AGENT:android] [P1] [STATUS:TODO] Implement NavHost with all routes and argument types
- [AGENT:android] [P1] [STATUS:TODO] Implement auth guard navigation (redirect to login if no valid JWT)
- [AGENT:android] [P2] [STATUS:TODO] Implement deep link support for shared menus

---

## Phase 5 — UI/UX Design

### 5.1 Design System
- [AGENT:uiux] [P1] [STATUS:TODO] Define Material 3 color scheme mapped to VaultWares STYLE.md palettes
  - Dark theme: base #4A5459, surface #52606B, accent cyan #21b8cc (skin #7 variant)
  - Light theme: background #fafafa, surface #f0f0f0, text #333333, accent #7c3aed (skin #9)
- [AGENT:uiux] [P1] [STATUS:TODO] Define typography scale (Segoe UI Semilight equivalent for Android: Roboto Semilight / Nunito)
- [AGENT:uiux] [P1] [STATUS:TODO] Define spacing system (4dp base grid, consistent with Tailwind scale analog)
- [AGENT:uiux] [P1] [STATUS:TODO] Define shape system (8dp corner radius for cards, 50% for chips/FAB)
- [AGENT:uiux] [P2] [STATUS:TODO] Define motion specs (150ms enter, 100ms hover, respect reduceMotion)
- [AGENT:uiux] [P2] [STATUS:TODO] Define icon set (Material Symbols rounded, supplemented with custom food icons)

### 5.2 Component Library (Compose)
- [AGENT:uiux] [P1] [STATUS:TODO] Create WeeklyMenuTheme composable (wraps MaterialTheme with custom colors/typography)
- [AGENT:uiux] [P1] [STATUS:TODO] Create DietBadge composable (colored chip for Vegan/Keto/etc.)
- [AGENT:uiux] [P1] [STATUS:TODO] Create MacroProgressBar composable (protein/carb/fat segmented bar)
- [AGENT:uiux] [P1] [STATUS:TODO] Create QuantityStepper composable (reusable +/- spinner)
- [AGENT:uiux] [P2] [STATUS:TODO] Create AnimatedFoodIcon composable (Lottie-based cooking animation for loading states)
- [AGENT:uiux] [P2] [STATUS:TODO] Create GlassCard composable (frosted glass effect for hero sections, per VaultWares glass-ui)
- [AGENT:uiux] [P2] [STATUS:TODO] Create ToastNotification composable (dismissible, success/error/info variants)
- [AGENT:uiux] [P2] [STATUS:TODO] Create FilterChipGroup composable (reusable multi-select chip group)
- [AGENT:uiux] [P3] [STATUS:TODO] Create CalendarWeekView composable (horizontal scrollable day selector)

### 5.3 Accessibility
- [AGENT:uiux] [P2] [STATUS:TODO] Ensure all interactive elements have contentDescription for screen readers
- [AGENT:uiux] [P2] [STATUS:TODO] Ensure minimum 4.5:1 contrast ratio for all text (WCAG AA)
- [AGENT:uiux] [P2] [STATUS:TODO] Implement reduceMotion support in all animations
- [AGENT:uiux] [P3] [STATUS:TODO] Add TalkBack announcements for menu generation progress

---

## Phase 6 — Documentation

### 6.1 Technical Documentation
- [AGENT:doc] [P1] [STATUS:TODO] Write API documentation (OpenAPI/Swagger spec for all endpoints)
- [AGENT:doc] [P1] [STATUS:TODO] Write README.md — project overview, setup instructions, architecture diagram
- [AGENT:doc] [P2] [STATUS:TODO] Write ARCHITECTURE.md — detailed system design, component interaction diagrams
- [AGENT:doc] [P2] [STATUS:TODO] Write backend/README.md — backend setup, environment variables, local dev guide
- [AGENT:doc] [P2] [STATUS:TODO] Write android/README.md — Android setup, build instructions, signing guide
- [AGENT:doc] [P2] [STATUS:TODO] Write database/README.md — schema overview, migration guide, seed data
- [AGENT:doc] [P3] [STATUS:TODO] Write CONTRIBUTING.md additions specific to weekly-menu app

### 6.2 User-Facing Documentation
- [AGENT:doc] [P3] [STATUS:TODO] Write user guide — how to set up preferences, generate a menu, use shopping list
- [AGENT:doc] [P3] [STATUS:TODO] Write FAQ — common questions about diet types, budget options, ingredient tracking

---

## Phase 7 — Testing

### 7.1 Backend Testing
- [AGENT:backend] [P2] [STATUS:TODO] Write unit tests for MenuGenerationService (all diet combos, budget modes, edge cases)
- [AGENT:backend] [P2] [STATUS:TODO] Write unit tests for NutritionCalculationService
- [AGENT:backend] [P2] [STATUS:TODO] Write unit tests for BudgetEstimationService
- [AGENT:backend] [P2] [STATUS:TODO] Write integration tests for all auth routes
- [AGENT:backend] [P2] [STATUS:TODO] Write integration tests for menu generation route
- [AGENT:backend] [P3] [STATUS:TODO] Write integration tests for shopping list route
- [AGENT:backend] [P3] [STATUS:TODO] Write load tests for menu generation endpoint (simulate 100 concurrent requests)

### 7.2 Android Testing
- [AGENT:android] [P2] [STATUS:TODO] Write unit tests for all ViewModels using Turbine + JUnit5
- [AGENT:android] [P2] [STATUS:TODO] Write unit tests for all UseCases / repository implementations
- [AGENT:android] [P2] [STATUS:TODO] Write Compose UI tests for critical flows (login, onboarding, menu generation)
- [AGENT:android] [P3] [STATUS:TODO] Write end-to-end instrumentation tests with Espresso

---

## Phase 8 — Security & Compliance

- [AGENT:backend] [P1] [STATUS:TODO] Enable OWASP input sanitization on all endpoints
- [AGENT:backend] [P1] [STATUS:TODO] Add rate limiting middleware (100 req/min per IP, 20 req/min for auth endpoints)
- [AGENT:backend] [P1] [STATUS:TODO] Add HTTPS-only enforcement and HSTS header
- [AGENT:backend] [P1] [STATUS:TODO] Validate all JWT tokens on every protected route (signature + expiry)
- [AGENT:backend] [P1] [STATUS:TODO] Enforce Row-Level Security (RLS) in all user-scoped queries (filter by userId from JWT)
- [AGENT:backend] [P2] [STATUS:TODO] Add SQL injection scan to CI pipeline
- [AGENT:android] [P1] [STATUS:TODO] Store JWT securely in Android EncryptedSharedPreferences / DataStore with encryption
- [AGENT:android] [P1] [STATUS:TODO] Implement certificate pinning for API requests
- [AGENT:android] [P2] [STATUS:TODO] Enable Android ProGuard/R8 rules for release builds
- [AGENT:android] [P2] [STATUS:TODO] Add network security config (cleartext traffic disabled in production)

---

## Phase 9 — Deployment & DevOps

- [AGENT:planner] [P2] [STATUS:TODO] Create Docker Compose for local development (PostgreSQL + backend)
- [AGENT:planner] [P2] [STATUS:TODO] Configure Cloud SQL instance (PostgreSQL 15, private IP)
- [AGENT:planner] [P2] [STATUS:TODO] Configure Cloud Run service for backend (min-instances=0, max-instances=10)
- [AGENT:planner] [P2] [STATUS:TODO] Configure Secret Manager secrets (DB_URL, JWT_SECRET, ENCRYPTION_KEY)
- [AGENT:planner] [P3] [STATUS:TODO] Configure Cloud Build trigger on main branch push
- [AGENT:planner] [P3] [STATUS:TODO] Configure environment-specific configs (dev/staging/production)
- [AGENT:planner] [P3] [STATUS:TODO] Set up error alerting (Cloud Monitoring + Slack webhook)

---

## Phase 10 — Internationalization

- [AGENT:android] [P2] [STATUS:TODO] Extract all Android string resources to strings.xml (English)
- [AGENT:android] [P2] [STATUS:TODO] Create French translation file values-fr/strings.xml
- [AGENT:backend] [P2] [STATUS:TODO] Add Accept-Language header support in API responses
- [AGENT:backend] [P2] [STATUS:TODO] Localize error messages in API responses (en + fr)

---

_Last updated: auto-maintained by LonelyManager_
_Total tasks: 238 across all phases_
