
from app.pdf_processor import extract_pdf_content
import pytest

def test_pdf_extraction():
    sample_text = extract_pdf_content("data/techtrix_events.pdf")
    assert len(sample_text) > 0
    assert "tech" in sample_text.lower()