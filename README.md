# 📘 Cover Generator Scripts

This repository provides two Python utilities for automatically generating **custom cover images** from PDF files.  
Each script extracts the **first page** of a PDF, scales it, and overlays it onto a predefined **cover image** (e.g. `cover.png` or `cover2.png`).

---

## 🧩 Scripts Overview

### 1. `cover.py`
Interactive version — for creating a single cover.

**Features:**
- Asks you to choose a PDF from the current folder  
- Extracts the first page of the selected PDF  
- Places it in the center of a base cover image (`cover.png` by default)  
- Scales the overlay by a given ratio (default **0.5**)  
- Displays the resulting image in a Python window  
- Saves the final PNG file using the same name as the PDF (e.g. `manual.pdf` → `manual.png`)

**Example usage:**
```
python cover.py
```

**With custom options:**
```
python cover.py --cover cover2.png --ratio 0.45
```

---

### 2. `batch_cover.py`
Batch version — for processing multiple PDFs automatically.

**Features:**
- Processes **all PDFs** in a specified folder (default = current folder)  
- Uses a single base cover (`cover.png` by default)  
- Applies the same scale ratio to all  
- Saves one `.png` output per `.pdf`

**Example usage:**
```
python batch_cover.py
```

**With options:**
```
python batch_cover.py --folder ./manuals --cover cover2.png --ratio 0.55
```

---

## ⚙️ Command-Line Options

| Option | Description | Default |
|--------|--------------|----------|
| `--cover` | Path to the base cover image | `cover.png` |
| `--ratio` | Scale ratio of the inserted PDF page (0–1) | `0.5` |
| `--folder` | *(batch only)* Folder containing PDFs | `.` |

---

## 📦 Requirements

Install required Python libraries:
```
pip install pillow pdf2image matplotlib
```

### Poppler installation

`pdf2image` requires **Poppler** (for PDF rendering).  

- **Windows:**  
  Download the latest release from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/),  
  extract it, and add the `bin/` folder to your system `PATH`.

- **Linux (Debian/Ubuntu):**
  ```
  sudo apt install poppler-utils
  ```

- **macOS:**
  ```
  brew install poppler
  ```

---

## 🖼️ Output Example

If your folder contains:

```
cover.png
manual1.pdf
manual2.pdf
```

Running:
```
python batch_cover.py
```

Produces:
```
manual1.png
manual2.png
```

Each image shows the first page of the PDF centered on `cover.png`.

---

## 🧰 Notes

- The ratio defines how wide the inserted PDF page appears relative to the base cover width  
- The composition maintains the original aspect ratio of the PDF page  
- You can use any image format for the cover (PNG, JPG, etc.)  
- The scripts always output PNG files  

---

## 📄 License

MIT License © 2025 — Free for personal and commercial use.  
Attribution appreciated but not required.
