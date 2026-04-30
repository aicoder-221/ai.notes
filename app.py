import streamlit as st

st.set_page_config(page_title="AI Notes Viewer", layout="wide")

st.title("📘 AI Notes Viewer")

# --- Function to load HTML ---
def load_html(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

# --- Sidebar Navigation ---
st.sidebar.title("Chapters")
choice = st.sidebar.radio(
    "Select a chapter:",
    [
        "Computer Vision - Part 1",
        "Pixel Reconstruction - Complete"
    ]
)

# --- Display content ---
if choice == "Computer Vision - Part 1":
    html_content = load_html("computer_vision_class12_1.html")
else:
    html_content = load_html("pixel_reconstruction_complete.html")

# Render HTML content
st.components.v1.html(html_content, height=1000, scrolling=True)
