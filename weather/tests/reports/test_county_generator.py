from reports.county_generator import _targets

def cfg():
    return {
        "counties": [
            {"key": "honolulu", "aliases": ["Honolulu", "Oahu"]},
            {"key": "hawaii", "aliases": ["Hawaii", "Big Island"]},
            {"key": "maui", "aliases": ["Maui"]},
            {"key": "kauai", "aliases": ["Kauai"]},
            {"key": "kalawao", "aliases": ["Kalawao"]},
        ],
        "statewide_resource_ids": ["state_report"],
        "resource_routing": {"county_patterns": {"hawaii": ["hilo"]}},
    }

def test_statewide_all():
    found, scope = _targets("state_report", "x", cfg())
    assert found == {"honolulu", "hawaii", "maui", "kauai", "kalawao"}
    assert scope == "statewide"

def test_resource_route():
    found, scope = _targets("hilo_forecast", "x", cfg())
    assert found == {"hawaii"}
    assert scope == "explicit-resource"

def test_text_route():
    found, scope = _targets("local", "Wind on Oahu", cfg())
    assert found == {"honolulu"}
    assert scope == "explicit-text"

def test_unknown_preserved():
    found, scope = _targets("unknown", "No geography here", cfg())
    assert found == {"honolulu", "hawaii", "maui", "kauai", "kalawao"}
    assert scope == "unresolved/statewide-source"
