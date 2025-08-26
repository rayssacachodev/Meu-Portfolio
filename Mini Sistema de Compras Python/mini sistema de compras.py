#mensagem de boas-vindas
print("Bem-vindo a loja da Rayssa Cacho Pedrosa!")

#solicito que a pessoa insira o valor do pedido e converto para número flutuante.
ValordoPedido = float(input("O valor do pedido é:"))

#solicito que a pessoa insira a quantidade de parcelas e converto para número inteiro.
QuantidadeParcelas = int(input("A quantidade de parcelas é:"))

#verifico a quantidade de parcelas e defino a taxa dos juros correspondente.
if QuantidadeParcelas < 4:
     Juros = 0/100   #sem juros se parcelado em até 3 vezes.
elif QuantidadeParcelas >= 4 and QuantidadeParcelas < 6:
     Juros = 4/100   #4% de juros se parcelado em 4 ou 5 vezes.
elif QuantidadeParcelas >= 6 and QuantidadeParcelas < 9:
     Juros = 8/100   #8% de juros se parcelado em 6, 7 ou 8 vezes.
elif QuantidadeParcelas >= 9 and QuantidadeParcelas < 13:
     Juros = 16/100  #16% de juros se parcelado em 9, 10, 11 ou 12 vezes.
else:
     Juros = 32/100  #32% de juros se parcelado em 13 ou mais parcelas.

#calculo do valor de cada parcela com os juros.
ValordaParcela = (ValordoPedido * (1+Juros))/(QuantidadeParcelas)

#calculo do valor total somado com as parcelas.
ValorTotalParcelado = ValordaParcela*QuantidadeParcelas

#resultado
print(f"O valor das parcelas é de: {ValordaParcela}")
print(f"O valor total parcelado é de: {ValorTotalParcelado}")

