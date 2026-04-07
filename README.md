# Weekly Menu — AI-Powered 7-Day Meal Planner

A **privacy-first Android application** built by VaultWares that generates personalized
7-day meal plans tailored to your dietary preferences, food restrictions, budget, and pantry.

---

## Features

- 🥩 **Base diet selection** — Omnivore, Vegan, Vegetarian, Pescatarian, Flexitarian
- 🌿 **Special diets** — Keto, Mediterranean, DASH, Paleo, Gluten-Free, Low-Sodium, High-Protein
- 🚫 **Allergies & intolerances** — Gluten, Dairy, Eggs, Nuts, Shellfish, Fish, Soy, Sesame
- 🥦 **Food group exclusions** — Exclude any specific food group
- 💰 **Budget control** — No budget / Loose estimate / Strict weekly cap
- 👨‍👩‍👧 **Multi-person serving** — Scale all meals and shopping lists for 1–10+ people
- 🧂 **Pantry integration** — Tell the app what you have, reduce your shopping list
- 🛒 **Auto shopping list** — Categorised, check-off enabled, with cost estimates
- 📊 **Nutrition balance** — Macros balanced across the full week
- 🌍 **Cuisine variety** — Italian, Asian, Mexican, Mediterranean, and more
- 🔄 **Meal swapping** — Tap any meal to see alternatives
- 🌗 **Light & dark themes** — VaultWares branded, Material 3

---

## Architecture

```
Android App (Kotlin + Jetpack Compose + MVVM)
    ↕ HTTPS / JWT
Backend API (Node.js + TypeScript + Express)
    ↕ Parameterized SQL
PostgreSQL 15 (Google Cloud SQL, RLS enforced)
```

See [ROADMAP.md](ROADMAP.md) for full milestone plan and [TODO.md](TODO.md) for all tasks.

---

## Agent System

This project uses the **VaultWares agentciation** multi-agent framework.
The `LonelyManager` reads `TODO.md` and `ROADMAP.md` to dispatch development tasks
to specialized worker agents:

| Agent | Responsibilities |
|---|---|
| `planner-agent` | Architecture decisions, scaffolding, CI/CD, DevOps |
| `data-agent` | Database schema, migrations, seed data, Room entities |
| `backend-agent` | Node.js API routes, services, business logic, tests |
| `android-agent` | Kotlin/Compose screens, ViewModels, navigation, tests |
| `uiux-agent` | Design system, component library, accessibility |
| `doc-agent` | API docs, README files, architecture diagrams |

### Running the Agent System

```bash
# Install dependencies
pip install redis

# Start Redis
redis-server vaultwares-agentciation/redis.conf

# Run the full coordination system
python run_coordinated_system.py

# Or run the manager alone
python run_lonely_manager.py
```

---

## Quick Start (Development)

### Backend

```bash
cd backend/
npm install
cp .env.example .env.local   # Fill in your environment variables
npm run dev
```

### Android

Open `android/` in Android Studio (Hedgehog or later).
Set `BASE_URL` in `local.properties` to your backend URL.
Run on emulator (min API 24) or device.

---

## Guidelines

This project follows all [VaultWares enterprise guidelines](.github/INSTRUCTIONS.md):
security → correctness → performance → scalability → developer experience.

See [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) for contribution process
and [.github/STYLE.md](.github/STYLE.md) for design system.

---

## License

See [LICENSE](LICENSE).
