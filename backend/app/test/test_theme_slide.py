
from app.presentations.theme_engine import (
    PresentationThemeEngine,
)


def test_default_theme():

    engine = PresentationThemeEngine()

    theme = engine.get_theme()

    assert theme["theme_id"] == "cognexa_aurora"
    assert theme["name"] == (
        "Cognexa Aurora Intelligence"
    )
    assert theme["mode"] == "dark"
    assert theme["background"] == "#0B1020"
    assert theme["primary"] == "#00D4FF"
    assert theme["font_family"] == "Aptos"

    assert engine.validate_theme(theme)

    print("\nDEFAULT PRESENTATION THEME TEST PASSED")
    print(theme)


def test_executive_theme():

    engine = PresentationThemeEngine()

    theme = engine.get_theme(
        "executive_dark"
    )

    assert theme["theme_id"] == "executive_dark"
    assert theme["mode"] == "dark"

    assert engine.validate_theme(theme)

    print("\nEXECUTIVE PRESENTATION THEME TEST PASSED")


def test_light_theme():

    engine = PresentationThemeEngine()

    theme = engine.get_theme(
        "light_professional"
    )

    assert theme["theme_id"] == (
        "light_professional"
    )
    assert theme["mode"] == "light"

    assert engine.validate_theme(theme)

    print("\nLIGHT PRESENTATION THEME TEST PASSED")


def test_custom_theme():

    engine = PresentationThemeEngine()

    theme = engine.create_custom_theme(
        theme_id="custom_test",
        name="Custom Test Theme",
        mode="dark",
        background="#101010",
        surface="#202020",
        primary="#FFFFFF",
        secondary="#AAAAAA",
        accent="#00D4FF",
        text="#FFFFFF",
        muted_text="#AAAAAA",
        border="#333333",
    )

    assert theme["theme_id"] == "custom_test"
    assert theme["name"] == "Custom Test Theme"

    retrieved = engine.get_theme(
        "custom_test"
    )

    assert retrieved["theme_id"] == "custom_test"
    assert engine.validate_theme(retrieved)

    print("\nCUSTOM PRESENTATION THEME TEST PASSED")


def test_theme_listing():

    engine = PresentationThemeEngine()

    themes = engine.list_themes()

    assert "cognexa_aurora" in themes
    assert "executive_dark" in themes
    assert "light_professional" in themes

    print("\nTHEME LIST TEST PASSED")


def test_invalid_theme():

    engine = PresentationThemeEngine()

    try:

        engine.get_theme(
            "unknown_theme"
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nTHEME VALIDATION TEST PASSED")


def test_invalid_mode():

    engine = PresentationThemeEngine()

    try:

        engine.create_custom_theme(
            theme_id="invalid",
            name="Invalid",
            mode="blue",
            background="#000000",
            surface="#111111",
            primary="#FFFFFF",
            secondary="#AAAAAA",
            accent="#00D4FF",
            text="#FFFFFF",
            muted_text="#AAAAAA",
            border="#333333",
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nMODE VALIDATION TEST PASSED")


if __name__ == "__main__":

    test_default_theme()
    test_executive_theme()
    test_light_theme()
    test_custom_theme()
    test_theme_listing()
    test_invalid_theme()
    test_invalid_mode()

    print(
        "\nALL PRESENTATION THEME ENGINE TESTS PASSED"
    )

