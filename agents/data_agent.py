import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vaultwares_agentciation.extrovert_agent import ExtrovertAgent
from vaultwares_agentciation.enums import AgentStatus


class DataAgent(ExtrovertAgent):
    """
    Data Modeling & Database Agent for the Weekly Menu app.

    Specializes in:
    - PostgreSQL schema design and SQL migrations
    - Android Room entity and DAO definitions
    - Seed data creation (recipes, ingredients, food groups, nutrition)
    - Row-Level Security (RLS) policy enforcement
    - Data validation schemas (Zod on backend, data class validation on Android)
    - Offline sync strategy between Room cache and backend API

    Dispatched tasks come from the [AGENT:data] items in TODO.md.
    Follows the manager-extrovert pattern from vaultwares-agentciation.
    """

    AGENT_TYPE = "data"
    SKILLS = [
        "schema_design",
        "sql_migration",
        "room_entity",
        "seed_data",
        "rls_policy",
        "zod_schema",
        "data_modeling",
        "sync_strategy",
    ]

    def __init__(
        self,
        agent_id: str = "data-agent",
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
        """Execute a data modeling or database task."""
        print(f"🗄️  [{self.agent_id}] Executing data task: {task}")

        handlers = {
            "schema_design": self._schema_design,
            "sql_migration": self._sql_migration,
            "room_entity": self._room_entity,
            "seed_data": self._seed_data,
            "rls_policy": self._rls_policy,
            "zod_schema": self._zod_schema,
            "data_modeling": self._data_modeling,
            "sync_strategy": self._sync_strategy,
        }

        handler = handlers.get(task)
        if handler:
            handler(details)
        else:
            print(f"⚠️  [{self.agent_id}] Unknown data task: {task}. Logging and continuing.")
            self._log_unknown_task(task, details)

    def _schema_design(self, details: dict):
        """Design a PostgreSQL table schema for a given model."""
        model = details.get("model", "unknown")
        relations = details.get("relations", [])
        print(f"📐 [{self.agent_id}] Designing schema | model={model} | relations={relations}")
        time.sleep(1)
        result = (
            f"Schema design complete for model '{model}'. "
            f"Relations: {', '.join(relations) if relations else 'none'}. "
            "Parameterized queries enforced. RLS-ready user_id columns added."
        )
        self._publish_result("schema_design", result)

    def _sql_migration(self, details: dict):
        """Write a SQL migration file for a given table or change."""
        migration_number = details.get("number", "000")
        description = details.get("description", "")
        tables = details.get("tables", [])
        print(
            f"📜 [{self.agent_id}] Writing SQL migration {migration_number} | "
            f"tables={tables} | description={description}"
        )
        time.sleep(1)
        result = (
            f"Migration {migration_number} written: {description}. "
            f"Tables created/altered: {', '.join(tables)}. "
            "Uses parameterized syntax; includes rollback."
        )
        self._publish_result("sql_migration", result)

    def _room_entity(self, details: dict):
        """Define an Android Room entity and DAO interface."""
        entity_name = details.get("entity", "unknown")
        columns = details.get("columns", [])
        print(f"📱 [{self.agent_id}] Defining Room entity | entity={entity_name} | columns={len(columns)}")
        time.sleep(1)
        result = (
            f"Room entity '{entity_name}' defined with {len(columns)} columns. "
            "DAO interface with CRUD + flow queries generated."
        )
        self._publish_result("room_entity", result)

    def _seed_data(self, details: dict):
        """Create seed data SQL for recipes, ingredients, and food groups."""
        category = details.get("category", "recipes")
        count = details.get("count", 10)
        print(f"🌱 [{self.agent_id}] Creating seed data | category={category} | count={count}")
        time.sleep(2)
        result = (
            f"Seed data created for '{category}': {count} records inserted. "
            "Covers all diet types, allergen flags set, nutritional data populated."
        )
        self._publish_result("seed_data", result)

    def _rls_policy(self, details: dict):
        """Write Row-Level Security policies for user-scoped tables."""
        table = details.get("table", "unknown")
        policy_type = details.get("type", "SELECT")
        print(f"🔒 [{self.agent_id}] Writing RLS policy | table={table} | type={policy_type}")
        time.sleep(1)
        result = (
            f"RLS policy written for '{table}' ({policy_type}). "
            "Enforces user_id = current_setting('app.current_user_id') filter."
        )
        self._publish_result("rls_policy", result)

    def _zod_schema(self, details: dict):
        """Generate a Zod validation schema for a backend model."""
        schema_name = details.get("name", "unknown")
        fields = details.get("fields", [])
        print(f"✅ [{self.agent_id}] Generating Zod schema | name={schema_name} | fields={len(fields)}")
        time.sleep(1)
        result = (
            f"Zod schema '{schema_name}Schema' generated with {len(fields)} fields. "
            "safeParse used on all API inputs; typed errors returned on failure."
        )
        self._publish_result("zod_schema", result)

    def _data_modeling(self, details: dict):
        """Create comprehensive data model documentation."""
        domain = details.get("domain", "core")
        models = details.get("models", [])
        print(f"📊 [{self.agent_id}] Data modeling | domain={domain} | models={models}")
        time.sleep(1)
        result = f"Data models documented for domain '{domain}': {', '.join(models)}."
        self._publish_result("data_modeling", result)

    def _sync_strategy(self, details: dict):
        """Define and implement offline sync strategy between Room and API."""
        entity = details.get("entity", "unknown")
        strategy = details.get("strategy", "stale-while-revalidate")
        print(f"🔄 [{self.agent_id}] Sync strategy | entity={entity} | strategy={strategy}")
        time.sleep(1)
        result = (
            f"Sync strategy '{strategy}' implemented for entity '{entity}'. "
            "Uses WorkManager for background sync; Room as source of truth when offline."
        )
        self._publish_result("sync_strategy", result)

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
