"""
Entrypoint for the Weekly Menu VaultWares multi-agent coordination system.

Starts:
  - LonelyManager   — monitors heartbeats, enforces alignment, dispatches tasks
                      from TODO.md and ROADMAP.md
  - PlannerAgent    — architecture decisions, scaffolding, CI/CD, DevOps
  - DataAgent       — DB schema, migrations, Room entities, seed data
  - BackendAgent    — Node.js/TypeScript API routes, services, business logic
  - AndroidAgent    — Kotlin/Compose screens, ViewModels, navigation
  - UIUXAgent       — design system, component library, accessibility
  - DocAgent        — API docs, README files, architecture documentation

Usage:
    python run_coordinated_system.py

Requires:
    Redis server running on localhost:6379
    Start with: redis-server vaultwares-agentciation/redis.conf
"""

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from vaultwares_agentciation import LonelyManager
from agents.planner_agent import PlannerAgent
from agents.data_agent import DataAgent
from agents.backend_agent import BackendAgent
from agents.android_agent import AndroidAgent
from agents.uiux_agent import UIUXAgent
from agents.doc_agent import DocAgent


def alert_callback(alert: dict):
    print(f"\n🚨 [SYSTEM ALERT] {alert['message']}")


def main():
    print("=" * 60)
    print("  Weekly Menu — VaultWares Multi-Agent Coordination System")
    print("=" * 60)
    print()

    # ----------------------------------------------------------------
    # Start the Lonely Manager (monitors heartbeats, dispatches tasks)
    # Reads task queue from TODO.md and project milestones from ROADMAP.md
    # ----------------------------------------------------------------
    manager = LonelyManager(
        agent_id="lonely_manager",
        alert_callback=alert_callback,
        todo_path="TODO.md",
        roadmap_path="ROADMAP.md",
    )
    manager.start()
    print(f"✅ Manager '{manager.agent_id}' started.")

    # ----------------------------------------------------------------
    # Start the Weekly Menu specialized worker agents
    # ----------------------------------------------------------------
    planner_agent = PlannerAgent(agent_id="planner-agent")
    data_agent = DataAgent(agent_id="data-agent")
    backend_agent = BackendAgent(agent_id="backend-agent")
    android_agent = AndroidAgent(agent_id="android-agent")
    uiux_agent = UIUXAgent(agent_id="uiux-agent")
    doc_agent = DocAgent(agent_id="doc-agent")

    all_agents = (planner_agent, data_agent, backend_agent, android_agent, uiux_agent, doc_agent)
    for agent in all_agents:
        agent.start()
        print(f"✅ Agent '{agent.agent_id}' started.")

    print()
    print("--- All agents are running. Redis heartbeat active. ---")
    print("--- Press Ctrl+C to stop all agents. ---")
    print()

    # ----------------------------------------------------------------
    # Dispatch real tasks from TODO.md to the appropriate agents
    # ----------------------------------------------------------------
    time.sleep(3)
    print("\n📤 [Task Dispatch] Assigning real tasks from TODO.md to agents...\n")

    import re

    AGENT_MAP = {
        "planner": "planner-agent",
        "data": "data-agent",
        "backend": "backend-agent",
        "android": "android-agent",
        "uiux": "uiux-agent",
        "doc": "doc-agent",
    }

    def parse_todo_tasks(todo_path="TODO.md"):
        tasks = []
        with open(todo_path, encoding="utf-8") as f:
            lines = f.readlines()
        task_pattern = re.compile(r"^- \[AGENT:(?P<agent>\w+)] \[P(?P<priority>\d)] \[STATUS:(?P<status>\w+)] (?P<desc>.+)")
        for line in lines:
            m = task_pattern.match(line.strip())
            if m and m.group("status") == "TODO":
                tasks.append({
                    "agent": m.group("agent").lower(),
                    "priority": int(m.group("priority")),
                    "description": m.group("desc").strip(),
                })
        return tasks

    tasks = parse_todo_tasks("TODO.md")
    for task in tasks:
        agent_id = AGENT_MAP.get(task["agent"])
        if not agent_id:
            print(f"⚠️  Unknown agent type: {task['agent']}")
            continue
        # Use a generic task_type based on description (could be improved)
        task_type = "task"
        manager.assign_task(
            agent_id,
            task_type,
            description=task["description"],
            priority=task["priority"],
        )
        print(f"✅ Assigned to {agent_id}: {task['description']}")
    manager.assign_task(
        "backend-agent",
        "auth_middleware",
        description="Implement JWT authentication middleware — verify signature, check expiry, attach userId to req",
        type="verify-jwt",
    )
    manager.assign_task(
        "android-agent",
        "compose_screen",
        description="Implement WelcomeScreen — app logo, tagline, Login/Register buttons",
        screen="WelcomeScreen",
        components=["AppLogo", "TaglineText", "LoginButton", "RegisterButton"],
        has_viewmodel=False,
    )
    manager.assign_task(
        "uiux-agent",
        "theme_design",
        description="Design Material 3 theme with VaultWares palettes — dark skin #7 (cyan) + light skin #9 (purple)",
        theme="WeeklyMenuTheme",
        mode="both",
        skin_index=7,
    )
    manager.assign_task(
        "doc-agent",
        "openapi_spec",
        description="Generate OpenAPI 3.1 specification for all API endpoints",
        version="1.0.0",
        endpoint_count=30,
    )

    # ----------------------------------------------------------------
    # Main monitoring loop
    # ----------------------------------------------------------------
    try:
        while True:
            time.sleep(30)
            print(f"\n[{time.strftime('%H:%M:%S')}] System heartbeat — agents active:")
            for agent in all_agents:
                print(f"  - {agent.agent_id}: {agent.status.value}")
            print(f"\n{manager.get_project_status_report()}")

    except KeyboardInterrupt:
        print("\n\n--- Shutting down all agents ---")
        for agent in all_agents:
            agent.stop()
            print(f"  Stopped: {agent.agent_id}")
        manager.stop()
        print("  Stopped: lonely_manager")
        print("\nSystem shutdown complete.")


if __name__ == "__main__":
    main()

