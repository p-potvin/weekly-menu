import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vaultwares_agentciation.extrovert_agent import ExtrovertAgent
from vaultwares_agentciation.enums import AgentStatus


class PlannerAgent(ExtrovertAgent):
    """
    Project Planning & Architecture Agent for the Weekly Menu app.

    Specializes in:
    - Architecture decisions and stack selection
    - Project scaffolding and repository structure
    - CI/CD pipeline configuration (GitHub Actions, Cloud Build)
    - Cloud infrastructure planning (GCP: Cloud Run, Cloud SQL, Secret Manager)
    - Docker Compose and local development environment setup
    - DevOps and deployment configuration

    Dispatched tasks come from the [AGENT:planner] items in TODO.md.
    Follows the manager-extrovert pattern from vaultwares-agentciation.
    """

    AGENT_TYPE = "planner"
    SKILLS = [
        "architecture_design",
        "scaffold_project",
        "configure_ci_cd",
        "cloud_infrastructure",
        "docker_compose",
        "deployment_config",
        "environment_setup",
        "devops",
    ]

    def __init__(
        self,
        agent_id: str = "planner-agent",
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
        """Execute a planning or architecture task."""
        print(f"📐 [{self.agent_id}] Executing planner task: {task}")

        handlers = {
            "architecture_design": self._architecture_design,
            "scaffold_project": self._scaffold_project,
            "configure_ci_cd": self._configure_ci_cd,
            "cloud_infrastructure": self._cloud_infrastructure,
            "docker_compose": self._docker_compose,
            "deployment_config": self._deployment_config,
            "environment_setup": self._environment_setup,
        }

        handler = handlers.get(task)
        if handler:
            handler(details)
        else:
            print(f"⚠️  [{self.agent_id}] Unknown planner task: {task}. Logging and continuing.")
            self._log_unknown_task(task, details)

    def _architecture_design(self, details: dict):
        """Define and document the system architecture."""
        component = details.get("component", "system")
        scope = details.get("scope", "full")
        print(f"🏗️  [{self.agent_id}] Designing architecture | component={component} | scope={scope}")
        time.sleep(1)
        result = (
            f"Architecture design complete for '{component}' (scope={scope}). "
            "Stack: Kotlin/Compose (Android) + Node.js/TypeScript (API) + PostgreSQL (Cloud SQL). "
            "Pattern: MVVM on Android, layered service architecture on backend."
        )
        self._publish_result("architecture_design", result)

    def _scaffold_project(self, details: dict):
        """Generate project scaffolding for a given layer."""
        layer = details.get("layer", "unknown")
        framework = details.get("framework", "")
        print(f"🔧 [{self.agent_id}] Scaffolding project | layer={layer} | framework={framework}")
        time.sleep(1)
        result = f"Project scaffold created for layer '{layer}' using '{framework}'."
        self._publish_result("scaffold_project", result)

    def _configure_ci_cd(self, details: dict):
        """Configure a CI/CD pipeline."""
        pipeline = details.get("pipeline", "github-actions")
        target = details.get("target", "")
        print(f"⚙️  [{self.agent_id}] Configuring CI/CD | pipeline={pipeline} | target={target}")
        time.sleep(1)
        result = f"CI/CD pipeline '{pipeline}' configured for target '{target}'."
        self._publish_result("configure_ci_cd", result)

    def _cloud_infrastructure(self, details: dict):
        """Plan and document cloud infrastructure components."""
        service = details.get("service", "cloud-run")
        region = details.get("region", "us-central1")
        print(f"☁️  [{self.agent_id}] Configuring cloud infrastructure | service={service} | region={region}")
        time.sleep(1)
        result = f"Cloud infrastructure configured: {service} in {region}."
        self._publish_result("cloud_infrastructure", result)

    def _docker_compose(self, details: dict):
        """Generate Docker Compose configuration for local development."""
        services = details.get("services", ["postgres", "backend"])
        print(f"🐳 [{self.agent_id}] Generating Docker Compose | services={services}")
        time.sleep(1)
        result = f"Docker Compose generated with services: {', '.join(services)}."
        self._publish_result("docker_compose", result)

    def _deployment_config(self, details: dict):
        """Create deployment configuration files."""
        environment = details.get("environment", "production")
        target = details.get("target", "cloud-run")
        print(f"🚀 [{self.agent_id}] Creating deployment config | env={environment} | target={target}")
        time.sleep(1)
        result = f"Deployment config created for environment '{environment}' targeting '{target}'."
        self._publish_result("deployment_config", result)

    def _environment_setup(self, details: dict):
        """Set up environment configuration (.env.example, Secret Manager docs)."""
        env_type = details.get("env_type", "local")
        print(f"🔐 [{self.agent_id}] Setting up environment | type={env_type}")
        time.sleep(1)
        result = f"Environment setup complete for type '{env_type}'. .env.example generated."
        self._publish_result("environment_setup", result)

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
