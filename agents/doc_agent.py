import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vaultwares_agentciation.extrovert_agent import ExtrovertAgent
from vaultwares_agentciation.enums import AgentStatus


class DocAgent(ExtrovertAgent):
    """
    Documentation Agent for the Weekly Menu app.

    Specializes in:
    - OpenAPI/Swagger specification generation for all API endpoints
    - README files (root, backend, android, database)
    - Architecture documentation with component diagrams
    - User guides and FAQ
    - CONTRIBUTING.md additions for Weekly Menu specifics
    - Inline code documentation review (JSDoc, KDoc)

    Dispatched tasks come from the [AGENT:doc] items in TODO.md.
    Follows the manager-extrovert pattern from vaultwares-agentciation.
    Documentation follows VaultWares guidelines:
    - Clear, concise technical writing
    - Setup instructions for all environments
    - Security checklist compliance notes
    """

    AGENT_TYPE = "doc"
    SKILLS = [
        "openapi_spec",
        "readme",
        "architecture_doc",
        "user_guide",
        "contributing_guide",
        "inline_doc_review",
        "api_reference",
        "faq",
    ]

    def __init__(
        self,
        agent_id: str = "doc-agent",
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
        """Execute a documentation task."""
        print(f"📚 [{self.agent_id}] Executing doc task: {task}")

        handlers = {
            "openapi_spec": self._openapi_spec,
            "readme": self._readme,
            "architecture_doc": self._architecture_doc,
            "user_guide": self._user_guide,
            "contributing_guide": self._contributing_guide,
            "inline_doc_review": self._inline_doc_review,
            "api_reference": self._api_reference,
            "faq": self._faq,
        }

        handler = handlers.get(task)
        if handler:
            handler(details)
        else:
            print(f"⚠️  [{self.agent_id}] Unknown doc task: {task}. Logging and continuing.")
            self._log_unknown_task(task, details)

    def _openapi_spec(self, details: dict):
        """Generate an OpenAPI/Swagger specification for the API."""
        version = details.get("version", "1.0.0")
        endpoint_count = details.get("endpoint_count", 0)
        print(f"📋 [{self.agent_id}] Generating OpenAPI spec | version={version} | endpoints={endpoint_count}")
        time.sleep(1)
        result = (
            f"OpenAPI 3.1 spec generated (v{version}). "
            f"{endpoint_count} endpoints documented. "
            "Includes: request/response schemas, authentication (Bearer JWT), "
            "error codes, CorrelationId in all error responses, "
            "example payloads for menu generation, shopping list, auth."
        )
        self._publish_result("openapi_spec", result)

    def _readme(self, details: dict):
        """Write or update a README file for a project component."""
        component = details.get("component", "root")
        sections = details.get("sections", ["overview", "setup", "usage"])
        print(f"📖 [{self.agent_id}] Writing README | component={component} | sections={sections}")
        time.sleep(1)
        result = (
            f"README.md written for component '{component}'. "
            f"Sections: {', '.join(sections)}. "
            "Includes setup instructions, environment variables, build commands, "
            "and architecture overview."
        )
        self._publish_result("readme", result)

    def _architecture_doc(self, details: dict):
        """Write architecture documentation with diagrams."""
        scope = details.get("scope", "full-system")
        diagram_type = details.get("diagram", "ascii")
        print(f"🏗️  [{self.agent_id}] Writing architecture doc | scope={scope} | diagram={diagram_type}")
        time.sleep(1)
        result = (
            f"ARCHITECTURE.md written for scope '{scope}'. "
            f"Diagram type: {diagram_type}. "
            "Covers: Android MVVM layers, backend service architecture, "
            "database schema overview, API request/response flow, "
            "Redis agent coordination system."
        )
        self._publish_result("architecture_doc", result)

    def _user_guide(self, details: dict):
        """Write a user-facing guide."""
        topic = details.get("topic", "getting-started")
        locale = details.get("locale", "en")
        print(f"👤 [{self.agent_id}] Writing user guide | topic={topic} | locale={locale}")
        time.sleep(1)
        result = (
            f"User guide written for topic '{topic}' in locale '{locale}'. "
            "Topics covered: setting preferences, generating a menu, "
            "understanding diet types, using the shopping list, managing your pantry."
        )
        self._publish_result("user_guide", result)

    def _contributing_guide(self, details: dict):
        """Write or update CONTRIBUTING.md additions for this project."""
        additions = details.get("additions", [])
        print(f"🤝 [{self.agent_id}] Writing contributing guide | additions={additions}")
        time.sleep(1)
        result = (
            "CONTRIBUTING.md updated with Weekly Menu specific additions: "
            "Android build instructions, backend local dev setup, "
            "agent system extension guide, seed data contribution guide. "
            "Follows VaultWares security checklist."
        )
        self._publish_result("contributing_guide", result)

    def _inline_doc_review(self, details: dict):
        """Review and improve inline documentation in source files."""
        file_path = details.get("file", "unknown")
        doc_style = details.get("style", "kdoc")
        print(f"🔍 [{self.agent_id}] Reviewing inline docs | file={file_path} | style={doc_style}")
        time.sleep(1)
        result = (
            f"Inline doc review complete for '{file_path}' ({doc_style} style). "
            "All public functions documented. No dead code or debug comments. "
            "Complex third-party calls annotated with parameter explanations."
        )
        self._publish_result("inline_doc_review", result)

    def _api_reference(self, details: dict):
        """Generate API reference documentation for a specific endpoint group."""
        group = details.get("group", "menus")
        format_type = details.get("format", "markdown")
        print(f"📡 [{self.agent_id}] Generating API reference | group={group} | format={format_type}")
        time.sleep(1)
        result = (
            f"API reference generated for endpoint group '{group}' ({format_type}). "
            "Includes: method, path, authentication requirement, "
            "request body schema, response schema, error codes, curl examples."
        )
        self._publish_result("api_reference", result)

    def _faq(self, details: dict):
        """Write a FAQ document for common questions."""
        audience = details.get("audience", "end-user")
        question_count = details.get("question_count", 10)
        print(f"❓ [{self.agent_id}] Writing FAQ | audience={audience} | questions={question_count}")
        time.sleep(1)
        result = (
            f"FAQ written for audience '{audience}' with {question_count} Q&A pairs. "
            "Topics: diet types, budget modes, ingredient tracking, "
            "meal variety algorithm, privacy and data storage."
        )
        self._publish_result("faq", result)

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
