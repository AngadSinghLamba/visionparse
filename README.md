# 🧠 VisionParse

**VisionParse** is a multimodal document analysis tool powered by LLMs and VLMs. It allows users to upload and parse files such as PDFs, DOCX, PPTX, CSV, XLS, PNG, and JPG. The app extracts and summarizes content including text, tables, images, and diagrams — and outputs them in `.txt`, `.md`, and `.json` formats.

---

## 🚀 Features

- 📄 **Multi-format Support**: PDF, DOCX, PPTX, CSV, XLS, PNG, JPG
- 🧠 **Local LLM with Ollama (Mistral)**: For summarization, markdown generation, prompt refinement
- 🖼️ **Vision Captioning**: Using BLIP or SmolVLM to describe images
- 🔤 **OCR Support**: Extract text from scanned documents with Tesseract or EasyOCR
- 📥 **Bulk Upload**: Upload and process multiple documents at once
- 📤 **Download Outputs**: In `.txt`, `.md`, or `.json` format per document
- 📁 **Optional Image Extraction**: Save visual elements separately for reference

---

## 🧰 Tech Stack

| Layer        | Tech / Model                |
|--------------|-----------------------------|
| Frontend     | Streamlit                   |
| Backend      | Python                      |
| OCR Engine   | Tesseract / EasyOCR         |
| Image Captioning | BLIP / SmolVLM          |
| LLM          | Ollama (Mistral)            |
| File Parsing | PyMuPDF, python-docx, python-pptx, pandas, PIL, unstructured |

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/VisionParse.git
cd VisionParse
