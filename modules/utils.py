"""
utils.py
--------
Shared utility functions to:
- Save extracted content in .txt, .md, and .json formats
- Display download buttons in Streamlit
"""

import os
import json
import streamlit as st

# 📁 Create output directories if they don’t exist
os.makedirs("outputs/text", exist_ok=True)
os.makedirs("outputs/markdown", exist_ok=True)
os.makedirs("outputs/json", exist_ok=True)

def save_output_files(base_filename, raw_text, markdown_output, metadata):
    """
    Saves extracted text, markdown, and metadata JSON to disk.

    Parameters:
    - base_filename: stem name (without extension)
    - raw_text: final extracted or summarized text
    - markdown_output: formatted markdown string
    - metadata: dict containing file metadata and image captions
    """
    txt_path = f"outputs/text/{base_filename}.txt"
    md_path = f"outputs/markdown/{base_filename}.md"
    json_path = f"outputs/json/{base_filename}.json"

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(raw_text)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_output)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

def format_download_buttons(base_filename):
    """
    Creates Streamlit download buttons for .txt, .md, and .json outputs.
    """
    txt_path = f"outputs/text/{base_filename}.txt"
    md_path = f"outputs/markdown/{base_filename}.md"
    json_path = f"outputs/json/{base_filename}.json"

    with open(txt_path, "r", encoding="utf-8") as f:
        st.download_button("⬇️ Download .txt", f.read(), file_name=f"{base_filename}.txt")

    with open(md_path, "r", encoding="utf-8") as f:
        st.download_button("⬇️ Download .md", f.read(), file_name=f"{base_filename}.md")

    with open(json_path, "r", encoding="utf-8") as f:
        st.download_button("⬇️ Download .json", f.read(), file_name=f"{base_filename}.json")
