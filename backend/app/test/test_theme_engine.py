from app.visualization.theme_engine import ThemeEngine


def test_default_theme():

    engine = ThemeEngine()

    theme = engine.get_theme()

    assert theme["theme_id"] == "cognexa_aurora"
    assert theme["name"] == "Cognexa Aurora Intelligence"
    assert theme["mode"] == "dark"

    assert "primary" in theme
    assert "secondary" in theme
    assert "accent" in theme
    assert "background" in theme
    assert "surface" in theme
    assert "text" in theme
    assert "muted_text" in theme
    assert "border" in theme

    print("\nDEFAULT THEME TEST PASSED")
    print(theme)


def test_professional_light_theme():

    engine = ThemeEngine()

    theme = engine.get_theme("professional_light")

    assert theme["theme_id"] == "professional_light"
    assert theme["name"] == "Professional Light"
    assert theme["mode"] == "light"

    print("\nLIGHT THEME TEST PASSED")


def test_executive_dark_theme():

    engine = ThemeEngine()

    theme = engine.get_theme("executive_dark")

    assert theme["theme_id"] == "executive_dark"
    assert theme["mode"] == "dark"

    print("\nEXECUTIVE THEME TEST PASSED")


def test_custom_theme():

    engine = ThemeEngine()

    theme = engine.create_custom_theme(
        name="Market Intelligence",
        mode="dark",
        primary="#00D4FF",
        secondary="#7C3AED",
        accent="#38BDF8",
        background="#0B1020",
        surface="#111827",
        text="#F8FAFC",
        muted_text="#94A3B8",
        border="#1E293B",
    )

    assert theme["theme_id"] == "market_intelligence"
    assert theme["name"] == "Market Intelligence"
    assert theme["mode"] == "dark"
    assert theme["primary"] == "#00D4FF"

    print("\nCUSTOM THEME TEST PASSED")


def test_invalid_theme():

    engine = ThemeEngine()

    try:
        engine.get_theme("does_not_exist")
        assert False, "Expected ValueError"

    except ValueError:
        pass

    try:
        engine.create_custom_theme(
            name="Invalid Theme",
            mode="neon",
            primary="#000000",
            secondary="#000000",
            accent="#000000",
            background="#000000",
            surface="#000000",
            text="#FFFFFF",
            muted_text="#AAAAAA",
            border="#333333",
        )

        assert False, "Expected ValueError"

    except ValueError:
        pass

    print("\nVALIDATION TEST PASSED")


if __name__ == "__main__":

    test_default_theme()
    test_professional_light_theme()
    test_executive_dark_theme()
    test_custom_theme()
    test_invalid_theme()

    print("\nALL THEME ENGINE TESTS PASSED")