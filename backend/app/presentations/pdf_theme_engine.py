from typing import Any, Dict, Optional

class PDFThemeEngine:
    """
    Deterministic PDF theme engine.

    Provides reusable visual themes for PDF generation.
    Does not generate or render PDFs.
    """

    DEFAULT_THEMES = {
        "cognexa_aurora": {
            "theme_id": "cognexa_aurora",
            "name": "Cognexa Aurora Intelligence",
            "mode": "dark",
            "background": "#0B1020",
            "surface": "#111827",
            "primary": "#00D4FF",
            "secondary": "#7C3AED",
            "accent": "#38BDF8",
            "text": "#F8FAFC",
            "muted_text": "#94A3B8",
            "border": "#1E293B",
            "success": "#22C55E",
            "warning": "#F59E0B",
            "danger": "#EF4444",
            "font_family": "Helvetica",
            "title_size": 24,
            "heading_size": 18,
            "body_size": 11,
            "small_size": 8,
        },
        "executive_dark": {
            "theme_id": "executive_dark",
            "name": "Executive Dark",
            "mode": "dark",
            "background": "#101010",
            "surface": "#1A1A1A",
            "primary": "#FFFFFF",
            "secondary": "#A3A3A3",
            "accent": "#D4D4D4",
            "text": "#FFFFFF",
            "muted_text": "#A3A3A3",
            "border": "#333333",
            "success": "#22C55E",
            "warning": "#F59E0B",
            "danger": "#EF4444",
            "font_family": "Helvetica",
            "title_size": 24,
            "heading_size": 18,
            "body_size": 11,
            "small_size": 8,
        },
        "light_professional": {
            "theme_id": "light_professional",
            "name": "Light Professional",
            "mode": "light",
            "background": "#FFFFFF",
            "surface": "#F8FAFC",
            "primary": "#0F172A",
            "secondary": "#475569",
            "accent": "#2563EB",
            "text": "#0F172A",
            "muted_text": "#64748B",
            "border": "#CBD5E1",
            "success": "#16A34A",
            "warning": "#D97706",
            "danger": "#DC2626",
            "font_family": "Helvetica",
            "title_size": 24,
            "heading_size": 18,
            "body_size": 11,
            "small_size": 8,
        },
    }

    def __init__(
        self,
        custom_themes: Optional[
            Dict[str, Dict[str, Any]]
        ] = None,
    ):
        self.themes = dict(self.DEFAULT_THEMES)

        if custom_themes:
            self.themes.update(custom_themes)

    def get_theme(
        self,
        theme_id: str = "cognexa_aurora",
    ) -> Dict[str, Any]:

        if not theme_id:
            raise ValueError(
                "Theme ID cannot be empty."
            )

        if theme_id not in self.themes:
            raise ValueError(
                f"Unknown PDF theme: {theme_id}"
            )

        return dict(self.themes[theme_id])

    def list_themes(self):
        return list(self.themes.keys())

    def create_custom_theme(
        self,
        theme_id: str,
        name: str,
        mode: str,
        background: str,
        surface: str,
        primary: str,
        secondary: str,
        accent: str,
        text: str,
        muted_text: str,
        border: str,
        success: str = "#22C55E",
        warning: str = "#F59E0B",
        danger: str = "#EF4444",
        font_family: str = "Helvetica",
        title_size: int = 24,
        heading_size: int = 18,
        body_size: int = 11,
        small_size: int = 8,
    ) -> Dict[str, Any]:

        if not theme_id:
            raise ValueError(
                "Theme ID cannot be empty."
            )

        if not name:
            raise ValueError(
                "Theme name cannot be empty."
            )

        if mode not in {"dark", "light"}:
            raise ValueError(
                "Theme mode must be 'dark' or 'light'."
            )

        sizes = [
            title_size,
            heading_size,
            body_size,
            small_size,
        ]

        if any(size <= 0 for size in sizes):
            raise ValueError(
                "Font sizes must be greater than zero."
            )

        theme = {
            "theme_id": theme_id,
            "name": name,
            "mode": mode,
            "background": background,
            "surface": surface,
            "primary": primary,
            "secondary": secondary,
            "accent": accent,
            "text": text,
            "muted_text": muted_text,
            "border": border,
            "success": success,
            "warning": warning,
            "danger": danger,
            "font_family": font_family,
            "title_size": title_size,
            "heading_size": heading_size,
            "body_size": body_size,
            "small_size": small_size,
        }

        self.themes[theme_id] = theme

        return dict(theme)

    def validate_theme(
        self,
        theme: Dict[str, Any],
    ) -> bool:

        required_fields = {
            "theme_id",
            "name",
            "mode",
            "background",
            "surface",
            "primary",
            "secondary",
            "accent",
            "text",
            "muted_text",
            "border",
            "success",
            "warning",
            "danger",
            "font_family",
            "title_size",
            "heading_size",
            "body_size",
            "small_size",
        }

        if not required_fields.issubset(
            theme.keys()
        ):
            return False

        if theme["mode"] not in {
            "dark",
            "light",
        }:
            return False

        return all(
            isinstance(theme[field], int)
            and theme[field] > 0
            for field in (
                "title_size",
                "heading_size",
                "body_size",
                "small_size",
            )
        )

