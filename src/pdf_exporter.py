"""
pdf_exporter.py – Xuất báo cáo Markdown thành PDF (Hỗ trợ tiếng Việt)
Sử dụng ReportLab — thư viện tạo PDF ổn định nhất cho Python.
"""

import re
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Đăng ký font hỗ trợ tiếng Việt ──────────────────────
_font_registered = False

def _register_fonts():
    """Đăng ký font hỗ trợ Unicode (DejaVuSans có sẵn trong reportlab)."""
    global _font_registered
    if _font_registered:
        return
    
    import os
    
    # Thử dùng font hệ thống Windows trước, fallback về DejaVuSans
    fonts_to_try = [
        # (family_name, regular_path, bold_path)
        ("VNFont",
         os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'arial.ttf'),
         os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'arialbd.ttf')),
    ]
    
    for family, regular, bold in fonts_to_try:
        if os.path.exists(regular):
            try:
                pdfmetrics.registerFont(TTFont(family, regular))
                if os.path.exists(bold):
                    pdfmetrics.registerFont(TTFont(f"{family}-Bold", bold))
                _font_registered = True
                return
            except Exception:
                continue
    
    # Fallback: không cần đăng ký thêm, dùng Helvetica mặc định
    _font_registered = True


def _strip_emoji(text: str) -> str:
    """Loại bỏ emoji và ký tự ngoài BMP."""
    text = re.sub(r'[\U00010000-\U0010FFFF]', '', text)
    text = text.replace('\ufe0f', '')
    bmp_symbols = ['\u2695', '\u26a0', '\u2705', '\u274c', '\u2b07',
                   '\u23f3', '\u23f9', '\u2b50']
    for s in bmp_symbols:
        text = text.replace(s, '')
    return text


def _get_styles():
    """Tạo bộ style cho PDF."""
    _register_fonts()
    
    # Kiểm tra font nào đã đăng ký
    font_name = "VNFont"
    font_bold = "VNFont-Bold"
    try:
        pdfmetrics.getFont(font_name)
    except KeyError:
        font_name = "Helvetica"
        font_bold = "Helvetica-Bold"
    
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        'VNTitle',
        parent=styles['Title'],
        fontName=font_bold,
        fontSize=16,
        textColor=HexColor('#0f172a'),
        spaceAfter=8,
        alignment=TA_LEFT,
    ))
    
    styles.add(ParagraphStyle(
        'VNHeading2',
        parent=styles['Heading2'],
        fontName=font_bold,
        fontSize=13,
        textColor=HexColor('#1e3a5f'),
        spaceBefore=14,
        spaceAfter=6,
    ))
    
    styles.add(ParagraphStyle(
        'VNHeading3',
        parent=styles['Heading3'],
        fontName=font_bold,
        fontSize=12,
        textColor=HexColor('#334155'),
        spaceBefore=10,
        spaceAfter=4,
    ))
    
    styles.add(ParagraphStyle(
        'VNBody',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=10,
        leading=14,
        spaceAfter=4,
    ))
    
    styles.add(ParagraphStyle(
        'VNBullet',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=10,
        leading=14,
        leftIndent=20,
        spaceAfter=2,
    ))
    
    return styles


def _escape_html(text: str) -> str:
    """Escape các ký tự HTML đặc biệt, giữ lại tag <b> <i>."""
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    # Khôi phục tag bold/italic
    text = text.replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    text = text.replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>')
    return text


def markdown_to_pdf_bytes(md_text: str, title: str = "Báo Cáo Y Tế") -> bytes:
    """
    Chuyển Markdown text thành mảng bytes PDF.
    Sử dụng ReportLab với font hỗ trợ Unicode tiếng Việt.
    """
    md_text = _strip_emoji(md_text)
    styles = _get_styles()
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )
    
    story = []
    lines = md_text.split('\n')
    current_text = ""
    
    def flush_text():
        nonlocal current_text
        if current_text.strip():
            # Chuyển bold markdown ** thành HTML <b>
            text = current_text.strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
            text = text.replace('\n', '<br/>')
            text = _escape_html(text)
            try:
                story.append(Paragraph(text, styles['VNBody']))
            except Exception:
                # Nếu Paragraph lỗi, thử plain text
                safe = text.encode('ascii', errors='replace').decode('ascii')
                story.append(Paragraph(safe, styles['VNBody']))
        current_text = ""
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            flush_text()
            story.append(Spacer(1, 4))
            continue
        
        if stripped == '---':
            flush_text()
            story.append(HRFlowable(
                width="100%", thickness=0.5,
                color=HexColor('#cbd5e1'),
                spaceBefore=6, spaceAfter=6
            ))
            continue
        
        if stripped.startswith('# '):
            flush_text()
            title_text = stripped[2:].replace('**', '').strip()
            title_text = re.sub(r'[^\w\s\-–—:()&]', '', title_text).strip()
            title_text = _escape_html(title_text)
            story.append(Paragraph(title_text, styles['VNTitle']))
            story.append(HRFlowable(
                width="100%", thickness=1.5,
                color=HexColor('#0284c7'),
                spaceBefore=2, spaceAfter=8
            ))
        
        elif stripped.startswith('### '):
            flush_text()
            h3 = stripped[4:].replace('**', '').strip()
            h3 = _escape_html(h3)
            story.append(Paragraph(h3, styles['VNHeading3']))
        
        elif stripped.startswith('## '):
            flush_text()
            h2 = stripped[3:].replace('**', '').strip()
            h2 = _escape_html(h2)
            story.append(Paragraph(h2, styles['VNHeading2']))
        
        elif stripped.startswith('*   ') or stripped.startswith('- '):
            flush_text()
            item = stripped.lstrip('*- ').strip()
            item = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', item)
            item = _escape_html(item)
            story.append(Paragraph(f"• {item}", styles['VNBullet']))
        
        else:
            # Loại bỏ markdown formatting và tích lũy text
            line_clean = stripped.replace('**', '').replace('__', '')
            current_text += line_clean + "\n"
    
    flush_text()
    
    doc.build(story)
    return buffer.getvalue()
