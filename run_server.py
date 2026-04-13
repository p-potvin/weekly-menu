"""
HTTP server entrypoint for VaultWares multi-agent system (AI Toolkit Agent Inspector compatible).

Exposes the LonelyManager as an HTTP server using azure-ai-agentserver-agentframework.
"""
import os
import sys
from vaultwares_agentciation import LonelyManager
from azure.ai.agentserver.agentframework import from_agent_framework
import asyncio

def get_manager():
    return LonelyManager(
        agent_id="lonely_manager",
        todo_path="TODO.md",
        roadmap_path="ROADMAP.md",
    )

if __name__ == "__main__":
    manager = get_manager()
    agent = manager  # Expose as agent
    # Use async run for compatibility
    try:
        asyncio.run(from_agent_framework(agent).run_async())
    except KeyboardInterrupt:
        print("\nServer stopped.")
