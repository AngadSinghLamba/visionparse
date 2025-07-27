import os
import streamlit as st
from pathlib import Path
from modules.file_loader import process_file
from modules.llm_helpers import summarize_text, generate_markdown
from modules.utils import save_output_files, format_download_buttons

# 📁 Setup output directories
Path("outputs/text").mkdir(parents=True, exist_ok=True)
Path("outputs/markdown").mkdir(parents=True, exist_ok=True)
Path("outputs/json").mkdir(parents=True, exist_ok=True)
Path("outputs/images").mkdir(parents=True, exist_ok=True)

# 🎨 Streamlit UI setup
st.set_page_config(page_title="VisionParse - Document & Image Intelligence", layout="wide")
st.title("📄 VisionParse - Intelligent Document Parser")

# 📌 Sidebar for OCR and LLM settings
st.sidebar.header("🔧 Settings")
ocr_engine = st.sidebar.selectbox("Choose OCR Engine", ["EasyOCR", "Tesseract"])
use_ollama = st.sidebar.checkbox("Use Ollama for Summarization", value=True)

# 📤 File uploader with support for multiple file types
uploaded_files = st.file_uploader("Upload your files", type=["pdf", "png", "jpg", "jpeg", "docx", "pptx", "csv", "xls"], accept_multiple_files=True)

# ▶️ Process each file
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.divider()
        st.subheader(f"📎 Processing: `{uploaded_file.name}`")

        # 🔍 Step 1: Extract text & images
        with st.spinner("🔍 Extracting content..."):
            extracted_text, images, metadata = process_file(uploaded_file, ocr_engine=ocr_engine)

        # 🧠 Step 2: Optional LLM summarization (Ollama/Mistral)
        if use_ollama:
            with st.spinner("🤖 Summarizing with Ollama..."):
                extracted_text = summarize_text(extracted_text)

        # 📝 Step 3: Markdown generation
        markdown_output = generate_markdown(extracted_text, metadata)

        # 💾 Step 4: Save files to disk
        base_filename = Path(uploaded_file.name).stem
        save_output_files(base_filename, extracted_text, markdown_output, metadata)

        # 📤 Step 5: Display outputs & download options
        st.markdown("### 📤 Download Outputs")
        format_download_buttons(base_filename)

        # 🖼️ Step 6: Show extracted images with captions (optional)
        if images:
            st.markdown("### 🖼️ Extracted Images")
            for idx, img_path in enumerate(images):
                st.image(img_path, caption=f"Image {idx + 1}: {Path(img_path).name}", use_column_width=True)
