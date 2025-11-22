# 📘 Cover Generator — PDF to Custom Cover Image

This repository contains Python utilities for generating **custom cover images** from PDF files.  
The primary script (`cover.py`) now includes **smart PDF search**, **multiple library folders**, optional **preview display**, and improved scaling.

---

## 🧩 Overview

### ✔ `cover.py`
Interactive tool to generate a **single cover image** by:

- Searching PDFs in multiple predefined folders  
- Extracting the **first page** of a selected PDF  
- Scaling the PDF page and placing it centered on a base cover image  
- Saving the final output as a `.png` file  
- Optionally displaying the result with `matplotlib`

This updated script is ideal for eBay manual production, keeping your workflow extremely fast.

---

## 📂 PDF Search Behavior

The script automatically searches for PDFs inside these folders:

```
C:\Users\benoi\Downloads\ebay_manuals
C:\Users\benoi\Downloads\manuals
```

**How search works:**

1. You type part of the filename:  
   ```
   hp41
   ```
2. The script finds all matching PDFs across both folders.
3. If multiple results exist, you can choose the correct one.
4. If only one match exists, it is used automatically.

---

## 🚀 Usage

### Basic usage
```
python cover.py
```

### With custom cover image
```
python cover.py --cover cover2.png
```

### With custom scaling ratio
```
python cover.py --ratio 0.45
```

### Show the preview in a window
```
python cover.py --show
```

### Full example
```
python cover.py --cover white_cover.png --ratio 0.55 --show
```

---

## ⚙️ Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--cover` | Base cover image (PNG/JPG/etc.) | `cover.png` |
| `--ratio` | Width ratio of the PDF relative to cover (0–1) | `0.5` |
| `--show` | Display the final image using matplotlib | *off* |

---

## 🧠 How It Works (Internals)

### 1️⃣ `find_pdf()`
Searches all PDFs in the configured folders, using case-insensitive substring matching.

### 2️⃣ `pdf_first_page_to_image()`
Converts the first page of the PDF to an RGB image (via `pdf2image`).

### 3️⃣ `place_in_center()`
- Scales the PDF page to `(cover_width × ratio)`
- Preserves original PDF aspect ratio  
- Centers it perfectly on the base image

### 4️⃣ Output
For input:
```
my_manual.pdf
```
You get:
```
my_manual.png
```

---

## 📦 Installation Requirements

Install Python dependencies:

```
pip install pillow pdf2image matplotlib
```

### Poppler (REQUIRED for pdf2image)

#### Windows
Download:  
https://github.com/oschwartz10612/poppler-windows/releases/

Extract → add the `bin` folder to your PATH.

#### Linux (Debian/Ubuntu)
```
sudo apt install poppler-utils
```

#### macOS
```
brew install poppler
```

---

## 🖼 Example Workflow

If you have:

```
cover.png
HP41CX Manual.pdf
```

Run:

```
python cover.py --ratio 0.52 --show
```

Output:

```
HP41CX Manual.png
```

---

## 🧰 Notes

- You can use any image format for the cover (PNG/JPG/WebP/etc.)  
- The script **never modifies** your original cover image  
- PDF page aspect ratio is fully preserved  
- Output always uses the same name as the PDF  
- Works perfectly for eBay listings, LightScribe discs, or binder covers  

---

## 📄 License

MIT License © 2025 — free for commercial and personal use.
