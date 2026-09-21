
# 🎨 Image Filter Studio & CLI Explorer

A Python-based image filtering application that transforms images into grayscale and maps Matplotlib colormaps as visual filters. The project provides both a command-line interface (CLI) and an interactive web dashboard built with Streamlit.

---

## 📋 Table of Contents
* [Overview](#-overview)
* [Key Features](#-key-features)
* [How It Works (RGB to Grayscale)](#-how-it-works-rgb-to-grayscale)
* [Installation & Setup](#-installation--setup)
* [Usage](#-usage)
  * [1. Streamlit Web Interface](#1-streamlit-web-interface)
  * [2. Command Line Interface (CLI)](#2-command-line-interface-cli)
* [Supported Colormaps & Filters](#-supported-colormaps--filters)
* [Project File Directory](#-project-file-directory)

---

## 🔍 Overview
**Image Filter Studio** takes standard color images, separates their underlying red, green, and blue color channels, and converts them to luminance-based grayscale. From there, users can dynamically apply any Matplotlib colormap (such as `viridis`, `plasma`, `inferno`, or `coolwarm`) to false-color the image and export high-resolution results.

---

## ✨ Key Features
* **RGB Channel Separation:** Splits raw image arrays into isolated R, G, and B matrices.
* **Luminosity Grayscale Conversion:** Standard weighted formula ensures balanced perceived brightness.
* **Interactive UI (Streamlit):** Web app featuring side-by-side comparisons, responsive gallery grids, and instant PNG downloads.
* **Terminal CLI:** Standalone menu-driven Python script for quick local operations and batch filter previews.
* **Batch Previews:** View dozens of Matplotlib colormaps simultaneously in responsive subplots.

---

## 🧠 How It Works (RGB to Grayscale)

A digital image consists of a 3D matrix `[height, width, channels]` where the third dimension contains the Red, Green, and Blue intensity channels.

To convert a color image into accurate grayscale, human eye sensitivity to colors must be accounted for (the human eye is most sensitive to green, moderately to red, and least to blue). The project applies standard ITU-R luminosity weights:

$$\text{Grayscale} = 0.2989 \times R + 0.5870 \times G + 0.1140 \times B$$

```python
# Channel separation and grayscale calculation
self.R = arr[:, :, 0]
self.G = arr[:, :, 1]
self.B = arr[:, :, 2]
self.grayscale = 0.2989 * self.R + 0.587 * self.G + 0.114 * self.B

```

Once reduced to a 2D grayscale matrix, any colormap maps brightness values (0.0 to 1.0) to a distinct gradient palette.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/image-filter-studio.git](https://github.com/your-username/image-filter-studio.git)
cd image-filter-studio

```


2. **Install dependencies:**
Ensure you have Python installed, then install the required packages using the provided `requirements.txt`:
```bash
pip install -r requirements.txt

```


*Required libraries: `streamlit`, `matplotlib`, `numpy`, `Pillow*`

---

## 🖥️ Usage

### 1. Streamlit Web Interface

Run the Streamlit application to open the browser dashboard:

```bash
streamlit run "app (2).py"

```

#### Application Modes:

* **Original:** Preview the uploaded image in its natural RGB format.
* **Grayscale:** View and download the pure black-and-white luminosity representation.
* **Single Filter:** Compare the original and filtered image side-by-side using any curated colormap.
* **Filter Gallery:** Compare multiple colormaps simultaneously across configurable columns per row, each with its own download button.

---

### 2. Command Line Interface (CLI)

Run the menu-driven script directly in the terminal:

```bash
python Img_project.py

```

```text
----- Image Filter Menu -----
1. Show Original Image
2. Show Grayscale Image
3. Apply Specific Filter
4. Show All Filters (Batch)
0. Exit

```

---

## 🎨 Supported Colormaps & Filters

The Streamlit UI provides a curated list of popular filters, while the CLI supports every colormap registered in Matplotlib:

| Category | Filter Names |
| --- | --- |
| **Perceptually Uniform** | `viridis`, `plasma`, `inferno`, `magma`, `cividis` |
| **Sequential** | `gray`, `bone`, `copper`, `pink`, `hot` |
| **Diverging & Cycles** | `coolwarm`, `twilight`, `hsv` |
| **Stylistic & Themes** | `ocean`, `terrain`, `rainbow`, `turbo`, `spring`, `summer`, `autumn`, `winter` |

---

## 📂 Project File Directory

* **`app (2).py`**: Streamlit web application providing image uploads, UI layout modes, Matplotlib figure rendering, and PNG download triggers.
* **`Img_project.py`**: Command-line interface program implementing the core `IMG` class with interactive CLI options and batch subplot previews.
* **`requirements.txt`**: Package dependencies list (`streamlit`, `matplotlib`, `numpy`, `Pillow`).
