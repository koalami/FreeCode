from fpdf import FPDF, XPos, YPos


# Configuración ATS con Roboto
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(left=15, top=15, right=15)  # Márgenes reducidos

# Fuentes
pdf.add_font("Roboto", style="", fname="Practica5/static/Roboto-Regular.ttf")
pdf.add_font("Roboto", style="B", fname="Practica5/static/Roboto-Bold.ttf")

# ---- Estilo optimizado ----
line_height = 6
ancho_util = 180  # 210 - 15*2 márgenes
section_spacing = 8  # Variable faltante añadida
# ---- Encabezado ----
pdf.set_font("Roboto", "B", 18)
pdf.cell(0, 10, "Miguel Eduardo Chaves Bejarano", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(section_spacing)

# ---- Sección: Summary ----
pdf.set_font("Roboto", "B", 12)
pdf.cell(ancho_util, line_height, "SUMMARY", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Roboto", "", 11)
pdf.multi_cell(ancho_util, line_height, "Electrical Engineer with experience in circuit design, maintenance, and embedded systems. Skilled in C, C++, Python, and data analysis. Proven ability in troubleshooting and innovative problem-solving in technical environments. Currently seeking to leverage skills in a professional engineering role.")
pdf.ln(section_spacing)

# ---- Experiencia Profesional ----
pdf.set_font("Roboto", "B", 12)
pdf.cell(ancho_util, line_height, "PROFESSIONAL EXPERIENCE", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

experiencias = [
    {
        "empresa": "Multiservicios EILA - Electrical Maintenance Assistant",
        "fecha": "September 2024 - December 2024",
        "detalles": [
            "Conduct preventive and corrective maintenance on electrical systems\n",
            "Collaborate in the inspection and repair of industrial equipment"
        ]
    },
    {
        "empresa": "Instituto Costarricense de Electricidad - Cybersecurity Research Intern",
        "fecha": "March 2023 - May 2023",
        "detalles": [
            "Analyzed vulnerabilities in electric vehicle charging networks\n",
            "Delivered actionable recommendations to mitigate cybersecurity risks"
        ]
    }
]

for exp in experiencias:
    pdf.ln(4)
    # Empresa
    pdf.set_font("Roboto", "B", 11)
    pdf.multi_cell(ancho_util, line_height, exp["empresa"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    # Fecha (alineación precisa)
    pdf.set_font("Roboto", "", 10)
    pdf.cell(ancho_util, line_height, exp["fecha"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    # Detalles
    pdf.set_x(25)  # Resetear posición X al margen izquierdo + 10
    for detalle in exp["detalles"]:
        pdf.multi_cell(ancho_util - 10, line_height, f"- {detalle}") 
    pdf.ln(2)

# ---- Educación ----
pdf.ln(section_spacing)
pdf.set_font("Roboto", "B", 12)
pdf.cell(ancho_util, line_height, "EDUCATION & CERTIFICATIONS", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

educacion = [
    "Bachelor's Degree in Electrical Engineering - Universidad de Costa Rica, October 2024\n",
    "Technical Degree in Electrotechnics - Colegio Técnico Profesional de Heredia, 2015"
]

for item in educacion:
    pdf.set_x(25)  # Posición inicial
    pdf.set_font("Roboto", "", 11)
    pdf.multi_cell(ancho_util, line_height, f"- {item}")

# ---- Habilidades ----
pdf.ln(section_spacing)
pdf.set_font("Roboto", "B", 12)
pdf.cell(ancho_util, line_height, "SKILLS", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

skills = [
    "Preventive and corrective maintenance",
    "Programming Languages: C, C++, Python, Verilog",
    "Machine Learning: Basic knowledge and practical application",
    "Embedded Systems Development (SoC)",
    "Proficiency in algorithms and data structures",
    "Circuit Design and Electrical System Analysis"
]

pdf.set_x(25)  # Alineación consistente
for skill in skills:
    pdf.multi_cell(ancho_util, line_height, f"- {skill}")

# ---- Contacto al final ----
pdf.ln(section_spacing * 2)
pdf.set_font("Roboto", "B", 12)
pdf.cell(ancho_util, line_height, "CONTACT INFORMATION", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Roboto", "", 11)
contacto = [
    "mob.eduardo1996@gmail.com",
    "+506 8341 5266",
    "www.linkedin.com/in/miguel-chaves-bejarano-8a38b3227"
]

for item in contacto:
    pdf.cell(ancho_util, line_height, item, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# ---- Información adicional ----
pdf.ln(section_spacing)
pdf.set_font("Roboto", "", 10)
pdf.cell(ancho_util, line_height, "Additional information: Driving Licence B1 | Able for immediate incorporation | First Aid Workshop", align="C")

# ---- Generar PDF ----
pdf.output("CV_Final_Corregido.pdf")