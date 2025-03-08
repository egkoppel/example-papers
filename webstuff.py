import streamlit as st
import base64

def get_pdf_html(file_path, page=1):
    # Read the PDF file in binary mode
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Embed the PDF in an iframe with the page parameter
    pdf_html = f'''
        <iframe src="data:application/pdf;base64,{base64_pdf}#page={page}"
                width="100%" height="900" type="application/pdf">
        </iframe>
    '''
    return pdf_html

# Create two columns: one for text and one for the PDF
col1, col2 = st.columns([1, 3])

with col1:
    st.header("Instructions")
    st.write("""
    *Welcome to the PDF Viewer!*

    - This sidebar provides useful information about the document.
    - Use the controls on the right to navigate the PDF.
    - The PDF opens on a specific page as defined by the URL fragment.
    """)

with col2:
    pdf_html = get_pdf_html("L24fullnotesp2.pdf", page=3)
    st.markdown(pdf_html, unsafe_allow_html=True)

import streamlit as st
import base64

def get_pdf_html(file_path, page=1):
    # Read the PDF file in binary mode
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Embed the PDF in an iframe with the page parameter
    pdf_html = f'''
        <iframe src="data:application/pdf;base64,{base64_pdf}#page={page}"
                width="100%" height="900" type="application/pdf">
        </iframe>
    '''
    return pdf_html

# Create two columns: one for text and video, and one for the PDF
col1, col2 = st.columns([1, 3])

with col1:
    st.header("Instructions & Video")
    st.write("""
    **Welcome to the PDF Viewer!**

    - Use this sidebar to review instructions.
    - Below, you can also watch a helpful video.
    - The PDF on the right opens at the specified page.
    """)
    # Embed the video file (ensure 'hi.mp4' is in the same directory)
    st.video("hi.mp4")

with col2:
    pdf_html = get_pdf_html("L24fullnotesp2.pdf", page=3)
    st.markdown(pdf_html, unsafe_allow_html=True)
