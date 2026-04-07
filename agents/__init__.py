"""
VaultWares Agents — specialized agent implementations.

All agents inherit from ExtrovertAgent and implement domain-specific
task handling. They connect to Redis and participate in the
LonelyManager heartbeat & dispatch network.

Weekly Menu App Agents:
  - PlannerAgent  — architecture, scaffolding, CI/CD, DevOps
  - DataAgent     — database schema, migrations, Room entities, seed data
  - BackendAgent  — Node.js API routes, services, business logic, tests
  - AndroidAgent  — Kotlin/Compose screens, ViewModels, navigation, tests
  - UIUXAgent     — design system, component library, accessibility
  - DocAgent      — API docs, README files, architecture documentation

Legacy Agents (media pipeline):
  - TextAgent, ImageAgent, VideoAgent, WorkflowAgent
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.text_agent import TextAgent
from agents.image_agent import ImageAgent
from agents.video_agent import VideoAgent
from agents.workflow_agent import WorkflowAgent
from agents.planner_agent import PlannerAgent
from agents.data_agent import DataAgent
from agents.backend_agent import BackendAgent
from agents.android_agent import AndroidAgent
from agents.uiux_agent import UIUXAgent
from agents.doc_agent import DocAgent

__all__ = [
    "TextAgent",
    "ImageAgent",
    "VideoAgent",
    "WorkflowAgent",
    "PlannerAgent",
    "DataAgent",
    "BackendAgent",
    "AndroidAgent",
    "UIUXAgent",
    "DocAgent",
]
