#!/usr/bin/env python3
"""Extract embedded base64 images from source/*.html into docs/images/."""
import base64, hashlib, io, re
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE, OUT = ROOT / "source", ROOT / "docs"
IMAGES = OUT / "images"
URI = re.compile(r"data:image/(png|jpeg|jpg|webp|gif|svg\+xml);base64,([A-Za-z0-9+/=\s]+)", re.I)
EXT = {"jpeg":"jpg", "jpg":"jpg", "png":"png", "webp":"webp", "gif":"gif", "svg+xml":"svg"}

def optimize(kind, raw):
    if kind in ("gif", "svg+xml"):
        return raw, EXT[kind]
    try:
        with Image.open(io.BytesIO(raw)) as im:
            im = ImageOps.exif_transpose(im)
            im.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
            out = io.BytesIO()
            if im.mode not in ("RGBA", "LA"):
                im = im.convert("RGB")
            im.save(out, format="WEBP", quality=82, method=6)
            if out.tell() < len(raw):
                return out.getvalue(), "webp"
    except Exception as exc:
        print("Keeping original image:", exc)
    return raw, EXT[kind]

def main():
    files = sorted(SOURCE.glob("*.html"))
    if not files:
        raise SystemExit("Upload original HTML files to source/ before running.")
    IMAGES.mkdir(parents=True, exist_ok=True)
    for src in files:
        html = src.read_text(encoding="utf-8-sig")
        count = [0]
        def replace(m):
            try:
                raw = base64.b64decode(re.sub(r"\s+", "", m.group(2)), validate=True)
            except Exception:
                return m.group(0)
            data, ext = optimize(m.group(1).lower(), raw)
            name = hashlib.sha256(data).hexdigest()[:24] + "." + ext
            target = IMAGES / name
            if not target.exists():
                target.write_bytes(data)
            count[0] += 1
            return "images/" + name
        result = URI.sub(replace, html)
        (OUT / src.name).write_text(result, encoding="utf-8")
        print(src.name, "images extracted:", count[0])
if __name__ == "__main__":
    main()
