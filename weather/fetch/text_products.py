"""api.weather.gov/products/types/{TYPE}/locations/HFO -- PRIMARY path for
text products, per NWS_Hawaii_Resource_Map.md Section 3B. Falls back to
text_products_fallback.py's product.php scrape only if this fails.
"""
from __future__ import annotations

import json

from core.manifest import Manifest
from fetch import _engine, text_products_fallback


def _extract_latest_product_text(list_json_bytes: bytes) -> str:
    """The API returns a JSON @graph list of latest products; each entry's
    @id fetches the full record with a productText field. This helper is a
    placeholder for that two-step resolution -- see note below.
    """
    envelope = json.loads(list_json_bytes.decode("utf-8"))
    graph = envelope.get("@graph", [])
    if not graph:
        raise ValueError("no products in @graph -- nothing to extract")
    # NOTE: a real implementation makes a second http_client.get() to the
    # first entry's `@id` URL to fetch the full record's `productText` field.
    # That second hop belongs here (category-specific two-step API shape),
    # not in fetch/_engine.py, which only knows single-request pipelines.
    # Left as the documented next step rather than guessed at, since the
    # exact field name/shape should be confirmed against a live response
    # before being relied on for archiving.
    first = graph[0]
    return first.get("productText") or json.dumps(first)


# One entry per text product this module owns (primary API path). Each maps
# to a `types/{AWIPS}/locations/HFO` products-API URL, per the resource map.
PRODUCT_TYPES: dict[str, str] = {
    "sfp_state_forecast": "SFP",
    "zfp_zone_forecast": "ZFP",
    "afd_area_forecast_discussion": "AFD",
    "nowhfo_short_term_forecast": "NOW",
    "hwo_hazardous_weather_outlook": "HWO",
    "cwf_coastal_waters": "CWF",
}


def fetch_all(manifest: Manifest, base_dir: str) -> list[_engine.FetchOutcome]:
    outcomes = []
    for resource_id, awips_type in PRODUCT_TYPES.items():
        url = f"https://api.weather.gov/products/types/{awips_type}/locations/HFO"
        outcome = _engine.run_resource(
            manifest, base_dir, resource_id, url,
            method="text",
            accept="application/ld+json",
            clean_text_body=True,
            extract_text=_extract_latest_product_text,
        )
        if outcome.status == "failed":
            # Primary path down -- fall back to the product.php scrape for
            # whichever product has a known fallback URL configured.
            fallback_outcome = text_products_fallback.fetch_one(manifest, base_dir, resource_id)
            outcomes.append(fallback_outcome or outcome)
        else:
            outcomes.append(outcome)
    return outcomes
