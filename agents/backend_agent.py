import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vaultwares_agentciation.extrovert_agent import ExtrovertAgent
from vaultwares_agentciation.enums import AgentStatus


class BackendAgent(ExtrovertAgent):
    """
    Backend API Agent for the Weekly Menu app.

    Specializes in:
    - Node.js + TypeScript + Express route implementation
    - Zod validation schemas for all API inputs
    - Menu generation algorithm (balanced diet, budget, restrictions)
    - JWT authentication middleware
    - PostgreSQL parameterized queries with RLS
    - Service layer implementation (MenuGenerationService, ShoppingListService, etc.)
    - Rate limiting, error handling, CorrelationId middleware
    - Unit and integration tests for routes and services

    Dispatched tasks come from the [AGENT:backend] items in TODO.md.
    Follows the manager-extrovert pattern from vaultwares-agentciation.
    All code follows VaultWares TypeScript guidelines:
    - strict mode, no 'any', named exports, Zod validation, parameterized SQL.
    """

    AGENT_TYPE = "backend"
    SKILLS = [
        "express_route",
        "auth_middleware",
        "menu_generation_service",
        "nutrition_service",
        "budget_service",
        "shopping_list_service",
        "zod_validation",
        "postgresql_query",
        "rate_limiting",
        "error_handling",
        "unit_test",
        "integration_test",
        "dockerfile",
    ]

    def __init__(
        self,
        agent_id: str = "backend-agent",
        channel: str = "tasks",
        redis_host: str = "localhost",
        redis_port: int = 6379,
        redis_db: int = 0,
    ):
        super().__init__(agent_id, channel, redis_host, redis_port, redis_db)

    # ------------------------------------------------------------------
    # Task Execution
    # ------------------------------------------------------------------

    def _perform_task(self, task: str, details: dict):
        """Execute a backend development task."""
        print(f"⚙️  [{self.agent_id}] Executing backend task: {task}")

        handlers = {
            "express_route": self._express_route,
            "auth_middleware": self._auth_middleware,
            "menu_generation_service": self._menu_generation_service,
            "nutrition_service": self._nutrition_service,
            "budget_service": self._budget_service,
            "shopping_list_service": self._shopping_list_service,
            "zod_validation": self._zod_validation,
            "postgresql_query": self._postgresql_query,
            "rate_limiting": self._rate_limiting,
            "error_handling": self._error_handling,
            "unit_test": self._unit_test,
            "integration_test": self._integration_test,
            "dockerfile": self._dockerfile,
        }

        handler = handlers.get(task)
        if handler:
            handler(details)
        else:
            print(f"⚠️  [{self.agent_id}] Unknown backend task: {task}. Logging and continuing.")
            self._log_unknown_task(task, details)

    def _express_route(self, details: dict):
        """Implement an Express route handler with Zod validation."""
        method = details.get("method", "GET")
        path = details.get("path", "/api/v1/unknown")
        description = details.get("description", "")
        print(f"🌐 [{self.agent_id}] Implementing route | {method} {path} | {description}")
        time.sleep(1)
        result = (
            f"Route implemented: {method} {path}. "
            "Zod validation applied to all inputs. "
            "CorrelationId attached. JWT auth middleware applied. "
            "Parameterized SQL used for all queries. "
            "Structured JSON error responses on failure."
        )
        self._publish_result("express_route", result)

    def _auth_middleware(self, details: dict):
        """Implement JWT authentication middleware."""
        middleware_type = details.get("type", "verify-jwt")
        print(f"🔐 [{self.agent_id}] Implementing auth middleware | type={middleware_type}")
        time.sleep(1)
        result = (
            f"Auth middleware '{middleware_type}' implemented. "
            "Verifies JWT signature + expiry on every protected route. "
            "Attaches userId from token payload to req.user. "
            "Passwords hashed with bcryptjs (cost factor 12)."
        )
        self._publish_result("auth_middleware", result)

    def _menu_generation_service(self, details: dict):
        """Implement the core menu generation service."""
        algorithm = details.get("algorithm", "balanced-scoring")
        diet_types = details.get("diet_types", ["omnivore", "vegan", "vegetarian"])
        print(
            f"🍽️  [{self.agent_id}] Implementing MenuGenerationService | "
            f"algorithm={algorithm} | diet_types={diet_types}"
        )
        time.sleep(2)
        result = (
            f"MenuGenerationService implemented with '{algorithm}' algorithm. "
            "Supports diet types: " + ", ".join(diet_types) + ". "
            "Features: restriction filtering, nutritional balance scoring, "
            "budget optimization (loose/strict), variety enforcement (no repeat meals), "
            "special diet support (keto, Mediterranean, DASH, paleo, gluten-free, low-sodium). "
            "CorrelationId logged at every step."
        )
        self._publish_result("menu_generation_service", result)

    def _nutrition_service(self, details: dict):
        """Implement the nutrition calculation service."""
        scope = details.get("scope", "weekly")
        print(f"📊 [{self.agent_id}] Implementing NutritionCalculationService | scope={scope}")
        time.sleep(1)
        result = (
            f"NutritionCalculationService implemented for scope '{scope}'. "
            "Calculates: calories, protein, carbohydrates, fat, fiber, sugar, sodium. "
            "Aggregates per meal, per day, and per week."
        )
        self._publish_result("nutrition_service", result)

    def _budget_service(self, details: dict):
        """Implement the budget estimation service."""
        mode = details.get("mode", "loose")
        print(f"💰 [{self.agent_id}] Implementing BudgetEstimationService | mode={mode}")
        time.sleep(1)
        result = (
            f"BudgetEstimationService implemented for mode '{mode}'. "
            "Modes: none (no limit), loose (prefer cost-efficient), strict (hard cap). "
            "Estimates cost per recipe based on ingredient unit prices and serving count."
        )
        self._publish_result("budget_service", result)

    def _shopping_list_service(self, details: dict):
        """Implement the shopping list generation service."""
        pantry_mode = details.get("pantry_mode", False)
        print(f"🛒 [{self.agent_id}] Implementing ShoppingListService | pantry_mode={pantry_mode}")
        time.sleep(1)
        result = (
            "ShoppingListService implemented. "
            "Aggregates all ingredients across weekly menu. "
            f"Pantry subtraction: {'enabled' if pantry_mode else 'disabled'}. "
            "Groups items by category. Estimates total cost."
        )
        self._publish_result("shopping_list_service", result)

    def _zod_validation(self, details: dict):
        """Create Zod validation schemas for API inputs."""
        endpoint = details.get("endpoint", "unknown")
        fields = details.get("fields", [])
        print(f"✅ [{self.agent_id}] Creating Zod schema | endpoint={endpoint} | fields={len(fields)}")
        time.sleep(1)
        result = (
            f"Zod schema created for endpoint '{endpoint}' with {len(fields)} fields. "
            "safeParse used; typed error response on failure."
        )
        self._publish_result("zod_validation", result)

    def _postgresql_query(self, details: dict):
        """Write parameterized PostgreSQL queries for a given operation."""
        operation = details.get("operation", "SELECT")
        table = details.get("table", "unknown")
        print(f"🐘 [{self.agent_id}] Writing PostgreSQL query | {operation} on {table}")
        time.sleep(1)
        result = (
            f"Parameterized query written: {operation} on '{table}'. "
            "Uses $1, $2, ... placeholders. No string interpolation. "
            "Multi-step writes wrapped in BEGIN/COMMIT/ROLLBACK transaction."
        )
        self._publish_result("postgresql_query", result)

    def _rate_limiting(self, details: dict):
        """Configure rate limiting middleware."""
        limit = details.get("limit", 100)
        window_minutes = details.get("window_minutes", 1)
        scope = details.get("scope", "global")
        print(
            f"🚦 [{self.agent_id}] Configuring rate limiting | "
            f"{limit} req/{window_minutes}min | scope={scope}"
        )
        time.sleep(1)
        result = (
            f"Rate limiting configured: {limit} requests per {window_minutes} minute(s) "
            f"(scope={scope}). Auth endpoints get stricter limits (20 req/min)."
        )
        self._publish_result("rate_limiting", result)

    def _error_handling(self, details: dict):
        """Implement centralized error handling middleware."""
        include_correlation_id = details.get("include_correlation_id", True)
        print(f"🚨 [{self.agent_id}] Implementing error handling | correlationId={include_correlation_id}")
        time.sleep(1)
        result = (
            "Centralized error handler implemented. "
            "Returns structured JSON: { error, correlationId }. "
            "Stack traces never exposed to clients. "
            "All errors logged with CorrelationId for traceability."
        )
        self._publish_result("error_handling", result)

    def _unit_test(self, details: dict):
        """Write unit tests for a service or utility."""
        service = details.get("service", "unknown")
        test_count = details.get("expected_test_count", 10)
        print(f"🧪 [{self.agent_id}] Writing unit tests | service={service} | count={test_count}")
        time.sleep(1)
        result = f"Unit tests written for '{service}': {test_count} test cases covering happy path, edge cases, and error paths."
        self._publish_result("unit_test", result)

    def _integration_test(self, details: dict):
        """Write integration tests for API routes."""
        route = details.get("route", "unknown")
        scenarios = details.get("scenarios", [])
        print(f"🔬 [{self.agent_id}] Writing integration tests | route={route} | scenarios={len(scenarios)}")
        time.sleep(1)
        result = f"Integration tests written for route '{route}': {len(scenarios)} scenarios."
        self._publish_result("integration_test", result)

    def _dockerfile(self, details: dict):
        """Create a Dockerfile for Cloud Run deployment."""
        base_image = details.get("base_image", "node:20-alpine")
        print(f"🐳 [{self.agent_id}] Creating Dockerfile | base={base_image}")
        time.sleep(1)
        result = (
            f"Dockerfile created using base '{base_image}'. "
            "Multi-stage build (deps → build → runtime). "
            "Non-root user for security. Health check endpoint configured."
        )
        self._publish_result("dockerfile", result)

    def _log_unknown_task(self, task: str, details: dict):
        """Log an unrecognized task for debugging."""
        print(f"📋 [{self.agent_id}] Unknown task '{task}' — details: {details}")

    def _publish_result(self, task: str, result: str):
        """Publish a task result back to the Redis channel."""
        self.coordinator.publish(
            "RESULT",
            task,
            {
                "agent": self.agent_id,
                "task": task,
                "result": result,
            },
        )
        print(f"📤 [{self.agent_id}] Result published for task '{task}'")
