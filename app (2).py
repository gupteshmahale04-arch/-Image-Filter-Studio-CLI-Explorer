"""
Image Filter Studio — Streamlit App
------------------------------------
A real-world UI wrapper around the IMG class: upload an image, convert it
to grayscale, preview any Matplotlib colormap as a filter, browse all
filters in a grid, and download the result.

Run with:
    streamlit run image_filter_app.py
"""

import io

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image


# ----------------------------- Core class -----------------------------
class IMG:
    def __init__(self, image_array: np.ndarray):
        self.image = image_array
        # Normalize to 0-1 float range if needed (handles 0-255 uint8 too)
        arr = self.image.astype(float)
        if arr.max() > 1.0:
            arr = arr / 255.0

        self.R = arr[:, :, 0]
        self.G = arr[:, :, 1]
        self.B = arr[:, :, 2]
        self.grayscale = 0.2989 * self.R + 0.587 * self.G + 0.114 * self.B

    def filtered_figure(self, cmap_name: str, title: str | None = None):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.imshow(self.grayscale, cmap=cmap_name)
        ax.set_title(title or cmap_name, fontsize=10)
        ax.axis("off")
        fig.tight_layout()
        return fig


# ----------------------------- Helpers -----------------------------
def fig_to_bytes(fig) -> bytes:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=200, bbox_inches="tight")
    buf.seek(0)
    return buf.getvalue()


CURATED_CMAPS = [
    "gray", "viridis", "plasma", "inferno", "magma", "cividis",
    "jet", "hot", "cool", "spring", "summer", "autumn",
    "winter", "bone", "copper", "pink", "hsv", "twilight",
    "terrain", "ocean", "cubehelix", "rainbow", "turbo", "nipy_spectral",
]


# ----------------------------- Page config -----------------------------
st.set_page_config(page_title="Image Filter Studio", page_icon="🎨", layout="wide")

st.title("🎨 Image Filter Studio")
st.caption("Upload an image, convert it to grayscale, and explore colormap filters.")

# ----------------------------- Sidebar -----------------------------
with st.sidebar:
    st.header("📤 Upload")
    uploaded_file = st.file_uploader(
        "Choose an image", type=["png", "jpg", "jpeg", "bmp", "webp"]
    )

    st.divider()
    st.header("⚙️ Mode")
    mode = st.radio(
        "What do you want to do?",
        ["Original", "Grayscale", "Single Filter", "Filter Gallery"],
        index=2,
    )

    selected_cmap = None
    batch_cmaps = None
    if mode == "Single Filter":
        selected_cmap = st.selectbox("Choose a colormap", CURATED_CMAPS, index=1)
    elif mode == "Filter Gallery":
        batch_cmaps = st.multiselect(
            "Pick colormaps to compare",
            CURATED_CMAPS,
            default=CURATED_CMAPS[:6],
        )
        cols_per_row = st.slider("Columns per row", 2, 6, 3)

# ----------------------------- Main area -----------------------------
if uploaded_file is None:
    st.info("👈 Upload an image from the sidebar to get started.")
    st.stop()

pil_img = Image.open(uploaded_file).convert("RGB")
img_array = np.array(pil_img)
img = IMG(img_array)

if mode == "Original":
    st.subheader("Original Image")
    st.image(pil_img, use_container_width=True)

elif mode == "Grayscale":
    st.subheader("Grayscale Image")
    fig = img.filtered_figure("gray", title="Grayscale")
    st.pyplot(fig, use_container_width=True)
    st.download_button(
        "⬇️ Download Grayscale PNG",
        data=fig_to_bytes(fig),
        file_name="grayscale.png",
        mime="image/png",
    )

elif mode == "Single Filter":
    st.subheader(f"Filter: {selected_cmap}")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Original**")
        st.image(pil_img, use_container_width=True)
    with col2:
        st.markdown(f"**{selected_cmap}**")
        fig = img.filtered_figure(selected_cmap)
        st.pyplot(fig, use_container_width=True)
        st.download_button(
            "⬇️ Download Filtered PNG",
            data=fig_to_bytes(fig),
            file_name=f"filtered_{selected_cmap}.png",
            mime="image/png",
        )

elif mode == "Filter Gallery":
    st.subheader("Filter Gallery")
    if not batch_cmaps:
        st.warning("Select at least one colormap from the sidebar.")
        st.stop()

    rows = (len(batch_cmaps) + cols_per_row - 1) // cols_per_row
    idx = 0
    for _ in range(rows):
        cols = st.columns(cols_per_row)
        for c in cols:
            if idx >= len(batch_cmaps):
                break
            cmap_name = batch_cmaps[idx]
            fig = img.filtered_figure(cmap_name)
            c.pyplot(fig, use_container_width=True)
            c.download_button(
                f"⬇️ {cmap_name}",
                data=fig_to_bytes(fig),
                file_name=f"filtered_{cmap_name}.png",
                mime="image/png",
                key=f"dl_{cmap_name}",
            )
            idx += 1

st.divider()
st.caption("Built with Streamlit, Matplotlib & Pillow.")