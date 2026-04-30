import streamlit as st

st.set_page_config(page_title="AI Notes", layout="wide")

st.title("📘 AI Unit Notes Viewer")

st.write("Select a topic to view the notes:")

# Buttons for HTML files
choice = st.radio(
    "Choose a chapter:",
    [
        "Computer Vision Class 12 – Part 1",
        "Pixel Reconstruction – Complete",
        "AI Pipeline – Study Notes"
    ]
)

# Function to read HTML file
def load_html(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

# Show HTML based on selection
if choice == "Computer Vision Class 12 – Part 1":
    html_content = load_html("computer_vision_class12_1.html")
elif choice == "Pixel Reconstruction – Complete":
    html_content = load_html("pixel_reconstruction_complete.html")
else:
    html_content = load_html("ai_pipeline_study_notes.html")

# Render the HTML
st.components.v1.html(html_content, height=900, scrolling=True)
