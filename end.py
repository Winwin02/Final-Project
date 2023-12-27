import streamlit as st
import os

st.markdown("<h1 style='text-align: center;'>Archmage Streamer - Chapter 1</h1> <br>", unsafe_allow_html=True)

class ImageFolderViewer:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def _get_sorted_images(self):
        files = sorted(os.listdir(self.folder_path), key=lambda x: int(x.split('.')[0]))
        return [file for file in files if file.lower().endswith((".png", ".jpg", ".jpeg"))]

    def show_images(self):
        image_files = self._get_sorted_images()
        for image_file in image_files:
            image_path = os.path.join(self.folder_path, image_file)
            st.image(image_path, use_column_width=True)

mik1 = ImageFolderViewer("chapter/solo-leveling-chapter-01")
mik1._get_sorted_images()
mik1.show_images()
