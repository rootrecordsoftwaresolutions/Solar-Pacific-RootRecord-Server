from reports.generator import _build_readme_sections, _render_readme


def test_build_readme_sections_formats_product_blocks():
    sections = [
        (
            "cli_daily_climate_summary_HNL",
            "Daily Climate Summary — HNL",
            "https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=HNL",
            "2026-09-25T18:15:57-10:00",
            "CLIMATE REPORT\nHONOLULU",
        )
    ]
    body = _build_readme_sections(sections)
    assert "### 1. Daily Climate Summary — HNL" in body
    assert "cli_daily_climate_summary_HNL" in body
    assert "```text" in body
    assert "CLIMATE REPORT" in body


def test_render_readme_replaces_all_placeholders():
    template = "\n".join([
        "Banner: {{README_BANNER_URL}}",
        "Conditions: {{CURRENT_CONDITIONS}}",
        "Updated: {{REPORT_UPDATED}}",
        "Count: {{REPORT_SECTION_COUNT}}",
        "Sections:",
        "{{REPORT_SECTIONS}}",
        "",
    ])
    rendered = _render_readme(
        template,
        {
            "{{README_BANNER_URL}}": "https://example.test/banner.gif",
            "{{CURRENT_CONDITIONS}}": "| Honolulu | Fair |",
            "{{REPORT_UPDATED}}": "2026-09-25T21:00:00-10:00 HST",
            "{{REPORT_SECTION_COUNT}}": "1",
            "{{REPORT_SECTIONS}}": "### 1. Example",
        },
    )
    assert "{{" not in rendered
    assert "https://example.test/banner.gif" in rendered
    assert "### 1. Example" in rendered
    assert rendered.endswith("\n")


def test_render_readme_rejects_unresolved_placeholders():
    try:
        _render_readme("# {{CURRENT_CONDITIONS}}\n", {"{{README_BANNER_URL}}": "x"})
    except RuntimeError as exc:
        assert "CURRENT_CONDITIONS" in str(exc)
    else:
        raise AssertionError("expected RuntimeError for unresolved placeholders")
