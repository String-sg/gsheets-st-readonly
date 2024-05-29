# this is largely for string branding so you can ignore if you are reading for logic of gsheets read-only query
import streamlit as st

# Custom CSS to change link and header colors and use Space Grotesk and Montserrat fonts
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Space+Grotesk:wght@400;700&display=swap');

body {
    font-family: 'Montserrat', sans-serif;
}
a, h1, h2, h3, h4, h5, h6 {
    color: #75F8CC;
    font-family: 'Space Grotesk', sans-serif;
}
</style>
"""

# Display logo and custom title
def display_branding():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <img src="https://file.go.gov.sg/str-png.png" alt="Logo" style="height: 50px; margin-right: 10px;">
            <h1 style="color: #75F8CC; font-family: 'Space Grotesk', sans-serif;">Workshop Checker</h1>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <head>
            <link rel="icon" type="image/png" href="https://file.go.gov.sg/str-png.png">
        </head>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="font-family: 'Montserrat', sans-serif">
            Created for Tech Summit@SST Lab School 2024
        </div>
        """, unsafe_allow_html=True
    )