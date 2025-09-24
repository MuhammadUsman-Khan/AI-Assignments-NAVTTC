from rembg import remove
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Image Background Remover", layout="centered")
st.title("Image Background Remover")
upload = st.file_uploader("Upload Your Image", type=["jpg", "jpeg", "png"])

if upload:
    st.write("Uploaded Image")
    image = Image.open(upload)
    st.image(image)
    output = remove(image)

    st.write("Processed Image")
    st.image(output)