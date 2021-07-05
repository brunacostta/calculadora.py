from datetime import date

nome_anuncio = input("Digite o nome do seu anúncio: ")
cliente = input("Digite o nome do cliente: ")
data_inicio = input("Digite a data de ínicio do anúncio YYYY-MM-DD: ")
data_termino = input("Digite a data de término do anúncio YYYY-MM-DD: ")
investiment_dia = input("Digite o valor do investimento diário: ")

print("\nNome do anúncio: {}".format(nome_anuncio) + "\n" + "Nome do cliente: {}".format(cliente) + "\n" + "Data de início do anúncio: {}".format(data_inicio) + "\n" + "Data de término do anúncio: {}".format(data_termino) + "\n" + "Valor do investimento diário: R$ {}".format(investiment_dia) + "\n")

year, month, day = map(int, data_inicio.split('-'))
date1 = date(year, month, day)

year, month, day = map(int, data_termino.split('-'))
date2 = date(year, month, day)

total_data = date2 - date1
print("Quantidade total de dias investidos: {} dias".format(total_data.days))
dias_invest = print("Valor total do investimento: R$ {0:.2f}".format(total_data.days * float(investiment_dia)))
