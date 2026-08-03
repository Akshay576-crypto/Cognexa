from typing import Any, Dict, Optional


class ThemeEngine:
    """
    Deterministic theme specification engine.

    The Theme Engine defines the visual configuration used by
    dashboards, presentations, and reports.

    It does not render UI, charts, PPTs, or PDFs.
    """

    DEFAULT_THEMES = {
        "cognexa_aurora": {
            "name": "Cognexa Aurora Intelligence",
            "mode": "dark",
            "primary": "#00D4FF",
            "secondary": "#7C3AED",
            "accent": "#38BDF8",
            "background": "#0B1020",
            "surface": "#111827",
            "text": "#F8FAFC",
            "muted_text": "#94A3B8",
            "border": "#1E293B",
            "success": "#22C55E",
            "warning": "#F59E0B",
            "danger": "#EF4444",
        },
        "professional_light": {
            "name": "Professional Light",
            "mode": "light",
            "primary": "#2563EB",
            "secondary": "#4F46E5",
            "accent": "#0EA5E9",
            "background": "#F8FAFC",
            "surface": "#FFFFFF",
            "text": "#0F172A",
            "muted_text": "#64748B",
            "border": "#E2E8F0",
            "success": "#16A34A",
            "warning": "#D97706",
            "danger": "#DC2626",
        },
        "executive_dark": {
            "name": "Executive Dark",
            "mode": "dark",
            "primary": "#E5E7EB",
            "secondary": "#9CA3AF",
            "accent": "#60A5FA",
            "background": "#111111",
            "surface": "#1F1F1F",
            "text": "#F9FAFB",
            "muted_text": "#9CA3AF",
            "border": "#374151",
            "success": "#22C55E",
            "warning": "#F59E0B",
            "danger": "#EF4444",
        },
    }

    def get_theme(self, theme_name: str = "cognexa_aurora") -> Dict[str, Any]:
        """
        Return a predefined theme specification.
        """

        if theme_name not in self.DEFAULT_THEMES:
            raise ValueError(
                f"Unknown theme: {theme_name}. "
                f"Available themes: {list(self.DEFAULT_THEMES.keys())}"
            )

        theme = self.DEFAULT_THEMES[theme_name].copy()

        theme["theme_id"] = theme_name

        return theme

    def create_custom_theme(
        self,
        name: str,
        mode: str,
        primary: str,
        secondary: str,
        accent: str,
        background: str,
        surface: str,
        text: str,
        muted_text: str,
        border: str,
        success: str = "#22C55E",
        warning: str = "#F59E0B",
        danger: str = "#EF4444",
        theme_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a custom deterministic theme specification.
        """

        if not name:
            raise ValueError("Theme name cannot be empty.")

        if mode not in {"light", "dark"}:
            raise ValueError("Theme mode must be either 'light' or 'dark'.")

        return {
            "theme_id": theme_id or self._generate_theme_id(name),
            "name": name,
            "mode": mode,
            "primary": primary,
            "secondary": secondary,
            "accent": accent,
            "background": background,
            "surface": surface,
            "text": text,
            "muted_text": muted_text,
            "border": border,
            "success": success,
            "warning": warning,
            "danger": danger,
        }

    def _generate_theme_id(self, name: str) -> str:
        """
        Convert a theme name into a deterministic theme ID.
        """

        return (
            name.lower()
            .strip()
            .replace(" ", "_")
            .replace("-", "_")
        )