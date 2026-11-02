import streamlit as st

st.set_page_config(
    page_title="WalkLabel",
    page_icon="🚶",
    layout="wide",
)

st.title("WalkLabel")
st.write("Extract video frames and annotate walkability indicators.")

st.page_link(
    "pages/extract_frames.py",
    label="Extract frames",
    icon="🎞️",
)

st.page_link(
    "pages/classify_frames.py",
    label="Classify frames",
    icon="🏷️",
)
