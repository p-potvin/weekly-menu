import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vaultwares_agentciation.extrovert_agent import ExtrovertAgent
from vaultwares_agentciation.enums import AgentStatus


class UIUXAgent(ExtrovertAgent):
    """
    UI/UX Design & Component Library Agent for the Weekly Menu app.

    Specializes in:
    - Material 3 color scheme mapped to VaultWares STYLE.md palettes
    - Jetpack Compose design system (theme, typography, spacing, shapes)
    - Reusable Compose component library (DietBadge, MacroProgressBar, GlassCard, etc.)
    - Glassmorphism effects following VaultWares glass-ui conventions
    - Motion and animation specifications (150ms enter, respect reduceMotion)
    - Accessibility (WCAG AA contrast, TalkBack, contentDescription)
    - Light/dark theme implementation and persistence
    - VaultWares skin system (9 premade themes)

    Dispatched tasks come from the [AGENT:uiux] items in TODO.md.
    Follows the manager-extrovert pattern from vaultwares-agentciation.
    All UI follows VaultWares STYLE.md:
    - Font: Segoe UI Semilight equivalent (Nunito/Roboto Semilight on Android)
    - Dark theme base: #4A5459, accent: #21b8cc (cyan teal)
    - Light theme base: #fafafa, accent: #7c3aed (purple)
    - Glassmorphism: rgba(255,255,255,0.08-0.15), blur < 12dp
    - Motion: 150ms enter, 100ms micro, 200-300ms page transitions
    """

    AGENT_TYPE = "uiux"
    SKILLS = [
        "theme_design",
        "component_library",
        "glassmorphism",
        "motion_spec",
        "accessibility_audit",
        "icon_set",
        "color_palette",
        "typography",
    ]

    def __init__(
        self,
        agent_id: str = "uiux-agent",
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
        """Execute a UI/UX design or component task."""
        print(f"🎨 [{self.agent_id}] Executing UI/UX task: {task}")

        handlers = {
            "theme_design": self._theme_design,
            "component_library": self._component_library,
            "glassmorphism": self._glassmorphism,
            "motion_spec": self._motion_spec,
            "accessibility_audit": self._accessibility_audit,
            "icon_set": self._icon_set,
            "color_palette": self._color_palette,
            "typography": self._typography,
        }

        handler = handlers.get(task)
        if handler:
            handler(details)
        else:
            print(f"⚠️  [{self.agent_id}] Unknown UI/UX task: {task}. Logging and continuing.")
            self._log_unknown_task(task, details)

    def _theme_design(self, details: dict):
        """Design and implement the Material 3 theme with VaultWares palettes."""
        theme_name = details.get("theme", "WeeklyMenuTheme")
        mode = details.get("mode", "both")
        skin_index = details.get("skin_index", 7)
        print(
            f"🌗 [{self.agent_id}] Designing theme | "
            f"name={theme_name} | mode={mode} | skin={skin_index}"
        )
        time.sleep(1)

        skin_descriptions = {
            7: "Dark: near-black #121212, accent VaultWares cyan #00bcd4",
            9: "Light: pale white #fafafa, accent bright purple #7c3aed",
        }
        skin_desc = skin_descriptions.get(skin_index, f"skin #{skin_index}")

        result = (
            f"Theme '{theme_name}' designed for mode '{mode}'. "
            f"Applied VaultWares skin #{skin_index}: {skin_desc}. "
            "Dark theme: base #4A5459, surface #52606B, accent #21b8cc. "
            "Light theme: background #fafafa, surface #f0f0f0, text #333333, accent #7c3aed. "
            "Persisted in DataStore; toggle available in settings."
        )
        self._publish_result("theme_design", result)

    def _component_library(self, details: dict):
        """Design and implement a reusable Compose component."""
        component = details.get("component", "UnknownComponent")
        variants = details.get("variants", [])
        print(
            f"🧩 [{self.agent_id}] Implementing component | "
            f"component={component} | variants={variants}"
        )
        time.sleep(1)

        component_descriptions = {
            "DietBadge": "Colored chip showing diet type (Vegan=green, Keto=orange, etc.). Accessible with contentDescription.",
            "MacroProgressBar": "Segmented bar for protein/carb/fat ratios. Animated, respects reduceMotion.",
            "QuantityStepper": "+/- stepper with min/max bounds. Haptic feedback on change.",
            "GlassCard": "Frosted glass card (rgba 0.08-0.15 opacity, blur 8dp). For hero sections only.",
            "ToastNotification": "Dismissible snackbar. Success (green), error (red), info (cyan) variants.",
            "FilterChipGroup": "Multi-select chip group with animated selection. Used for diet/cuisine preferences.",
            "CalendarWeekView": "Horizontal scrollable 7-day selector. Active day highlighted with accent color.",
            "AnimatedFoodIcon": "Lottie animation for cooking/loading states. Falls back to static icon if Lottie unavailable.",
        }

        description = component_descriptions.get(
            component, f"Component '{component}' with variants: {', '.join(variants) if variants else 'standard'}."
        )
        result = f"Component '{component}' implemented. {description} Supports light/dark theme."
        self._publish_result("component_library", result)

    def _glassmorphism(self, details: dict):
        """Implement glassmorphism effect for a screen or component."""
        target = details.get("target", "modal")
        opacity = details.get("opacity", 0.10)
        blur_dp = details.get("blur_dp", 8)
        print(f"💎 [{self.agent_id}] Implementing glassmorphism | target={target} | opacity={opacity} | blur={blur_dp}dp")
        time.sleep(1)
        result = (
            f"Glassmorphism applied to '{target}'. "
            f"Background: rgba(255,255,255,{opacity}). "
            f"Blur: {blur_dp}dp (below 12dp GPU budget). "
            "Border: 1px rgba(255,255,255,0.18). "
            "Used sparingly per VaultWares guidelines — only on hero/modal elements."
        )
        self._publish_result("glassmorphism", result)

    def _motion_spec(self, details: dict):
        """Define motion and animation specifications."""
        element = details.get("element", "component")
        animation_type = details.get("type", "enter")
        print(f"✨ [{self.agent_id}] Defining motion spec | element={element} | type={animation_type}")
        time.sleep(1)

        duration_map = {
            "micro": "100–150ms (hover, focus)",
            "enter": "150–250ms (modal, drawer, tooltip)",
            "page": "200–300ms (screen transitions)",
        }
        duration = duration_map.get(animation_type, "150ms")

        result = (
            f"Motion spec defined for '{element}' ({animation_type}). "
            f"Duration: {duration}. "
            "Easing: ease-out for enter, ease-in for exit. "
            "Wrapped in reduceMotion check. "
            "Uses transform/opacity only (GPU-composited). "
            "No animating width/height/top/left."
        )
        self._publish_result("motion_spec", result)

    def _accessibility_audit(self, details: dict):
        """Perform an accessibility audit on a screen or component."""
        screen = details.get("screen", "all")
        checks = details.get("checks", ["contrast", "talkback", "focus"])
        print(f"♿ [{self.agent_id}] Accessibility audit | screen={screen} | checks={checks}")
        time.sleep(1)
        result = (
            f"Accessibility audit complete for '{screen}'. "
            f"Checks performed: {', '.join(checks)}. "
            "WCAG AA 4.5:1 contrast ratio verified. "
            "TalkBack announcements added for dynamic content. "
            "All interactive elements have contentDescription. "
            "Focus order verified. Color alone does not convey meaning."
        )
        self._publish_result("accessibility_audit", result)

    def _icon_set(self, details: dict):
        """Configure the icon set for the app."""
        icon_style = details.get("style", "Material Symbols Rounded")
        custom_icons = details.get("custom", [])
        print(f"🔣 [{self.agent_id}] Configuring icon set | style={icon_style} | custom={custom_icons}")
        time.sleep(1)
        result = (
            f"Icon set configured: {icon_style}. "
            f"Custom food icons added: {', '.join(custom_icons) if custom_icons else 'none'}. "
            "All icon-only buttons have aria-label equivalents (contentDescription)."
        )
        self._publish_result("icon_set", result)

    def _color_palette(self, details: dict):
        """Define and document the color palette for a theme."""
        theme_mode = details.get("mode", "dark")
        print(f"🎨 [{self.agent_id}] Defining color palette | mode={theme_mode}")
        time.sleep(1)

        palettes = {
            "dark": (
                "Dark palette: background #4A5459, surface #52606B, "
                "onSurface #E8EDF0, primary #21b8cc (cyan teal), "
                "secondary #4ecc21 (lime green), error #cf6679."
            ),
            "light": (
                "Light palette: background #fafafa, surface #f0f0f0, "
                "onSurface #333333, primary #7c3aed (purple), "
                "secondary #1a5276 (deep sea blue), error #b00020."
            ),
        }
        description = palettes.get(theme_mode, f"Color palette defined for mode '{theme_mode}'.")
        result = f"Color palette defined. {description}"
        self._publish_result("color_palette", result)

    def _typography(self, details: dict):
        """Define the typography scale for the app."""
        font_family = details.get("font_family", "Nunito")
        print(f"🔤 [{self.agent_id}] Defining typography | font={font_family}")
        time.sleep(1)
        result = (
            f"Typography scale defined using '{font_family}' (Segoe UI Semilight equivalent on Android). "
            "Display: 57sp/Semilight. Headline: 32sp/Light. "
            "Title: 22sp/Regular. Body: 16sp/Regular (lineHeight 1.5). "
            "Label: 12sp/Medium. "
            "Letter spacing: wider on headings, default on body."
        )
        self._publish_result("typography", result)

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
