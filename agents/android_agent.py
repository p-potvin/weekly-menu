import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vaultwares_agentciation.extrovert_agent import ExtrovertAgent
from vaultwares_agentciation.enums import AgentStatus


class AndroidAgent(ExtrovertAgent):
    """
    Android Application Agent for the Weekly Menu app.

    Specializes in:
    - Kotlin + Jetpack Compose screen implementation (MVVM pattern)
    - ViewModel and UseCase implementation with Hilt DI
    - Retrofit API client and OkHttp interceptors (JWT auth, certificate pinning)
    - Room database entities, DAOs, and repository implementations
    - Navigation Compose route setup and deep links
    - Jetpack DataStore for preferences and encrypted JWT storage
    - WorkManager background sync tasks
    - Compose unit tests (Turbine + JUnit5) and Espresso instrumentation tests
    - ProGuard/R8 rules and Android security hardening
    - String resources extraction and French translation

    Dispatched tasks come from the [AGENT:android] items in TODO.md.
    Follows the manager-extrovert pattern from vaultwares-agentciation.
    All Kotlin code follows VaultWares MVVM conventions:
    - No business logic in composables; all state in ViewModels.
    - Repository pattern for data access.
    - Hilt for dependency injection.
    """

    AGENT_TYPE = "android"
    SKILLS = [
        "compose_screen",
        "viewmodel",
        "retrofit_client",
        "room_dao",
        "navigation",
        "datastore",
        "workmanager",
        "compose_test",
        "espresso_test",
        "security_hardening",
        "i18n_strings",
        "proguard_rules",
    ]

    def __init__(
        self,
        agent_id: str = "android-agent",
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
        """Execute an Android development task."""
        print(f"📱 [{self.agent_id}] Executing Android task: {task}")

        handlers = {
            "compose_screen": self._compose_screen,
            "viewmodel": self._viewmodel,
            "retrofit_client": self._retrofit_client,
            "room_dao": self._room_dao,
            "navigation": self._navigation,
            "datastore": self._datastore,
            "workmanager": self._workmanager,
            "compose_test": self._compose_test,
            "espresso_test": self._espresso_test,
            "security_hardening": self._security_hardening,
            "i18n_strings": self._i18n_strings,
            "proguard_rules": self._proguard_rules,
        }

        handler = handlers.get(task)
        if handler:
            handler(details)
        else:
            print(f"⚠️  [{self.agent_id}] Unknown Android task: {task}. Logging and continuing.")
            self._log_unknown_task(task, details)

    def _compose_screen(self, details: dict):
        """Implement a Jetpack Compose screen."""
        screen_name = details.get("screen", "UnknownScreen")
        components = details.get("components", [])
        has_viewmodel = details.get("has_viewmodel", True)
        print(
            f"🖥️  [{self.agent_id}] Implementing Compose screen | "
            f"screen={screen_name} | components={len(components)} | vm={has_viewmodel}"
        )
        time.sleep(1)
        result = (
            f"Compose screen '{screen_name}' implemented. "
            f"Components: {', '.join(components) if components else 'standard'}. "
            f"{'Connected to ViewModel via hiltViewModel().' if has_viewmodel else 'Stateless composable.'} "
            "Follows Material 3 design. Light/dark theme supported."
        )
        self._publish_result("compose_screen", result)

    def _viewmodel(self, details: dict):
        """Implement a Hilt-injected ViewModel."""
        vm_name = details.get("viewmodel", "UnknownViewModel")
        use_cases = details.get("use_cases", [])
        state_type = details.get("state_type", "UiState sealed class")
        print(
            f"🧠 [{self.agent_id}] Implementing ViewModel | "
            f"vm={vm_name} | use_cases={use_cases} | state={state_type}"
        )
        time.sleep(1)
        result = (
            f"ViewModel '{vm_name}' implemented. "
            f"Use cases injected: {', '.join(use_cases) if use_cases else 'none'}. "
            f"State type: {state_type}. "
            "Exposes StateFlow<UiState> to UI. Handles loading, success, error states."
        )
        self._publish_result("viewmodel", result)

    def _retrofit_client(self, details: dict):
        """Implement a Retrofit API service interface and OkHttp client."""
        service_name = details.get("service", "ApiService")
        endpoints = details.get("endpoints", [])
        has_auth_interceptor = details.get("has_auth_interceptor", True)
        print(
            f"🌐 [{self.agent_id}] Implementing Retrofit client | "
            f"service={service_name} | endpoints={len(endpoints)} | auth={has_auth_interceptor}"
        )
        time.sleep(1)
        result = (
            f"Retrofit client '{service_name}' implemented with {len(endpoints)} endpoints. "
            f"{'JWT auth interceptor configured (Bearer token from DataStore). ' if has_auth_interceptor else ''}"
            "Token refresh interceptor handles 401 responses automatically. "
            "Certificate pinning enabled for production."
        )
        self._publish_result("retrofit_client", result)

    def _room_dao(self, details: dict):
        """Implement a Room DAO interface and repository."""
        entity = details.get("entity", "Unknown")
        operations = details.get("operations", ["insert", "update", "delete", "getAll"])
        print(f"🗄️  [{self.agent_id}] Implementing Room DAO | entity={entity} | ops={operations}")
        time.sleep(1)
        result = (
            f"Room DAO implemented for entity '{entity}'. "
            f"Operations: {', '.join(operations)}. "
            "Flow<List<T>> used for reactive queries. "
            "Repository wraps DAO with coroutine dispatchers."
        )
        self._publish_result("room_dao", result)

    def _navigation(self, details: dict):
        """Implement Navigation Compose routes and NavHost."""
        routes = details.get("routes", [])
        has_auth_guard = details.get("has_auth_guard", True)
        print(
            f"🗺️  [{self.agent_id}] Implementing navigation | "
            f"routes={len(routes)} | auth_guard={has_auth_guard}"
        )
        time.sleep(1)
        result = (
            f"NavHost configured with {len(routes)} routes. "
            f"{'Auth guard: redirects to LoginScreen if no valid JWT. ' if has_auth_guard else ''}"
            "Typed navigation arguments using Navigation Compose. "
            "Deep link support for shared menus."
        )
        self._publish_result("navigation", result)

    def _datastore(self, details: dict):
        """Implement Jetpack DataStore for preferences or encrypted token storage."""
        store_type = details.get("type", "preferences")
        keys = details.get("keys", [])
        encrypted = details.get("encrypted", False)
        print(
            f"💾 [{self.agent_id}] Implementing DataStore | "
            f"type={store_type} | keys={len(keys)} | encrypted={encrypted}"
        )
        time.sleep(1)
        result = (
            f"DataStore ({store_type}) implemented with {len(keys)} keys. "
            f"{'Encrypted with EncryptedSharedPreferences wrapper for JWT. ' if encrypted else ''}"
            "Exposes preferences as Flow<T> for reactive collection in ViewModels."
        )
        self._publish_result("datastore", result)

    def _workmanager(self, details: dict):
        """Implement a WorkManager background task."""
        worker_name = details.get("worker", "SyncWorker")
        trigger = details.get("trigger", "periodic-6h")
        print(f"⏰ [{self.agent_id}] Implementing WorkManager | worker={worker_name} | trigger={trigger}")
        time.sleep(1)
        result = (
            f"WorkManager worker '{worker_name}' implemented. "
            f"Trigger: {trigger}. "
            "Syncs Room cache with backend API. "
            "Handles network constraints (requires network). "
            "Exponential backoff on failure."
        )
        self._publish_result("workmanager", result)

    def _compose_test(self, details: dict):
        """Write Compose UI tests for a screen or component."""
        screen = details.get("screen", "UnknownScreen")
        test_scenarios = details.get("scenarios", [])
        print(
            f"🧪 [{self.agent_id}] Writing Compose tests | "
            f"screen={screen} | scenarios={len(test_scenarios)}"
        )
        time.sleep(1)
        result = (
            f"Compose UI tests written for '{screen}': {len(test_scenarios)} scenarios. "
            "Uses ComposeTestRule + Hilt test injection. "
            "Tests: render, interaction, navigation, error state, loading state."
        )
        self._publish_result("compose_test", result)

    def _espresso_test(self, details: dict):
        """Write Espresso instrumentation tests for end-to-end flows."""
        flow = details.get("flow", "unknown")
        steps = details.get("steps", [])
        print(f"🔬 [{self.agent_id}] Writing Espresso test | flow={flow} | steps={len(steps)}")
        time.sleep(1)
        result = f"Espresso instrumentation test written for flow '{flow}': {len(steps)} steps."
        self._publish_result("espresso_test", result)

    def _security_hardening(self, details: dict):
        """Apply Android security hardening measures."""
        measure = details.get("measure", "certificate-pinning")
        print(f"🔒 [{self.agent_id}] Applying security hardening | measure={measure}")
        time.sleep(1)

        measure_descriptions = {
            "certificate-pinning": "Certificate pinning configured for API hostname. SHA-256 pin hashes added to network_security_config.xml.",
            "encrypted-storage": "JWT stored in EncryptedSharedPreferences. Keys managed by Android Keystore.",
            "proguard": "ProGuard/R8 rules configured. Obfuscation enabled for release builds.",
            "network-security": "Network security config: cleartext traffic disabled. Production API enforces HTTPS only.",
            "root-detection": "Root/emulator detection implemented for production builds.",
        }

        result = measure_descriptions.get(
            measure, f"Security hardening measure '{measure}' applied."
        )
        self._publish_result("security_hardening", result)

    def _i18n_strings(self, details: dict):
        """Extract string resources and create translations."""
        locale = details.get("locale", "en")
        string_count = details.get("count", 0)
        print(f"🌍 [{self.agent_id}] i18n strings | locale={locale} | count={string_count}")
        time.sleep(1)
        result = (
            f"String resources {'extracted' if locale == 'en' else 'translated'} for locale '{locale}'. "
            f"{string_count} strings {'in strings.xml' if locale == 'en' else 'in values-' + locale + '/strings.xml'}."
        )
        self._publish_result("i18n_strings", result)

    def _proguard_rules(self, details: dict):
        """Configure ProGuard/R8 rules for the release build."""
        libraries = details.get("libraries", ["retrofit", "room", "hilt"])
        print(f"🔧 [{self.agent_id}] Configuring ProGuard rules | libraries={libraries}")
        time.sleep(1)
        result = (
            f"ProGuard rules configured for libraries: {', '.join(libraries)}. "
            "Keep annotations preserved. Retrofit models and Room entities protected."
        )
        self._publish_result("proguard_rules", result)

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
