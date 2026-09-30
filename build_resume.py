import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def create_resume(output_path):
    # Letter is 612 x 792 pt
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=30,
        bottomMargin=30
    )

    PRIMARY = colors.HexColor('#0f172a')     # Dark slate
    SECONDARY = colors.HexColor('#2563eb')   # Blue
    ACCENT = colors.HexColor('#059669')      # Emerald Green for live demo
    TEXT = colors.HexColor('#334155')        # Charcoal
    LIGHT_TEXT = colors.HexColor('#64748b')  # Muted slate
    BORDER = colors.HexColor('#cbd5e1')      # Divider line

    name_style = ParagraphStyle(
        'DocName',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        textColor=PRIMARY,
        spaceAfter=3
    )

    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=SECONDARY,
        spaceAfter=5
    )

    contact_style = ParagraphStyle(
        'DocContact',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=LIGHT_TEXT,
        alignment=0
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=PRIMARY,
        spaceBefore=6,
        spaceAfter=3,
        textTransform='uppercase'
    )

    body_style = ParagraphStyle(
        'DocBody',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT
    )

    proj_title_style = ParagraphStyle(
        'ProjTitle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=PRIMARY
    )

    proj_meta_style = ParagraphStyle(
        'ProjMeta',
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        textColor=LIGHT_TEXT
    )

    proj_link_style = ParagraphStyle(
        'ProjLink',
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=SECONDARY,
        alignment=2 # Right align
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=TEXT,
        leftIndent=12,
        firstLineIndent=-10
    )

    story = []

    # Header: Name and Title
    story.append(Paragraph("GAURANG KODWANI", name_style))
    story.append(Paragraph("PYTHON BACKEND DEVELOPER", title_style))

    # Contact line with clickable links
    contact_html = (
        'Hyderabad, Sindh, Pakistan &nbsp;•&nbsp; '
        '<a href="mailto:gaurangkodwani8@gmail.com" color="#2563eb">gaurangkodwani8@gmail.com</a> &nbsp;•&nbsp; '
        '<a href="https://github.com/gaurangkodwani-svg" color="#2563eb">GitHub: gaurangkodwani-svg</a> &nbsp;•&nbsp; '
        '<a href="https://www.linkedin.com/in/gaurang-kodwani-b04777437/" color="#2563eb">LinkedIn Profile</a>'
    )
    story.append(Paragraph(contact_html, contact_style))
    story.append(Spacer(1, 5))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=2, spaceAfter=5))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading_style))
    summary_text = (
        "Professional Python Backend Developer focused on building reliable, production-ready APIs and data pipelines. "
        "Specializes in clean, testable code, scalable architectures, and automation workflows. Passionate about eliminating "
        "repetitive tasks and deploying robust, data-driven applications. Available for freelance projects."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=3, spaceAfter=3))

    # Tech Stack
    story.append(Paragraph("TECH STACK", section_heading_style))
    tech_data = [
        [
            Paragraph("<b>Languages &amp; Data Science:</b>", body_style),
            Paragraph("Python, Pandas, NumPy, Scikit-Learn", body_style)
        ],
        [
            Paragraph("<b>Backend &amp; APIs:</b>", body_style),
            Paragraph("FastAPI, REST API Design, Data Processing Pipelines, Maintainable Services", body_style)
        ],
        [
            Paragraph("<b>Testing &amp; Automation:</b>", body_style),
            Paragraph("Selenium, Automated Testing, CI/CD Integration Practices", body_style)
        ],
        [
            Paragraph("<b>Version Control &amp; Tools:</b>", body_style),
            Paragraph("Git, GitHub, SQLite, Vector Databases", body_style)
        ]
    ]
    t = Table(tech_data, colWidths=[150, 390])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=3, spaceAfter=3))

    # Featured Projects
    story.append(Paragraph("FEATURED PROJECTS", section_heading_style))

    projects = [
        {
            "name": "Budget-Buddy-AI",
            "tech": "Python, Pandas, Scikit-Learn, Groq API, FastAPI",
            "url": "https://github.com/gaurangkodwani-svg/BUDGET-BUDDY-AI",
            "live_url": "https://budget-buddy-ai.streamlit.app/",
            "desc": [
                "Engineered a personal finance dashboard analyzing 500+ bank statements with Exploratory Data Analysis (EDA) and budget tracking.",
                "Integrated ML anomaly detection (95% precision), auto-categorization, savings simulator, and Groq-powered AI financial advisor, reducing manual tracking by 70%."
            ]
        },
        {
            "name": "Vault-Guard-AI",
            "tech": "Python, Cryptography, Machine Learning",
            "url": "https://github.com/gaurangkodwani-svg/Vault-Guard-AI",
            "live_url": None,
            "desc": [
                "Built a comprehensive dual-layer security application delivering robust file and folder encryption and AI-driven password strength analysis.",
                "Implemented security anomaly detection identifying 98% of simulated unauthorized file access patterns with 5x accelerated cryptographic throughput."
            ]
        },
        {
            "name": "Job-Finder.AI",
            "tech": "Python, FastAPI, SQLite",
            "url": "https://github.com/gaurangkodwani-svg/Job-Finder.AI",
            "live_url": "https://jobfinderai-umber.vercel.app/",
            "desc": [
                "Engineered a lightweight, high-throughput AI-powered job finder backend service ensuring rapid data retrieval and structured API responses.",
                "Optimized SQLite queries and FastAPI routes to reliably process 10,000+ job listings daily with sub-200ms latency."
            ]
        },
        {
            "name": "RAG-System",
            "tech": "Python, Vector Search, LLMs",
            "url": "https://github.com/gaurangkodwani-svg/RAG-SYSTEM",
            "live_url": "https://rag-system-1.streamlit.app/",
            "desc": [
                "Created a Retrieval-Augmented Generation (RAG) system for intelligent enterprise document processing and contextual QA.",
                "Improved contextual retrieval accuracy by 40% over baseline keyword matching across 1,000+ documents with 95% relevance precision."
            ]
        }
    ]

    for p in projects:
        if p.get("live_url"):
            link_html = f'<a href="{p["live_url"]}" color="#059669"><b>Live Demo ↗</b></a> &nbsp;|&nbsp; <a href="{p["url"]}" color="#2563eb"><b>GitHub ↗</b></a>'
        else:
            link_html = f'<a href="{p["url"]}" color="#2563eb"><b>GitHub Repo ↗</b></a>'

        header_row = [
            Paragraph(f"<b>{p['name']}</b> &nbsp;<font color='#64748b' size='7.5'>| {p['tech']}</font>", proj_title_style),
            Paragraph(link_html, proj_link_style)
        ]
        pt = Table([header_row], colWidths=[360, 180])
        pt.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ]))
        story.append(pt)
        for bullet in p['desc']:
            story.append(Paragraph(f"• &nbsp;{bullet}", bullet_style))
        story.append(Spacer(1, 2))

    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=2, spaceAfter=3))

    # Education & Training
    story.append(Paragraph("EDUCATION &amp; TRAINING", section_heading_style))
    edu_data = [
        [
            Paragraph("<b>Foundation Public School</b>, Hyderabad", body_style),
            Paragraph("Cambridge O-Level Coursework", proj_meta_style)
        ],
        [
            Paragraph("<b>Gexton</b>", body_style),
            Paragraph("Python Programming Course &amp; AI Programming Course (Completed)", proj_meta_style)
        ],
        [
            Paragraph("<b>Continuous Learning</b>", body_style),
            Paragraph("Advanced backend reliability, system optimization &amp; automation pipelines", proj_meta_style)
        ]
    ]
    et = Table(edu_data, colWidths=[200, 340])
    et.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(et)
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=3, spaceAfter=3))

    # Languages
    story.append(Paragraph("LANGUAGES", section_heading_style))
    story.append(Paragraph("<b>English:</b> Professional Working Proficiency &nbsp;•&nbsp; <b>Urdu:</b> Native / Bilingual &nbsp;•&nbsp; <b>Sindhi:</b> Native / Bilingual", body_style))

    doc.build(story)

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), 'Gaurang_Kodwani_Resume.pdf')
    create_resume(out)
    print("Resume generated at:", out)
