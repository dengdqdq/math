import streamlit as st
from PIL import Image
import cv2
import numpy as np




up_file = st.file_uploader("upload")
image = Image.open(up_file)
image = np.array(image)
image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
st.image(image)