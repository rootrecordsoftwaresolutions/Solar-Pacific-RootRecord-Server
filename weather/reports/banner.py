"""Generate the processed GOES-18 Hawaii GeoColor GIF used by the README.

This is a presentation-only processor. It reads the collected raw GIF and
writes a separate banner copy; the raw weather-data product is never modified.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageSequence

SOURCE_RELATIVE = Path(
    "cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/hi/GEOCOLOR/"
    "GOES18-HI-GEOCOLOR-600x600/GOES18-HI-GEOCOLOR-600x600_current.gif"
)
OUTPUT_RELATIVE = Path("reports/assets/GOES18-HI-GEOCOLOR-README-banner.gif")
CROP_BOX = (0, 0, 600, 584)
TARGET_SIZE = (1200, 1168)
EXPECTED_SOURCE_SIZE = (600, 600)


def generate_readme_banner(base_dir: str | Path) -> Path:
    """Create the README banner from the current raw GOES-18 GIF."""
    base = Path(base_dir)
    source = base / SOURCE_RELATIVE
    output = base.parent / OUTPUT_RELATIVE

    if not source.is_file():
        raise FileNotFoundError("GOES-18 GeoColor source GIF not found: {}".format(source))

    output.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(source) as src:
        if src.size != EXPECTED_SOURCE_SIZE:
            raise ValueError(
                "Unexpected GOES-18 GeoColor size: {} (expected {})".format(
                    src.size, EXPECTED_SOURCE_SIZE
                )
            )

        frames = []
        durations = []

        for frame in ImageSequence.Iterator(src):
            cropped = frame.copy().convert("RGBA").crop(CROP_BOX)
            resized = cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
            frames.append(
                resized.convert("P", palette=Image.Palette.ADAPTIVE, colors=256)
            )
            durations.append(frame.info.get("duration", src.info.get("duration", 80)))

        if not frames:
            raise ValueError("GOES-18 GeoColor GIF contains no frames")

        frames[0].save(
            output,
            format="GIF",
            save_all=True,
            append_images=frames[1:],
            duration=durations,
            loop=0,
            optimize=False,
            disposal=2,
        )

    if not output.is_file():
        raise RuntimeError("README banner was not created: {}".format(output))

    return output


__all__ = ["generate_readme_banner", "SOURCE_RELATIVE", "OUTPUT_RELATIVE"]
