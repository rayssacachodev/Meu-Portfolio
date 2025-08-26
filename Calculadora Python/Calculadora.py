print("Digite o primeiro numero")
primeiro_numero = int(input())
print("digite o segundo numero")
segundo_numero = int(input())
print("Para somar, escreva soma, para multiplicar, escreva multiplicação, para dividir, escreva divisão, para subtrair, escreva subtração, para potenciar, escreva potência, para achar a raiz quadrada do primeiro número, escreva raiz quadrada 1, para raiz quadrada do segundo número, escreva raiz quadrada 2")
operacao = str(input())

if operacao == "soma":
  resultado = primeiro_numero + segundo_numero

elif operacao == "subtração":
  resultado = primeiro_numero - segundo_numero

elif operacao == "multiplicação":
  resultado = primeiro_numero * segundo_numero

elif operacao == "divisão":
  resultado = primeiro_numero / segundo_numero

elif operacao == "potência":
  resultado = primeiro_numero ** segundo_numero

elif operacao == "raiz quadrada 1":
  resultado = primeiro_numero ** 0.5

elif operacao == "raiz quadrada 2":
  resultado = segundo_numero ** 0.5

else:
  resultado = "Operação não encontrada"

print("O resultado é:")
print(resultado)
