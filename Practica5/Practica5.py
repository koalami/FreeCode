from fpdf import FPDF, XPos, YPos

# Configuración del PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(left=20, top=20, right=20)

# ---- Estilos ----
primary_color = (0, 51, 102)  # Azul oscuro
secondary_color = (150, 150, 150)  # Gris

# Fuentes
pdf.add_font("Roboto", style="", fname="Practica5/static/Roboto-Regular.ttf")
pdf.add_font("Roboto", style="B", fname="Practica5/static/Roboto-Bold.ttf")

# ---- Encabezado ----
pdf.set_font("Roboto", "B", 24)
pdf.set_text_color(*primary_color)
pdf.cell(0, 15, "Miguel Eduardo Chaves Bejarano", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# ---- Información de contacto ----
pdf.set_font("Roboto", "", 10)
pdf.set_text_color(*secondary_color)
contact_info = [
    "Email: mcb.eduardo1996@gmail.com",
    "Teléfono: +506 8341 5266",
    "LinkedIn: linkedin.com/in/miguel-chaves-bejarano-8a38b3227",
    "Ubicación: San José, Costa Rica"
]

for item in contact_info:
    pdf.cell(0, 5, item, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(8)

# ---- Sección: Resumen ----
pdf.set_font("Roboto", "B", 12)
pdf.set_text_color(*primary_color)
pdf.cell(0, 8, "SUMMARY", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_line_width(0.5)
pdf.line(20, pdf.get_y(), 190, pdf.get_y())

pdf.set_font("Roboto", "", 10)
pdf.set_text_color(0, 0, 0)  # Negro
pdf.multi_cell(0, 6, "Electrical Engineer with experience in circuit design, maintenance, and embedded systems. Skilled in C, C++, Python, and data analysis. Proven ability in troubleshooting and innovative problem-solving in technical environments. Currently seeking to leverage skills in a professional engineering role.")
pdf.ln(5)

# ---- Sección: Experiencia Profesional ----
pdf.set_font("Roboto", "B", 12)
pdf.set_text_color(*primary_color)
pdf.cell(0, 8, "PROFESSIONAL EXPERIENCE", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.line(20, pdf.get_y(), 190, pdf.get_y())
pdf.ln(5)

experiencias = [
    {
        "empresa": "Multiservicios EILA - Electrical Maintenance Assistant",
        "fecha": "September 2024 - December 2024",
        "detalles": [
            "Conducted preventive and corrective maintenance on electrical systems\n",
            "Collaborated in inspection and repair of industrial equipment"
        ]
    },
    # ... Añadir otras experiencias con el mismo formato
]

for exp in experiencias:
    pdf.set_font("Roboto", "B", 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, exp["empresa"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Roboto", "", 9)
    pdf.set_text_color(*secondary_color)
    pdf.cell(0, 4, exp["fecha"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Roboto", "", 9)
    pdf.set_text_color(0, 0, 0)
    available_width = 160  # 210 - 20 (left) - 20 (right) - 10 (sangría)
    for detalle in exp["detalles"]:
        pdf.cell(10)
        pdf.multi_cell(available_width, 5, f"• {detalle}")
    pdf.ln(3)


# ---- Sección: Educación ----
pdf.set_font("Roboto", "B", 12)
pdf.set_text_color(*primary_color)
pdf.cell(0, 8, "EDUCATION & CERTIFICATIONS", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.line(20, pdf.get_y(), 190, pdf.get_y())
pdf.ln(5)

educacion = [
    ("Bachelor's Degree in Electrical Engineering", "Universidad de Costa Rica, October 2024"),
    ("Technical Degree in Electrotechnics", "Colegio Técnico Profesional de Heredia, 2015")
]

pdf.set_font("Roboto", "B", 10)
for item in educacion:
    pdf.cell(0, 6, item[0], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Roboto", "", 9)
    pdf.set_text_color(*secondary_color)
    pdf.cell(0, 4, item[1], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Roboto", "B", 10)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(2)

# ---- Sección: Habilidades ----
pdf.set_font("Roboto", "B", 12)
pdf.set_text_color(*primary_color)
pdf.cell(0, 8, "SKILLS", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.line(20, pdf.get_y(), 190, pdf.get_y())
pdf.ln(5)

skills = [
    "Preventive/corrective maintenance",
    "Programming: C, C++, Python, Verilog",
    "Machine Learning basics",
    "Embedded Systems (SoC)",
    "Algorithms & Data Structures",
    "Circuit Design & Analysis"
]

pdf.set_font("Roboto", "", 10)
col_width = 85
for i in range(0, len(skills), 2):
    if i+1 < len(skills):
        pdf.cell(col_width, 6, f"• {skills[i]}")
        pdf.cell(col_width, 6, f"• {skills[i+1]}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    else:
        pdf.cell(col_width, 6, f"• {skills[i]}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# ---- Guardar PDF ----
pdf.output("Miguel_Chaves_Resume_Redesign.pdf")