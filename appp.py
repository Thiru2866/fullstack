import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Student Task Dashboard",
    layout="wide"
)

html_path = Path("index.html")

if html_path.exists():
    st.components.v1.html(
        html_path.read_text(encoding="utf-8"),
        height=900,
        scrolling=True
    )
else:
    st.error("index.html not found")
