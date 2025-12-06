from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime

# Create a new Document
doc = Document()

# Set up the document
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Add header/title
title = doc.add_heading('OCS Study Abroad Data Analytics Platform', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add subtitle
subtitle = doc.add_paragraph()
subtitle_run = subtitle.add_run('Interactive Visualization Dashboard - Ready for Publication')
subtitle_run.bold = True
subtitle_run.font.size = Pt(14)
subtitle_run.font.color.rgb = RGBColor(102, 126, 234)
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add date
date_para = doc.add_paragraph()
date_run = date_para.add_run(f'Date: {datetime.now().strftime("%B %d, %Y")}')
date_run.font.size = Pt(11)
date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add spacing
doc.add_paragraph()

# Overview section
doc.add_heading('Overview', 1)
overview = doc.add_paragraph(
    'I am pleased to announce that the OCS Study Abroad data analytics platform is now complete '
    'and ready for publication. This comprehensive dashboard provides interactive visualizations '
    'of 25 years of study abroad participation data (1999-2028), offering valuable insights for '
    'strategic planning, student advising, and program development.'
)
overview.paragraph_format.line_spacing = 1.15

# Key Features section
doc.add_heading('Key Features & Deliverables', 1)

features = [
    'Interactive Dashboard with 9 comprehensive visualizations covering 9,104 student participation records',
    'Top 20 Most Popular Programs analysis across multiple time periods (5, 10, 15, and 20 years)',
    'Top 20 Study Abroad Destinations showing geographic distribution and trends',
    'Major-Specific Destination Analysis helping students choose programs aligned with their academic goals',
    'Semester Participation Trends revealing historical patterns and peak periods',
    'Fully interactive charts with zoom, filter, and download capabilities',
    'Professional styling and responsive design for all devices',
    'Automated deployment system for easy updates'
]

for feature in features:
    p = doc.add_paragraph(feature, style='List Bullet')
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)

# Data Highlights section
doc.add_heading('Data Highlights', 1)

highlights_intro = doc.add_paragraph(
    'The analysis reveals several key insights from our comprehensive dataset:'
)
highlights_intro.paragraph_format.line_spacing = 1.15

# Create a table for highlights
table = doc.add_table(rows=6, cols=2)
table.style = 'Light Grid Accent 1'

# Add data to table
data = [
    ['Total Participation Records', '9,104 students'],
    ['Date Range', '1999 - 2028'],
    ['Unique Programs', '673'],
    ['Countries Represented', '74'],
    ['Academic Majors', '73'],
    ['Top Destination', 'England (306 participants)']
]

for i, (label, value) in enumerate(data):
    row = table.rows[i]
    row.cells[0].text = label
    row.cells[1].text = value
    # Make label bold
    row.cells[0].paragraphs[0].runs[0].font.bold = True

doc.add_paragraph()

# Top Programs section
doc.add_heading('Top 5 Study Abroad Programs', 2)
top_programs = [
    'IES (137 participants)',
    'Chamber Symphony Tour (125 participants)',
    'Servicio (118 participants)',
    'Life After Mandela (97 participants)',
    'CIEE (86 participants)'
]

for program in top_programs:
    p = doc.add_paragraph(program, style='List Number')
    p.paragraph_format.line_spacing = 1.15

# Top Majors section
doc.add_heading('Top 5 Participating Majors', 2)
top_majors = [
    'Communication (1,158 participants)',
    'English (999 participants)',
    'Economics (873 participants)',
    'Psychology (494 participants)',
    'Political Science (477 participants)'
]

for major in top_majors:
    p = doc.add_paragraph(major, style='List Number')
    p.paragraph_format.line_spacing = 1.15

# Technical Implementation section
doc.add_heading('Technical Implementation', 1)
tech_para = doc.add_paragraph(
    'The platform has been developed using industry-standard data visualization tools (Plotly) '
    'and is configured for immediate deployment via GitHub Pages. All visualizations are interactive, '
    'allowing users to zoom, filter, and explore data dynamically. The system includes automated '
    'deployment workflows for seamless updates as new data becomes available.'
)
tech_para.paragraph_format.line_spacing = 1.15

# Publication Options section
doc.add_heading('Publication & Access Options', 1)

pub_intro = doc.add_paragraph(
    'The dashboard is ready for publication with multiple deployment options:'
)
pub_intro.paragraph_format.line_spacing = 1.15

pub_options = [
    'GitHub Pages (Recommended): Free hosting with automatic updates',
    'Custom University Domain: Can be integrated with DePauw\'s existing web infrastructure',
    'Password Protection: Available via Netlify if restricted access is preferred',
    'Public Access: Immediate availability for students, faculty, and prospective students'
]

for option in pub_options:
    p = doc.add_paragraph(option, style='List Bullet')
    p.paragraph_format.line_spacing = 1.15

# Repository Information
doc.add_heading('Repository Information', 1)
repo_para = doc.add_paragraph()
repo_para.add_run('GitHub Repository: ').bold = True
repo_para.add_run('https://github.com/cdoan2026/OCS-Study\n')
repo_para.add_run('Live Dashboard URL (once enabled): ').bold = True
repo_para.add_run('https://cdoan2026.github.io/OCS-Study/\n')
repo_para.add_run('Documentation: ').bold = True
repo_para.add_run('Complete deployment guide included in repository')
repo_para.paragraph_format.line_spacing = 1.15

# Next Steps section
doc.add_heading('Recommended Next Steps', 1)

next_steps = [
    'Review the interactive visualizations and dashboard design',
    'Determine preferred hosting option (GitHub Pages, university server, or alternative)',
    'Decide on access level (public vs. restricted)',
    'Approve for publication and set go-live date',
    'Plan communication strategy to students and faculty about the new resource'
]

for i, step in enumerate(next_steps, 1):
    p = doc.add_paragraph(f'{step}', style='List Number')
    p.paragraph_format.line_spacing = 1.15

# Use Cases section
doc.add_heading('Potential Use Cases', 1)

use_cases = [
    'Student Advising: Help students explore study abroad options based on their major and interests',
    'Strategic Planning: Identify trending programs and allocate resources accordingly',
    'Marketing & Recruitment: Showcase DePauw\'s robust study abroad opportunities to prospective students',
    'Program Development: Understand gaps and opportunities in current offerings',
    'Academic Integration: Facilitate discussions between academic departments and OCS',
    'Alumni Engagement: Demonstrate the scope and impact of study abroad programs'
]

for use_case in use_cases:
    p = doc.add_paragraph(use_case, style='List Bullet')
    p.paragraph_format.line_spacing = 1.15

# Closing section
doc.add_paragraph()
doc.add_paragraph()

closing = doc.add_paragraph(
    'All documentation, deployment guides, and technical resources are included in the repository. '
    'I am available to discuss the platform, demonstrate the visualizations, and assist with the '
    'publication process at your convenience.'
)
closing.paragraph_format.line_spacing = 1.15

# Signature
doc.add_paragraph()
signature = doc.add_paragraph('Best regards,')
signature.paragraph_format.line_spacing = 1.15

# Add spacing for name
doc.add_paragraph()
doc.add_paragraph()

# Footer note
doc.add_paragraph()
footer = doc.add_paragraph()
footer_run = footer.add_run(
    'Note: Complete deployment instructions and detailed documentation are available in the '
    'repository under DEPLOYMENT.md and README.md files.'
)
footer_run.font.size = Pt(9)
footer_run.font.color.rgb = RGBColor(100, 100, 100)
footer_run.italic = True

# Save the document
doc.save('OCS_Data_Analytics_Announcement.docx')

print("✅ Announcement document created successfully!")
print("📄 File saved as: OCS_Data_Analytics_Announcement.docx")
