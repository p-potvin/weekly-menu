# Weekly Menu App — Project Roadmap

This document is read by the `LonelyManager` to understand project milestones and phases.

---

## Vision

**Weekly Menu** is a privacy-first Android application built by VaultWares that generates
personalized 7-day meal plans. Users configure their dietary preferences, restrictions,
allergies, budget, and available ingredients once — and the app creates a balanced,
varied, and budget-aware weekly menu on demand, complete with an auto-generated
shopping list.

---

## Milestones

### 🏁 Milestone 0 — Project Bootstrapping (Week 1–2)
**Goal:** Establish scaffolding, tooling, and CI/CD so all agents can work in parallel.

| Deliverable | Owner | Status |
|---|---|---|
| TODO.md with all tasks defined | planner | ✅ Done |
| ROADMAP.md with milestones | planner | ✅ Done |
| Android project scaffold | android | TODO |
| Backend project scaffold | backend | TODO |
| PostgreSQL schema migrations 001–007 | data | TODO |
| .env.example file | backend | TODO |
| GitHub Actions CI (Android build) | planner | TODO |
| GitHub Actions CI (Backend lint/test) | planner | TODO |
| Docker Compose for local dev | planner | TODO |
| agent_manifest.md updated | planner | ✅ Done |

---

### 🔐 Milestone 1 — Authentication & Onboarding (Week 3–4)
**Goal:** Users can register, log in, and complete the onboarding preference wizard.

| Deliverable | Owner | Status |
|---|---|---|
| Backend: auth routes (register, login, refresh, logout) | backend | TODO |
| Backend: user profile & preferences routes | backend | TODO |
| Android: WelcomeScreen, LoginScreen, RegisterScreen | android | TODO |
| Android: 9-step OnboardingFlow | android | TODO |
| Android: JWT storage (EncryptedDataStore) | android | TODO |
| Android: Auth navigation guard | android | TODO |
| Database migrations 001–002 (users, profiles) | data | TODO |

---

### 🍽️ Milestone 2 — Core Menu Generation (Week 5–7)
**Goal:** The app can generate a complete 7-day menu based on user preferences.

| Deliverable | Owner | Status |
|---|---|---|
| Database migrations 003–007 (food groups, ingredients, recipes, menus) | data | TODO |
| Seed data: 100+ recipes | data | TODO |
| Seed data: 200+ ingredients with nutrition | data | TODO |
| Backend: MenuGenerationService | backend | TODO |
| Backend: NutritionCalculationService | backend | TODO |
| Backend: BudgetEstimationService | backend | TODO |
| Backend: POST /api/v1/menus/generate | backend | TODO |
| Backend: GET /api/v1/menus/:id | backend | TODO |
| Android: GenerateMenuScreen | android | TODO |
| Android: WeeklyMenuScreen + DayMenuView + MealCard | android | TODO |
| Android: GenerateMenuViewModel + WeeklyMenuViewModel | android | TODO |
| Android: Meal swap dialog | android | TODO |

---

### 🛒 Milestone 3 — Shopping List & Pantry (Week 8–9)
**Goal:** Users can generate a shopping list from their menu and manage pantry items.

| Deliverable | Owner | Status |
|---|---|---|
| Database migrations 008–011 | data | TODO |
| Backend: ShoppingListService | backend | TODO |
| Backend: shopping-list routes | backend | TODO |
| Backend: pantry routes | backend | TODO |
| Android: ShoppingListScreen | android | TODO |
| Android: PantryScreen + AddIngredientBottomSheet | android | TODO |
| Android: ShoppingListViewModel + PantryViewModel | android | TODO |

---

### 🎨 Milestone 4 — UI Polish & Design System (Week 10–11)
**Goal:** App feels polished, on-brand, accessible, and supports light/dark themes.

| Deliverable | Owner | Status |
|---|---|---|
| WeeklyMenuTheme with VaultWares palettes | uiux | TODO |
| Full component library (DietBadge, MacroBar, etc.) | uiux | TODO |
| Glassmorphism hero sections | uiux | TODO |
| Animations and motion specs | uiux | TODO |
| Accessibility audit (contrast, TalkBack, reduceMotion) | uiux | TODO |
| Android: HomeScreen polish | android | TODO |
| Android: RecipeDetailScreen | android | TODO |
| Android: SettingsScreen + ThemeSelector | android | TODO |

---

### 🔒 Milestone 5 — Security Hardening (Week 12)
**Goal:** Full OWASP compliance, rate limiting, certificate pinning, RLS.

| Deliverable | Owner | Status |
|---|---|---|
| Backend: rate limiting middleware | backend | TODO |
| Backend: RLS on all user queries | backend | TODO |
| Backend: HSTS + HTTPS enforcement | backend | TODO |
| Android: certificate pinning | android | TODO |
| Android: ProGuard/R8 rules | android | TODO |
| Android: EncryptedSharedPreferences for JWT | android | TODO |
| Security audit pass | backend | TODO |

---

### 🌐 Milestone 6 — i18n & Localization (Week 13)
**Goal:** App supports English and French per VaultWares guidelines.

| Deliverable | Owner | Status |
|---|---|---|
| Android: strings.xml fully extracted | android | TODO |
| Android: values-fr/strings.xml translation | android | TODO |
| Backend: localized error messages (en + fr) | backend | TODO |
| Backend: Accept-Language header support | backend | TODO |

---

### ☁️ Milestone 7 — Cloud Deployment (Week 14–15)
**Goal:** Production backend deployed to Cloud Run, connected to Cloud SQL.

| Deliverable | Owner | Status |
|---|---|---|
| Cloud SQL instance provisioned | planner | TODO |
| Secret Manager secrets configured | planner | TODO |
| Cloud Run service deployed | planner | TODO |
| Cloud Build pipeline configured | planner | TODO |
| E2E smoke test on production | backend | TODO |
| Android: production API URL configured | android | TODO |
| Play Store internal test track upload | android | TODO |

---

### ✅ Milestone 8 — Testing & Quality Gate (Week 15–16)
**Goal:** All critical paths tested, coverage gates enforced.

| Deliverable | Owner | Status |
|---|---|---|
| Backend: unit tests for all services | backend | TODO |
| Backend: integration tests for all routes | backend | TODO |
| Android: ViewModel unit tests | android | TODO |
| Android: Compose UI tests for critical flows | android | TODO |
| Android: end-to-end instrumentation tests | android | TODO |
| Documentation complete | doc | TODO |

---

## Tech Stack Summary

| Layer | Technology |
|---|---|
| Android app | Kotlin, Jetpack Compose, Material 3, Hilt, Room, Retrofit, DataStore |
| Backend API | Node.js, TypeScript (strict), Express, Zod, pg (node-postgres) |
| Database | PostgreSQL 15 via Google Cloud SQL |
| Auth | JWT (jsonwebtoken) + bcryptjs, 24h expiry |
| Cloud | Google Cloud Run, Cloud SQL, Secret Manager, Cloud Build |
| CI/CD | GitHub Actions + Cloud Build |
| Agent Coordination | Redis pub/sub via vaultwares-agentciation |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                  Android App (Kotlin)                    │
│  ┌──────────┐  ┌────────────┐  ┌──────────────────────┐ │
│  │  UI Layer│  │  ViewModel │  │  Repository / Domain  │ │
│  │ (Compose)│◄─┤  (MVVM)   │◄─┤  (UseCases + Room)   │ │
│  └──────────┘  └────────────┘  └──────────┬───────────┘ │
└──────────────────────────────────────────|──────────────┘
                                            │ HTTPS / JWT
                         ┌──────────────────▼──────────────┐
                         │   Backend API (Express/Node.js)  │
                         │   POST /api/v1/menus/generate    │
                         │   GET  /api/v1/menus/:id         │
                         │   POST /api/v1/shopping-lists    │
                         └──────────────────┬───────────────┘
                                            │
                         ┌──────────────────▼──────────────┐
                         │    PostgreSQL (Cloud SQL)        │
                         │    Row-Level Security enforced   │
                         └─────────────────────────────────┘
```

---

_Maintained by: LonelyManager + VaultWares Coding Agents_
