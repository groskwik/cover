#!/usr/bin/env python3
import os
import argparse
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------
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

def pdf_first_page_to_image(pdf_path: str) -> Image.Image:
    pages = convert_from_path(pdf_path, first_page=1, last_page=1)
    return pages[0]

def place_in_center(base_img: Image.Image, overlay_img: Image.Image, scale_ratio: float) -> Image.Image:
    bw, bh = base_img.size
    ow, oh = overlay_img.size

    target_w = int(bw * scale_ratio)
    scale = target_w / ow
    target_h = int(oh * scale)

    overlay_resized = overlay_img.resize((target_w, target_h), Image.LANCZOS)
    x = (bw - target_w) // 2
    y = (bh - target_h) // 2

    base_img.paste(overlay_resized, (x, y))
    return base_img

# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Overlay first page of a PDF onto a cover image.")
    parser.add_argument("--ratio", type=float, default=0.5, help="Scale ratio (default = 0.5)")
    parser.add_argument("--cover", type=str, default="cover.png", help="Cover image file (default = cover.png)")
    args = parser.parse_args()

    pdf_name = pick_pdf_from_current()

    if not os.path.exists(args.cover):
        print(f"Cover file '{args.cover}' not found.")
        raise SystemExit(1)

    print(f"Using PDF: {pdf_name}")
    print(f"Using cover file: {args.cover}")
    print(f"Scale ratio: {args.ratio}")

    base = Image.open(args.cover).convert("RGB")
    page_img = pdf_first_page_to_image(pdf_name).convert("RGB")
    out_img = place_in_center(base, page_img, args.ratio)

    out_name = Path(pdf_name).with_suffix(".png").name
    out_img.save(out_name, "PNG")

    print(f"Saved: {out_name}")

    # show image inside Python
    plt.imshow(out_img)
    plt.axis("off")
    plt.title(f"{out_name} (ratio={args.ratio})")
    plt.show()

if __name__ == "__main__":
    main()
