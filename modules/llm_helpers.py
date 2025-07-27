"""
llm_helpers.py
---------------
This module handles LLM-based summarization, prompt generation, and markdown formatting.
Currently uses Ollama (locally running Mistral) to avoid API costs.

Functions:
- summarize_text(text): Summarizes long extracted text using Mistral via Ollama.
- generate_markdown(text, metadata): Converts final output to structured Markdown.
- generate_prompts(text): (Optional) Generate enhanced system prompts for downstream LLMs.
"""

import subprocess
import json

# 🧠 Function to run Mistral via Ollama for summarization
def summarize_text(text):
    """
    Sends text to the local Ollama (Mistral model) and returns a summary.
    """
    prompt = f"Summarize the following document content in concise paragraphs:\n\n{text[:3000]}"
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        return result.stdout.strip() or text
    except Exception as e:
        return f"[Summarization Error]: {e}"

# 📘 Function to format final output as Markdown
def generate_markdown(text, metadata):
    """
    Generates Markdown text including metadata and body content.
    
    Parameters:
    - text: Extracted (and possibly summarized) content
    - metadata: Dictionary with file info, caption info, etc.
    
    Returns:
    - Markdown-formatted string
    """
    md = f"# 📄 Parsed Document\n\n"
    md += f"**Filename:** `{metadata.get('filename', 'unknown')}`\n\n"
    
    if 'captions' in metadata:
        md += "## 🖼️ Image Captions\n"
        for fname, cap in metadata['captions'].items():
            md += f"- **{fname}**: {cap}\n"
        md += "\n"

    md += "## 📑 Content\n"
    md += text
    return md

# ⚙️ Optional: Generate refined prompts for downstream agents
def generate_prompts(text):
    """
    Returns a set of refined system prompts to use with LLMs.
    Can be used for downstream agents (e.g., summarization, categorization, tagging).
    """
    return [
        f"Summarize this text: {text[:1000]}",
        f"Generate 5 key points: {text[:1000]}",
        f"Extract all tables and explain briefly.",
        f"Tag the sections by type (intro, data, conclusion).",
        f"Detect key terms and glossary items."
    ]
