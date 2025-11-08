#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path

# CONFIG
COVER_FILES = ["cover.png", "cover2.png"]   # priority order
SCALE_RATIO = 0.50  # 60%, we can adjust later

def pick_pdf_from_current():
    pdfs = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
    if not pdfs:
        print("No PDF found in current folder.")
        raise SystemExit(1)

    print("Select a PDF:")
    for i, name in enumerate(pdfs, 1):
        print(f"{i}. {name}")

    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(pdfs):
                return pdfs[choice - 1]
        except ValueError:
            pass
        print("Invalid choice, try again.")

def find_cover_file():
    for c in COVER_FILES:
        if os.path.exists(c):
            return c
    print("No cover file found (expected cover.png or cover2.png).")
    raise SystemExit(1)

def pdf_first_page_to_image(pdf_path: str) -> Image.Image:
    # convert first page only
    pages = convert_from_path(pdf_path, first_page=1, last_page=1)
    return pages[0]  # PIL image

def place_in_center(base_img: Image.Image, overlay_img: Image.Image, scale_ratio: float) -> Image.Image:
    bw, bh = base_img.size
    # scale overlay relative to base width
    target_w = int(bw * scale_ratio)
    # keep aspect ratio
    ow, oh = overlay_img.size
    scale = target_w / ow
    target_h = int(oh * scale)

    overlay_resized = overlay_img.resize((target_w, target_h), Image.LANCZOS)

    # center position
    x = (bw - target_w) // 2
    y = (bh - target_h) // 2

    # paste – if overlay has no alpha, we just paste
    base_img.paste(overlay_resized, (x, y))
    return base_img

def main():
    pdf_name = pick_pdf_from_current()
    cover_file = find_cover_file()

    print(f"Using PDF: {pdf_name}")
    print(f"Using cover file: {cover_file}")

    # load base cover
    base = Image.open(cover_file).convert("RGB")

    # extract first page
    page_img = pdf_first_page_to_image(pdf_name).convert("RGB")

    # compose
    out_img = place_in_center(base, page_img, SCALE_RATIO)

    # output name = pdf name but .png
    out_name = Path(pdf_name).with_suffix(".png").name
    out_img.save(out_name, "PNG")
    print(f"Saved: {out_name}")

if __name__ == "__main__":
    main()

