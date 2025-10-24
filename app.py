import streamlit as st

# Page setup
st.set_page_config(page_title="Apology Page", layout="centered")

# Title (optional - shown above HTML)
st.title("💌 Personal Apology Page")

# Read and display the HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML inside Streamlit
st.components.v1.html(html_content, height=700, scrolling=True)

st.write("---")
st.caption("Made with ❤️ using Streamlit")
