from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_supplier_report_pdf(response, suppliers):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Fornecedores")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 14)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Fornecedores")

    table_top_y = height - 100
    row_height = 20
    col_widths = [40, 100, 140, 110, 110]

    headers = ["ID", "Nome", "Descrição", "Criado em", "Modificado em"]
    x_positions = [50, 90, 190, 330, 440]

    pdf_canvas.setFont("Helvetica-Bold", 10)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 15, header)
        pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 10)

    for supplier in suppliers:
        pdf_canvas.drawString(x_positions[0] + 5, y - 15, str(supplier.id))
        pdf_canvas.drawString(x_positions[1] + 5, y - 15, supplier.name)
        pdf_canvas.drawString(x_positions[2] + 5, y - 15, supplier.description)

        created_at = supplier.created_at.strftime("%d/%m/%Y %H:%M") if supplier.created_at else "-"
        updated_at = supplier.updated_at.strftime("%d/%m/%Y %H:%M") if supplier.updated_at else "-"
        pdf_canvas.drawString(x_positions[3] + 5, y - 15, created_at)
        pdf_canvas.drawString(x_positions[4] + 5, y - 15, updated_at)

        for i in range(len(headers)):
            pdf_canvas.rect(x_positions[i], y - row_height, col_widths[i], row_height)

        y -= row_height

        if y < 50:
            pdf_canvas.showPage()
            y = height - 100

    pdf_canvas.save()


def generate_brand_report_pdf(response, brands):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Marcas")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 14)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Marcas")

    table_top_y = height - 100
    row_height = 20
    col_widths = [40, 100, 140, 110, 110]

    headers = ["ID", "Nome", "Descrição", "Criado em", "Modificado em"]
    x_positions = [50, 90, 190, 330, 440]

    pdf_canvas.setFont("Helvetica-Bold", 10)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 15, header)
        pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 10)

    for brand in brands:
        pdf_canvas.drawString(x_positions[0] + 5, y - 15, str(brand.id))
        pdf_canvas.drawString(x_positions[1] + 5, y - 15, brand.name)
        pdf_canvas.drawString(x_positions[2] + 5, y - 15, brand.description)

        created_at = brand.created_at.strftime("%d/%m/%Y %H:%M") if brand.created_at else "-"
        updated_at = brand.updated_at.strftime("%d/%m/%Y %H:%M") if brand.updated_at else "-"
        pdf_canvas.drawString(x_positions[3] + 5, y - 15, created_at)
        pdf_canvas.drawString(x_positions[4] + 5, y - 15, updated_at)

        for i in range(len(headers)):
            pdf_canvas.rect(x_positions[i], y - row_height, col_widths[i], row_height)

        y -= row_height

        if y < 50:
            pdf_canvas.showPage()
            y = height - 100

    pdf_canvas.save()


def generate_category_report_pdf(response, categories):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Categorias")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 14)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Categorias")

    table_top_y = height - 100
    row_height = 20
    col_widths = [40, 100, 140, 110, 110]
    headers = ["ID", "Nome", "Descrição", "Criado em", "Modificado em"]
    x_positions = [50, 90, 190, 330, 440]

    pdf_canvas.setFont("Helvetica-Bold", 10)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 15, header)
        pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 10)

    for category in categories:
        pdf_canvas.drawString(x_positions[0] + 5, y - 15, str(category.id))
        pdf_canvas.drawString(x_positions[1] + 5, y - 15, category.name)
        pdf_canvas.drawString(x_positions[2] + 5, y - 15, category.description)

        created_at = category.created_at.strftime("%d/%m/%Y %H:%M") if category.created_at else "-"
        updated_at = category.updated_at.strftime("%d/%m/%Y %H:%M") if category.updated_at else "-"
        pdf_canvas.drawString(x_positions[3] + 5, y - 15, created_at)
        pdf_canvas.drawString(x_positions[4] + 5, y - 15, updated_at)

        for i in range(len(headers)):
            pdf_canvas.rect(x_positions[i], y - row_height, col_widths[i], row_height)

        y -= row_height

        if y < 50:
            pdf_canvas.showPage()
            y = height - 100

    pdf_canvas.save()


def generate_inflow_report_pdf(response, inflows):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Entradas")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Entradas")

    table_top_y = height - 80
    row_height = 15
    col_widths = [30, 80, 80, 30, 120, 80, 80]
    headers = ["ID", "Fornecedor", "Produto", "Qtd.", "Descrição", "Criado em", "Modificado em"]
    x_positions = [40, 70, 150, 230, 260, 380, 460]

    pdf_canvas.setFont("Helvetica-Bold", 8)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 10, header)
        pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 7)

    for inflow in inflows:
        pdf_canvas.drawString(x_positions[0] + 5, y - 10, str(inflow.id))
        pdf_canvas.drawString(x_positions[1] + 5, y - 10, inflow.supplier.name[:12])
        pdf_canvas.drawString(x_positions[2] + 5, y - 10, inflow.product.title[:12])
        pdf_canvas.drawString(x_positions[3] + 5, y - 10, str(inflow.quantity))
        pdf_canvas.drawString(x_positions[4] + 5, y - 10, (inflow.description[:18] + '...') if inflow.description and len(inflow.description) > 18 else inflow.description or "-")

        created_at = inflow.created_at.strftime("%d/%m/%Y") if inflow.created_at else "-"
        updated_at = inflow.updated_at.strftime("%d/%m/%Y") if inflow.updated_at else "-"
        pdf_canvas.drawString(x_positions[5] + 5, y - 10, created_at)
        pdf_canvas.drawString(x_positions[6] + 5, y - 10, updated_at)

        for i in range(len(headers)):
            pdf_canvas.rect(x_positions[i], y - row_height, col_widths[i], row_height)

        y -= row_height

        if y < 40:
            pdf_canvas.showPage()
            y = height - 80
            pdf_canvas.setFont("Helvetica-Bold", 8)
            for i, header in enumerate(headers):
                pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 10, header)
                pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)
            pdf_canvas.setFont("Helvetica", 7)

    pdf_canvas.save()


def generate_outflow_report_pdf(response, outflows):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Saídas")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Saídas")

    table_top_y = height - 80
    row_height = 15
    col_widths = [40, 140, 40, 140, 80]
    headers = ["ID", "Produto", "Qtd.", "Descrição", "Criado em"]
    x_positions = [40, 80, 220, 260, 400]

    pdf_canvas.setFont("Helvetica-Bold", 8)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 10, header)
        pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 7)

    for outflow in outflows:
        pdf_canvas.drawString(x_positions[0] + 5, y - 10, str(outflow.id))
        pdf_canvas.drawString(x_positions[1] + 5, y - 10, outflow.product.title[:18])
        pdf_canvas.drawString(x_positions[2] + 5, y - 10, str(outflow.quantity))
        pdf_canvas.drawString(x_positions[3] + 5, y - 10, (outflow.description[:18] + '...') if outflow.description and len(outflow.description) > 18 else outflow.description or "-")
        created_at = outflow.created_at.strftime("%d/%m/%Y") if outflow.created_at else "-"
        pdf_canvas.drawString(x_positions[4] + 5, y - 10, created_at)

        for i in range(len(headers)):
            pdf_canvas.rect(x_positions[i], y - row_height, col_widths[i], row_height)

        y -= row_height

        if y < 40:
            pdf_canvas.showPage()
            y = height - 80
            pdf_canvas.setFont("Helvetica-Bold", 8)
            for i, header in enumerate(headers):
                pdf_canvas.drawString(x_positions[i] + 5, table_top_y - 10, header)
                pdf_canvas.rect(x_positions[i], table_top_y - row_height, col_widths[i], row_height)
            pdf_canvas.setFont("Helvetica", 7)

    pdf_canvas.save()


def generate_user_report_pdf(response, users):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Usuários")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Usuários")

    table_top_y = height - 90
    row_height = 18
    col_widths = [40, 100, 150, 120, 100]
    headers = ["ID", "Nome de Usuário", "Nome Completo", "Email", "CPF"]

    pdf_canvas.setFont("Helvetica-Bold", 7)
    x_position = 40
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_position + 3, table_top_y - 12, header)
        pdf_canvas.rect(x_position, table_top_y - row_height, col_widths[i], row_height)
        x_position += col_widths[i]

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 7)

    for user in users:
        x_position = 40

        pdf_canvas.drawString(x_position + 3, y - 12, str(user.id))
        x_position += col_widths[0]
        pdf_canvas.drawString(x_position + 3, y - 12, user.username[:15])
        x_position += col_widths[1]
        pdf_canvas.drawString(x_position + 3, y - 12, user.full_name[:20])
        x_position += col_widths[2]
        pdf_canvas.drawString(x_position + 3, y - 12, user.email[:25])
        x_position += col_widths[3]
        pdf_canvas.drawString(x_position + 3, y - 12, user.cpf[:11])

        x_position = 40
        for i in range(len(headers)):
            pdf_canvas.rect(x_position, y - row_height, col_widths[i], row_height)
            x_position += col_widths[i]

        y -= row_height

        if y < 50:
            pdf_canvas.showPage()
            y = height - 90

            pdf_canvas.setFont("Helvetica-Bold", 7)
            x_position = 40
            for i, header in enumerate(headers):
                pdf_canvas.drawString(x_position + 3, table_top_y - 12, header)
                pdf_canvas.rect(x_position, table_top_y - row_height, col_widths[i], row_height)
                x_position += col_widths[i]
            pdf_canvas.setFont("Helvetica", 7)

    pdf_canvas.save()


def generate_product_report_pdf(response, products):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório de Produtos")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório de Produtos")

    table_top_y = height - 90
    row_height = 16

    col_widths = [25, 70, 70, 70, 60, 60, 90, 40]
    headers = ["ID", "Título", "Categoria", "Marca", "Custo", "Venda", "Número de Série", "Qtd"]

    x_position = 40
    pdf_canvas.setFont("Helvetica-Bold", 8)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_position + 2, table_top_y - 10, header)
        pdf_canvas.rect(x_position, table_top_y - row_height, col_widths[i], row_height)
        x_position += col_widths[i]

    y = table_top_y - row_height
    pdf_canvas.setFont("Helvetica", 8)

    for product in products:
        x_position = 40

        pdf_canvas.drawString(x_position + 2, y - 10, str(product.id))
        x_position += col_widths[0]
        pdf_canvas.drawString(x_position + 2, y - 10, str(product.title)[:10])
        x_position += col_widths[1]
        pdf_canvas.drawString(x_position + 2, y - 10, str(product.category.name)[:10])
        x_position += col_widths[2]
        pdf_canvas.drawString(x_position + 2, y - 10, str(product.brand.name)[:10])
        x_position += col_widths[3]
        pdf_canvas.drawString(x_position + 2, y - 10, f"R$ {product.cost_price:.2f}")
        x_position += col_widths[4]
        pdf_canvas.drawString(x_position + 2, y - 10, f"R$ {product.selling_price:.2f}")
        x_position += col_widths[5]
        pdf_canvas.drawString(x_position + 2, y - 10, str(product.serie_number)[:12])
        x_position += col_widths[6]
        pdf_canvas.drawString(x_position + 2, y - 10, str(product.quantity))

        x_position = 40
        for i in range(len(headers)):
            pdf_canvas.rect(x_position, y - row_height, col_widths[i], row_height)
            x_position += col_widths[i]

        y -= row_height

        if y < 50:
            pdf_canvas.showPage()
            y = height - 90

            pdf_canvas.setFont("Helvetica-Bold", 8)
            x_position = 40
            for i, header in enumerate(headers):
                pdf_canvas.drawString(x_position + 2, table_top_y - 10, header)
                pdf_canvas.rect(x_position, table_top_y - row_height, col_widths[i], row_height)
                x_position += col_widths[i]
            pdf_canvas.setFont("Helvetica", 8)

    pdf_canvas.save()


def generate_totality_report_pdf(response, totalities):
    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.setTitle("Relatório Geral")
    width, height = A4

    pdf_canvas.setFont("Helvetica-Bold", 14)
    pdf_canvas.drawString(40, height - 50, "Data Storage")
    pdf_canvas.drawString(width - 200, height - 50, "Relatório Geral")

    table_top_y = height - 90
    row_height = 20
    col_widths = [80, 60, 70, 70, 60, 60, 70]

    headers = ["Fornecedores", "Marcas", "Categorias", "Produtos", "Entradas", "Saídas", "Usuários"]
    values = [
        totalities["Fornecedores"],
        totalities["Marcas"],
        totalities["Categorias"],
        totalities["Produtos"],
        totalities["Entradas"],
        totalities["Saídas"],
        totalities["Usuários"],
    ]

    x_position = 40
    pdf_canvas.setFont("Helvetica-Bold", 10)
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x_position + 5, table_top_y - 15, header)
        pdf_canvas.rect(x_position, table_top_y - row_height, col_widths[i], row_height)
        x_position += col_widths[i]

    y_position = table_top_y - row_height
    x_position = 40
    pdf_canvas.setFont("Helvetica", 10)
    for i, value in enumerate(values):
        pdf_canvas.drawString(x_position + 5, y_position - 15, str(value))
        pdf_canvas.rect(x_position, y_position - row_height, col_widths[i], row_height)
        x_position += col_widths[i]

    pdf_canvas.save()
