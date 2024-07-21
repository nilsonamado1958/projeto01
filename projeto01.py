from fpdf import FPDF

projeto = input("Digite a descricao do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")

valor_total = int(horas_previstas) * int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, str(horas_previstas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, str(prazo))
pdf.text(115, 205, str(valor_total))

pdf.output("orcamento.pdf")
print("Orcamento gerado com sucesso")
