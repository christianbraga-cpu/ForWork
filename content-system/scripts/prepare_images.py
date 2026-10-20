#!/usr/bin/env python3
"""Resize, convert to WebP and strip personal EXIF for a post's approved images.

Usage: python3 -I content-system/scripts/prepare_images.py <source_image> <output.webp> [hero|inline] ["copyright text"]
Hero: longest side 2000 px, target <= 250 KB. Inline: 1400 px, <= 150 KB.
Prints JSON with size, dimensions and the EXIF GPS/date found (for location checks) before stripping.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ExifTags

LIMITS = {"hero": (2000, 250_000), "inline": (1400, 150_000)}


def read_exif(img):
    out = {}
    exif = img.getexif()
    if not exif:
        return out
    tags = {ExifTags.TAGS.get(k, k): v for k, v in exif.items()}
    for key in ("DateTimeOriginal", "DateTime", "Copyright", "Artist", "Model"):
        if key in tags:
            out[key] = str(tags[key])
    gps = exif.get_ifd(0x8825)
    if gps:
        def dms(v, ref):
            d = float(v[0]) + float(v[1]) / 60 + float(v[2]) / 3600
            return -d if ref in ("S", "W") else d
        try:
            out["gps"] = [round(dms(gps[2], gps[1]), 6), round(dms(gps[4], gps[3]), 6)]
        except (KeyError, TypeError, ZeroDivisionError):
            pass
    return out


def main(src, dst, kind="inline", copyright_text=""):
    max_side, max_bytes = LIMITS[kind]
    img = Image.open(src)
    found = read_exif(img)
    img = img.convert("RGB")
    img.thumbnail((max_side, max_side))
    clean = Image.new("RGB", img.size)
    clean.paste(img)
    exif = Image.Exif()
    if copyright_text:
        exif[0x8298] = copyright_text  # Copyright
    quality = 85
    while True:
        clean.save(dst, "WEBP", quality=quality, method=6, exif=exif.tobytes())
        if Path(dst).stat().st_size <= max_bytes or quality <= 50:
            break
        quality -= 5
    print(json.dumps({"output": dst, "bytes": Path(dst).stat().st_size, "size": clean.size,
                      "quality": quality, "exif_found": found}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
